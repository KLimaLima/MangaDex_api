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

        # refactor these; used the manga feed endpoints
        self.id: str
        self.attributes: str
        self.relationships: str

        self.volume: str
        self.chapter: str
        self.title: str
        self.lang: str
        self.pages: str
        self.version: str

    def set_metadata_feed(self, chp_dict: dict):

        self.id = chp_dict[ID]
        self.attributes = chp_dict[ATTR]
        self.relationships = chp_dict[RELATIONSHIP]

        self.volume = self.attributes[VOL]
        self.chapter = self.attributes[CHP]
        self.title = self.attributes[TITLE]
        self.lang = self.attributes[LANG]
        self.pages = self.attributes[PAGES]
        self.version = self.attributes[VER]

    def set_metadata_aggregate(self, id, volume, chapter):

        self.id = id
        self.volume = volume
        self.chapter = chapter

        print(f'id:{self.id}, volume:{self.volume}, chapter:{self.chapter}')

    def get_components(self):

        response = requests.get(
            f'{URL_CHP_ID}/{self.id}',
            timeout= TIMEOUT
        )

        response = response.json()

        return response[KEY_CHP_URL], response[KEY_CHP][KEY_CHP_HASH], response[KEY_CHP][KEY_DATA], response[KEY_CHP]['dataSaver']