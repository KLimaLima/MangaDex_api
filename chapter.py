import os
import requests

import util_filename
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

    def __init__(self, manga_title: str) -> None:

        self.id: str

        self.url: str
        self.hash: str
        self.pages_original_quality: str
        self.pages_low_quality: str

        self.manga_title: str = manga_title

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

    def set_metadata_aggregate(self, id, volume, chapter):

        # TODO: make a util finction that takes chp_number and converts it to double digits

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
        self.pages_original_quality = response[KEY_CHP][KEY_DATA]
        self.pages_low_quality = response[KEY_CHP]['dataSaver']

        return True
    
    def download(self, folder_path: str, data_saver: bool= True):
        
        if not self.get_components():
            self.error_message('Unable to get components')
            return False

        folder_path += f'/chp{self.chapter}'

        os.makedirs(folder_path)

        quality = KEY_DATASAVER
        pages = self.pages_low_quality
        if not data_saver:
            quality = KEY_DATA
            pages = self.pages_original_quality

        for page in pages:

            file_type = util_filename.get_file_type(page)
            page_number = util_filename.get_page_number(page)

            try:
                downloading = requests.get(
                    f'{self.url}/{quality}/{self.hash}/{page}',
                    timeout= TIMEOUT
                )

                with open(f'{folder_path}/{page_number}_chp{self.chapter}_{self.manga_title}.{file_type}', 'wb') as writing:
                    writing.write(downloading.content)

            except Exception as error:
                self.error_message(str(error))
                return False

            else:
                print(f'Downloaded page: {page_number} chapter: {self.chapter} manga: {self.manga_title}')

        return True

    def error_message(self, message: str):
        print(f'chapter id: {self.id}\nerror: {message}')