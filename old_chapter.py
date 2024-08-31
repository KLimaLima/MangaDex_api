import requests
import os
import sys

import filename_data
import old_response_crawler
from CONSTANTS import *

# THIS IS CHAPTER ID, NOT MANGA ID
def get_components(chp_id: str):

    response = requests.get(
        f'{URL_CHP_ID}/{chp_id}',
        timeout= TIMEOUT
        )
    
    response = response.json()

    return response[KEY_CHP_URL], response[KEY_CHP][KEY_CHP_HASH], response[KEY_CHP][KEY_DATA], response[KEY_CHP]['dataSaver']

# TODO: Create a feature to check if data is empty or not
# FIXME: Refactor to be similar to get_list
def ids_get_all(manga_id: str):

    response = requests.get(
        f'{URL_BASE}/manga/{manga_id}/feed'
        )
    
    response = response.json()
    return response[KEY_DATA]

# TODO: do pagination if exist
def ids_get_filtered(manga_id: str, languages: list[str] = [ENGLISH]):

    try:
        response = requests.get(
            f'{URL_BASE}/manga/{manga_id}/feed',
            params= {
                'translatedLanguage[]': languages,
                'includes[]': 'manga',
                'order[chapter]': 'asc',
                'contentRating[]': ['safe', 'suggestive', 'erotica', 'pornographic']
            },
            timeout= TIMEOUT
        )
        # print('url: ', response.url)
    except Exception as error:
        print(f'Error: {error}\nSkipped: could not get response for {manga_id}, check internet connection')
        sys.exit(0)

    print(response.url)

    response = response.json()
    # print(response)

    return response[KEY_DATA]

# TODO: extract data for chp volume, description and chapter title
# FIXME: data_saver is not working(only high quality is working) NOT YET CHECKED 24/8/2024
# FIXME: maybe can print downloading and skipped message here(do before doing get request; chp_get_component())
# FIXME: handle folder(if downloading failed, delete the folder indicating that the download is not successful)
def download_one(chp_id: str, data_saver: bool= True):

    try:
        # TODO: make it so that all other similar code does the same
        manga_title = old_response_crawler.list_of_dict(chp_id['relationships'], 'type', 'manga')
        manga_title = manga_title[0]['attributes']['title']['en'] # TODO: Currently just use the first element in list
        chp_number = chp_id['attributes']['chapter']

        folder_path = f'MangaDex/{manga_title}/chp{chp_number}'
        os.makedirs(folder_path)

        url, hash, pages_original, pages_low_quality = get_components(chp_id[KEY_ID])

    except FileExistsError:
        print('Skipped:', manga_title, 'chapter', chp_number, 'already exists')
        return
    
    except Exception as error:
        print(f'{error}\nSkipped: could not get response for {manga_title}, check internet connection')
        # TODO: create function to handle delete whole folder, wheter there is files in it or not by default
        os.rmdir(folder_path)
        sys.exit(0)
    
    quality = KEY_DATASAVER
    pages = pages_low_quality
    if(not data_saver):
        quality = KEY_DATA
        pages = pages_original

    print('Downloading:', manga_title, 'chapter' ,chp_number)
    progress = True

    for page in pages:

        file_type = filename_data.get_file_type(page)
        page_number = filename_data.get_page_number(page)

        try:
            downloading = requests.get(
                f'{url}/{quality}/{hash}/{page}',
                timeout= TIMEOUT
            )
            with open(f'{folder_path}/{manga_title}_chp{chp_number}_{page_number}.{file_type}', 'wb') as writing:
                writing.write(downloading.content)
        except TimeoutError:
            print('Took too long to response:', manga_title, 'chapter' ,chp_number)
        except Exception as error:
            print(error)
            print('Failed:', manga_title, 'chapter' ,chp_number)
            progress = False
            break
    
    if progress:
        print('Successful:', manga_title, 'chapter' ,chp_number)

def download_all(chp_ids: list[str], data_saver: bool= True):

    for chp_id in chp_ids:
        download_one(chp_id, data_saver= data_saver)