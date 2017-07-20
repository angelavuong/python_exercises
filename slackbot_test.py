'''
Name: slackbot_test.py
Purpose: With provided token, the bot slacks a user with a test message.
'''

import os
from slackclient import SlackClient

BOT_NAME = 'snowflake-bot'
token = 'XXX'
slack_client = SlackClient(token)

if __name__ == "__main__":
    slack_client.api_call("chat.postMessage", channel="@angela-vuong",text=str("Test Sucessful"), as_user=True)
