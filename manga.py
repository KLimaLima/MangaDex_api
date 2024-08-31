import requests

import pathlib
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED

import util_response
from chapter import Chapter

from CONSTANTS import *

# class Manga will help in when creating cbz files to put metadata and other stuff as well

# new plan; to get the manga metadata, just request for 1 first only
# afterwards get the next chp ids in bulk without manga reference expansion (but scanlation and users if hoshi)
# Manga manages the chapters
class Manga:

    total_downloaded = 0

    def __init__(self, manga_id: str, *pref_lang) -> None:

        self.id = manga_id

        self._cartel_metadata = None
        self._cartel_aggregate = None
        self._cartel_feed = None

        self.title: dict[str] #✔️
        self.alt_title: dict[str] #✔️ prob; list_dict_to_dict_list not tested yet
        self.description: dict[str] #✔️
        self.original_lang: str #✔️

        self.chapters: list[Chapter] = []
        self.chapters_num: list[float]

        # util properties
        self.pref_lang: tuple = pref_lang
        self.root_folder_name: str = 'MangaDex'

    # https://api.mangadex.org/docs/redoc.html#tag/Manga/operation/get-manga-id-feed
    # gives more information about chapters such as title if exist
    def get_chapters_feed(self, manga_id: str, languages: list[str]):

        try:
            response = requests.get(
                f'{URL_BASE}/manga/{manga_id}/feed',
                params= {
                    'translatedLanguage[]': languages,
                    # 'includes[]': 'manga', # use self.get_manga_metadata
                    'order[chapter]': 'asc',
                    'contentRating[]': ['safe', 'suggestive']
                },
                timeout= TIMEOUT
            )

            response = response.json()
            self._cartel_feed = response[KEY_DATA]

        except Exception as error:
            print(f'manga id: {self.id}, error: {error}')
            return False

        return True
    
    # https://api.mangadex.org/docs/redoc.html#tag/Manga/operation/get-manga-aggregate
    # is more focused on delivering ids and minimal information on chapters
    # also does not have utilities such as sort
    def get_chapters_aggregate(self):

        try:
            response = requests.get(
                f'{URL_BASE}/manga/{self.id}/aggregate',
                params= {
                    'translatedLanguage[]': self.pref_lang[0]
                },
                timeout= TIMEOUT
            )

            response = response.json()
            self._cartel_aggregate = response['volumes']

        except Exception as error:
            self.error_message(str(error))
            return False

        return True
    
    # https://api.mangadex.org/docs/redoc.html#tag/Manga/operation/get-manga-id
    # gives information about the manga
    def get_manga_metadata(self):

        try:
            response = requests.get(
                f'{URL_BASE}/manga/{self.id}',
                timeout= TIMEOUT
            )

            response = response.json()
            self._cartel_metadata = response['data']

        except Exception as error:
            print(f'manga id: {self.id}, error: {error}')
            return False

        return True
    
    def update_manga_metadata(self):

        if not self.get_manga_metadata():
            self.error_message('Unable to get data from server')
            return False

        if metadata['id'] != self.id:
            self.error_message('Different json was received')
            return False
        
        metadata = metadata['attributes']

        self.original_lang = metadata['originalLanguage']
        # this 'appends' the original language to pref_lang so that it takes the original language if user prefered language is not available
        self.pref_lang += self.original_lang,

        self.title = util_response.dict_values_grabber(metadata['title'], self.pref_lang)
        self.description = util_response.dict_values_grabber(metadata['description'], self.pref_lang)
        self.alt_title = util_response.dict_values_grabber(util_response.list_dict_to_dict_list(metadata['altTitles']),self.pref_lang)

        print(f'About Manga >\ntitle:{self.title}, desc:{self.description}, alt_title:{self.alt_title}')

    def zip_cbz_one_chp(self, chp_num: float):

        dir_to_zip = f'./{self.root_folder_name}/{util_response.dict_1_value_chooser(data= self.title, keys= self.pref_lang)}/chp{chp_num}'
        the_zip_file = f'{dir_to_zip}.zip'

        folder = pathlib.Path(dir_to_zip)

        # for file in folder.iterdir():
        #     print(file)

        with ZipFile(the_zip_file, 'w', ZIP_DEFLATED) as zip:
            for file in folder.iterdir():
                zip.write(file, arcname= file.name)

    def zip_cbz_chp(self):

        for chp in self.chapters_num:

            self.zip_cbz_one_chp(chp)

    def error_message(self, message: str):
        print(f'manga id: {self.id}, name: {self.id}\nerror: {message}')

    def create_chapters(self):

        if not self.get_chapters_aggregate():
            self.error_message('Could not get response from server')
            return False

        print('creating chapters')

        # DO NOT CHANGE A SINGLE
        for not_volume in self._cartel_aggregate.values():
            data = not_volume # values of vol1, vol2
            chapter_volume = not_volume['volume']
            for chapter in data['chapters'].values():
                chapter_id = chapter['id']
                chapter_num = chapter['chapter']
                append_chapter = Chapter()
                append_chapter.set_metadata_aggregate(chapter_id, chapter_volume, chapter_num)
                self.chapters.append(append_chapter)

        print('finished creating chapters')

    # def get_chapters(self):

    #     extract_me: dict = self._get_chapters_data()

    #     result = []
    #     for data in extract_me.values():
            
    #         volume = data['volume']
    #         for chapter in data['chapters'].values():
    #             result.append({'id': chapter['id'], 'volume': volume, 'chapter': chapter['chapter'], 'id_other': chapter['others']})

    #     return result

    # this is for when using feed
    # def get_relationships(self, get_key: str):

    #     for relationship in self._bahan[self._bahan_iter]['relationships']:
    #         if relationship['type'] == get_key:
    #             return relationship
            
    # def get_by_type(self, datas: list[dict], type_to_find: str):

    #     result = []

    #     for data in datas:
    #         if data['type'] == type_to_find:
    #             result.append(data)

    #     return result

    # def get_attributes(self, get_key: str):
    #     pass

    # def create_chps(self):
    #     pass