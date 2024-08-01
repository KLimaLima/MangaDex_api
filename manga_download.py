import requests
import os

import util
from CONSTANTS import *

# THIS IS CHAPTER ID, NOT MANGA ID
def chp_get_component(chp_id: str):

    response = requests.get(
        f'{URL_CHP_ID}/{chp_id}'
        )
    
    response = response.json()

    return response[KEY_CHP_URL], response[KEY_CHP][KEY_CHP_HASH], response[KEY_CHP][KEY_DATA]

def one_chp(chp_id: str, data_saver: bool= True):

    url, hash, pages = chp_get_component(chp_id[KEY_ID])
    manga_title = chp_id['relationships'][1]['attributes']['title']['en']
    chp_number = chp_id['attributes']['chapter']
    folder_path = f'MangaDex/{manga_title}/chp{chp_number}'

    os.makedirs(folder_path, exist_ok= True)

    quality = KEY_DATASAVER
    if(not data_saver):
        quality = KEY_DATA

    for page in pages:

        file_type = util.get_file_type(page)
        page_number = util.get_page_number(page)

        downloading = requests.get(
            f'{url}/{quality}/{hash}/{page}'
        )

        with open(f'{folder_path}/{manga_title}_chp{chp_number}_{page_number}.{file_type}', 'wb') as writing:
            writing.write(downloading.content)

def all_chps(chp_ids: list[str], data_saver: bool= True):

    for chp_id in chp_ids:
        print(chp_id)

    for chp_id in chp_ids:
        try:
            manga_title = chp_id['relationships'][1]['attributes']['title']['en']
            chp_number = chp_id['attributes']['chapter']
            folder_path = f'MangaDex/{manga_title}/chp{chp_number}'
            os.makedirs(folder_path)
        except FileExistsError:
            # there is already chp[number] here, meaning already downloaded this one
            # so skip(no need to redownload again)
            print('Skipped:', manga_title, 'chapter', chp_number, 'already exists')
            continue
        else:
            print('Downloading:', manga_title, 'chapter-' ,chp_number)
            one_chp(chp_id, data_saver= data_saver)