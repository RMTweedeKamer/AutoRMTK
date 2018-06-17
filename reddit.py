import praw
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def client():
   return praw.Reddit(user_agent='AutoRMTK (by /u/-___-_)',
                      client_id=os.getenv('AUTORMTK_CLIENT_ID'),
                      client_secret=os.getenv('AUTORMTK_CLIENT_SECRET'),
                      username=os.getenv('AUTORMTK_USERNAME'),
                      password=os.getenv('AUTORMTK_PASSWORD'),
                      check_for_updates=False)
