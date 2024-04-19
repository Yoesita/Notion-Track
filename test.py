import os
from notion_client import Client
from pprint import pprint

def CreateBlock(client, PAGE_ID):
    new_block = client.blocks.children.append(
        block_id=PAGE_ID,
        children= [
        {
            "heading_3": {
                "rich_text": [
                {
                    "text": {
                        "content": "Tuscan  kale",
                    },
                },
                ],
            },
        },
        {
            "paragraph": {
                "rich_text": [
                {
                    "text": {
                        "content":
                            "Tuscan  kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                        "link": {
                            "url": "https://en.wikipedia.org/wiki/Kale",
                        },
                    },
                    "annotations": {
                        "bold": True,
                        "italic": True,
                        "strikethrough": True,
                        "underline": True,
                        "color": "green",
                    },
                },
                ],
            },
        },
        ],
    )
    print(new_block)

def getDB(client, PAGE_ID):
    newDatabase = client.databases.retrieve(database_id=PAGE_ID)
    for p in newDatabase['properties']:
        print(p)


def main():
    TOKEN   = os.environ.get('Notion_Key')
    PAGE_ID = os.environ.get('Notion_Page')
    
    notion = Client(auth=TOKEN)
    # CreateBlock(notion, PAGE_ID)
    getDB(notion, "fc67a4b88ab0491abc18d414c9508618")

if __name__ == '__main__':
    main()


