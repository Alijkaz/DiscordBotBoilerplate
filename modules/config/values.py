from os import getenv
from modules.config import get
from dotenv import load_dotenv
from distutils.util import strtobool

class Config:   
    SAMPLE = get('sample')
        
class Env:
    load_dotenv('storage/data/.env')
    
    DEBUG = bool(strtobool(getenv('DEBUG')))
    LOG_SQL = bool(strtobool(getenv('LOG_SQL')))
    LOG_DEBUG_DISCORD = bool(strtobool(getenv('LOG_DEBUG_DISCORD')))

    TOKEN = getenv('DEBUG_TOKEN') if DEBUG else getenv('TOKEN')
    PREFIX = getenv('DEBUG_PREFIX') if DEBUG else getenv('PREFIX')
    
    DB_PATH = getenv('DB_PATH')
    CONFIG_PATH = getenv('CONFIG_PATH')

    
