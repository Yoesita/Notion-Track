import os
from notion_client import Client
from pprint import pprint

def createBlock(TOKEN, PAGE_ID):


def main():
    TOKEN   = os.environ.get('Notion_Key')
    PAGE_ID = os.environ.get('Notion_Page')
    
    notion = Client(auth=TOKEN)
    list_users_response = notion.users.list()
    pprint(list_users_response)

if __name__ == '__main__':
    main()


