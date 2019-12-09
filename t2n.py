from notion.client import NotionClient
from notion.block import *
import logging
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="<NOTION_TOKEN>",monitor=False)

# Replace this URL with the URL of the page you want to edit
page = client.get_block("<URL_OF_PAGE>")

print("The page title is:", page.title)

def addTextBlock(text):
    #for child in page.children:
    #    print(child.title)
    newchild = page.children.add_new(TextBlock, title=text)
    print(newchild)
    return newchild
    #print("Parent of {} is {}".format(page.id, page.parent.id))
    #print(newchild)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    result = addTextBlock(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Block added with id:'+str(result.id))

def initTelegram:
    updater = Updater(token='988894343:AAF8QugfGFSssOBpkGtXfme1pejN8bnirvg', use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    print('Bot Polling Started')
    updater.start_polling()

if __name__ == "__main__":
    initTelegram()
