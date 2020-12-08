
import configparser
import os
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pkg_resources

Base = declarative_base()

class SingletonDBSession:

  instance = None

  class DBSession:

    def __init__(self):
      engine_string = self.get_engine_string()
      engine = create_engine(engine_string)
      Session = sessionmaker(bind=engine)
      self.session = Session()

    def get_engine_string(self):
      config = configparser.ConfigParser()
      config.read(pkg_resources.resource_filename("gbtc_tracker.config", 'database.ini'))

      host = config['test'].get('host')
      user = config['test'].get('username')
      pw = config['test'].get('password')
      dbname = config['test'].get('database')
      return f"oracle://{user}:{pw}@{host}/PROD9"

  def __new__(self):
    if not SingletonDBSession.instance:
      SingletonDBSession.instance = SingletonDBSession.DBSession()
    return SingletonDBSession.instance.session

class ConnectionStringBuilder:

  @staticmethod
  def build_engine_string():
    config = configparser.ConfigParser()
    config.read(pkg_resources.resource_filename("abml_load.config", 'database.ini'))
    host = config['test'].get('host')
    user = config['test'].get('username')
    pw = config['test'].get('password')
    dbname = config['test'].get('database')
    return f"mysql://{user}:{pw}@{host}/{dbname}"