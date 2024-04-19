from notion_client import Client
import unicodedata

class SDK_Handler:
    def __init__(self, TOKEN):
        self.notion   = Client(auth=TOKEN)
        self.API_NAME = self.notion.users.me()['name']
        self.properties_exceptions = [
            'created_by',
            'formula',
            'last_edited_by',
            'last_edited_time',
            'relation',
            'unique_id']

    def getUsers(self):
        users = self.notion.users.list()['results']
        filtered_u = [user for user in users if not user['name'] == self.API_NAME]
        normalized_u = []
        for user in filtered_u:
            name = unicodedata.normalize('NFKD', user['name'])
            user['name'] = name.encode('ascii', 'ignore').decode('utf-8')
            normalized_u.append(user)
        return normalized_u

    def getDatabase(self, DATABASE_ID):
        return self.notion.databases.retrieve(database_id=DATABASE_ID)
    
    def getProperties(self, DB):
        properties = dict()
        for p, content in DB['properties'].items():
            type_ = content['type']

            if type_ in self.properties_exceptions: continue

            match type_:

                case 'people':
                    properties[p] = {type_ : sdk.getUsers()}
                    continue

                case 'date':
                    properties[p] = {type_ : {
                        "start": "2021-08-13T00:00:00Z",
                    }}
                    continue

                case 'title':
                    properties[p] = {type_ : [
                        {
                            "type": "text",
                            "text": {
                                "content": "This is a title",
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": "This is a title",
                        }
                    ]}
                    continue
        
            if 'options' in content[type_].keys():
                properties[p] = {type_ : content[type_]['options']}
            else:
                properties[p] = {type_ : content[type_]}

        return properties

    
    def getAllEntries(self, DATABASE_ID):
        return self.notion.databases.query(database_id=DATABASE_ID)
    
    def postPage(self, DATABASE_ID, properties):
        new_page = self.notion.pages.create(
            parent={"type":"database_id",
                    "database_id": DATABASE_ID},
            properties=properties
        )
        return new_page

if __name__ == '__main__':
    import json
    from pprint import pprint

    TOKEN = "secret_wAnmWlt6aTjbSE6mjC9dQ6BxKSGPGXtHsVavRJBb7nF"
    DASHBOARD_ID = "1b824f5ebbcd435ab1aacc6fcc5c5586"
    TASKS_DB_ID  = "42796bc1-7a09-4fa7-b18b-36483473eb5d"

    sdk = SDK_Handler(TOKEN)
    tasks_db = sdk.getDatabase(TASKS_DB_ID)
    db_properties = sdk.getProperties(tasks_db)

    page_properties = dict()
    for property_, format_ in db_properties.items():

        if 'title' in format_.keys():
            page_properties[property_] = format_
            title = input("Title: ")
            page_properties[property_]['title'][0]['text']['content'] = title
            page_properties[property_]['title'][0]['plain_text'] = title
            continue
        if 'date' in format_.keys():
            page_properties[property_] = format_
            date = input("Date: ")
            page_properties[property_]['date']['start'] = date
            continue
        if 'rich_text' in format_.keys(): continue

        if 'people' in format_.keys():
            print("People:")
            for i, person in enumerate(format_['people']):
                print(f"Person {i}: {person['name']}")
            choice = int(input("Choose a person: "))
            page_properties[property_] = {'people': [{
                "object": "user",
                "id": format_['people'][choice]['id']
            }]}
            continue
        
        if 'multi_select' in format_.keys():
            print("Multi Select:")
            for i, option in enumerate(format_['multi_select']):
                print(f"Option {i}: {option['name']}")
            choice = int(input("Choose an option: "))
            page_properties[property_] = {'multi_select': [
                {"name": format_['multi_select'][choice]['name']}
            ]}
            continue

        for type_, content in format_.items():
            print(f"Type: {type_}")
            for i, option in enumerate(content):
                print(f"Option {i}:")
                pprint(option)
            
        choice = int(input("Choose an option: "))
        page_properties[property_] = {type_: 
            {"name": content[choice]['name']}}

    # pprint(page_properties)
    with open('tests.json', 'w') as f:
        json.dump(page_properties, f, indent=4)
    new_page = sdk.postPage(TASKS_DB_ID, page_properties)
    # pprint(new_page)