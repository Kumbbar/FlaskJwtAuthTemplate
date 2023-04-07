import os

from dotenv import load_dotenv


# Load .env file
load_dotenv()


class Config:
    SALT: str = os.environ.get('SALT')
    JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS: str = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


config_dict = {atr: getattr(Config, atr) for atr in dir(Config) if not atr.startswith('__')}