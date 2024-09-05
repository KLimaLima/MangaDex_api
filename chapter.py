import requests

from CONSTANTS import *

ID = 'id'
ATTR = 'attributes'
RELATIONSHIP = 'relationships'
VOL = 'volume'
CHP = 'chapter'
TITLE = 'title'
LANG = 'translatedLanguage'
PAGES = 'pages'
VER = 'version'

class Chapter:

    def __init__(self) -> None:

        self.id: str

        self.url: str
        self.hash: str
        self.original_quality: str
        self.low_quality: str

        self.manga_title: str

        self.volume: str
        self.chapter: str
        self.title: str
        self.lang: str
        self.pages: str
        self.version: str

    def set_metadata_feed(self, cartel_feed: dict):

        self.id = cartel_feed[ID]
        attributes = cartel_feed[ATTR]
        relationships = cartel_feed[RELATIONSHIP]

        self.volume = attributes[VOL]
        self.chapter = attributes[CHP]
        self.title = attributes[TITLE]
        self.lang = attributes[LANG]
        self.pages = attributes[PAGES]
        self.version = attributes[VER]

    def set_metadata_aggregate(self, manga_title, id, volume, chapter):

        # TODO: make a util finction that takes chp_number and converts it to double digits

        self.manga_title = manga_title
        self.id = id
        self.volume = volume
        self.chapter = chapter

        print(f'id:{self.id}, volume:{self.volume}, chapter:{self.chapter}')

    def get_components(self):

        try:
            response = requests.get(
                f'{URL_CHP_ID}/{self.id}',
                timeout= TIMEOUT
                )

        except Exception as error:
            print(f'Error in chapter.py\nerror:{error}')
            return False
        
        response = response.json()

        self.url = response[KEY_CHP_URL]
        self.hash = response[KEY_CHP][KEY_CHP_HASH]
        self.original_quality = response[KEY_CHP][KEY_DATA]
        self.low_quality = response[KEY_CHP]['dataSaver']

        return True
    
    def download(self, data_saver: bool= True):
        
        if not self.get_components():
            self.error_message('Unable to get components')

    def error_message(self, message: str):
        print(f'chapter id: {self.id}\nerror: {message}')