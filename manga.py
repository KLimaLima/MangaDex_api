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

        # FIXME: use case where there is no chapters for the pref_lang
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
    def get_chapters_feed(self):

        try:
            response = requests.get(
                f'{URL_BASE}/manga/{self.id}/feed',
                params= {
                    'translatedLanguage[]': list(self.pref_lang),
                    # 'includes[]': 'manga', # use self.get_manga_metadata
                    'order[chapter]': 'asc',
                    'contentRating[]': ['safe', 'suggestive']
                },
                timeout= TIMEOUT
            )

            response = response.json()
            self._cartel_feed = response[KEY_DATA]

        except Exception as error:
            self.error_message(str(error))
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
        """
        https://api.mangadex.org/docs/redoc.html#tag/Manga/operation/get-manga-id

        Gets information about the manga.
        """

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
        """
        Updates the manga metadata
        """

        if not self.get_manga_metadata():
            self.error_message('Unable to get data from server')
            return False

        if self._cartel_metadata['id'] != self.id:
            self.error_message('Different json was received')
            return False
        
        metadata_attr = self._cartel_metadata['attributes']

        self.original_lang = metadata_attr['originalLanguage']

        temp_pref_lang: set = set(self.pref_lang)
        temp_pref_lang.add(self.original_lang) # helps to check if already in the array; if alrady exist than the size will be the same, if not size will differ
        if len(temp_pref_lang) != len(self.pref_lang):
            # this 'appends' the original language(self.original_lang) to pref_lang(self.pref_lang) so that it takes the original language if user prefered language is not available
            self.pref_lang += self.original_lang, # NOTE: this is tuple

        self.title = util_response.dict_values_grabber(metadata_attr['title'], self.pref_lang)
        self.description = util_response.dict_values_grabber(metadata_attr['description'], self.pref_lang)
        self.alt_title = util_response.dict_values_grabber(util_response.list_dict_to_dict_list(metadata_attr['altTitles']),self.pref_lang)

        print(f'About Manga >\ntitle:{self.title}\ndesc:{self.description}\nalt_title:{self.alt_title}')
        return True
    
    def cbz_one_chp(self, chp: Chapter):

        title_in_lang = util_response.dict_1_value_chooser(data= self.title, keys= self.pref_lang)

        dir_to_zip = f'./{self.root_folder_name}/{title_in_lang}/chp{chp.chapter}'
        the_zip_file = f'{dir_to_zip}.cbz'

        folder = pathlib.Path(dir_to_zip)

        # for file in folder.iterdir():
        #     print(file)

        with ZipFile(the_zip_file, 'w', ZIP_DEFLATED) as zip:
            for file in folder.iterdir():
                zip.write(file, arcname= file.name)

    def cbz_chp_all(self):

        for chp in self.chapters:

            self.cbz_one_chp(chp)

    def error_message(self, message: str):
        print(f'manga id: {self.id}\nerror: {message}')

    def create_chapters_aggregate(self):

        if not self.get_chapters_aggregate():
            self.error_message('Could not get response from server')
            return False
        
        if not self._cartel_aggregate:
            self.error_message('Response is empty: There is no chapter available in the language')
            return False

        print('creating chapters')

        # DO NOT CHANGE A SINGLE FUCKING THING HERE
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

        self.chapters.sort(key=lambda x: float(x.chapter))

        return True