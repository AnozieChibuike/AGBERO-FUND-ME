from dotenv import load_dotenv
import os 

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('APP_SECRET','John')