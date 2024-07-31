import requests
import os

import util
from CONSTANTS import *

# 5564932f-c64a-4f18-98b9-0e3867e3c861

# THIS IS CHAPTER ID, NOT MANGA ID
def chp_find_component(chp_id: str):

    response = requests.get(
        f'{URL_CHP_ID}/{chp_id}'
        )
    
    # print(response.json())
    response = response.json()
    print('chp_find_component=>', response)
    # print('chp_find_component=>', response)
    # print('chp_find_component=>', response)
    print('chp_find_component=>', type(response[KEY_CHP][KEY_DATA]))

    # print('url', response[KEY_CHP_URL])
    # print('hash', response[KEY_CHP][KEY_CHP_HASH]) # the related chp_quality hash
    # print('data', response[KEY_CHP][KEY_DATA]) # list of pages

    return response[KEY_CHP_URL], response[KEY_CHP][KEY_CHP_HASH], response[KEY_CHP][KEY_DATA]

def one_chp(chp_id: str, data_saver: bool= True):#url: str, hash: str, images: list, data_saver: bool= True):

    url, hash, pages = chp_find_component(chp_id[KEY_ID])
    manga_title = chp_id['relationships'][1]['attributes']['title']['en']
    chp_number = chp_id['attributes']['chapter']
    folder_path = f'{manga_title}/chp{chp_number}'

    os.makedirs(folder_path, exist_ok= True)

    quality = KEY_DATASAVER

    if(not data_saver):
        quality = KEY_DATA

    # TODO: Create dir/file to seperate chp
    for page in pages:

        file_type = util.get_file_type(page)
        page_number = util.get_page_number(page)

        downloading = requests.get(
            f'{url}/{quality}/{hash}/{page}'
        )

        # TODO: Create an auto filetype identifier so that it changes to the appropriate filetype
        with open(f'{folder_path}/{manga_title}_chp{chp_number}_{page_number}.{file_type}', 'wb') as writing:
            writing.write(downloading.content)

# chp = '96a41120-b7ac-4fd5-8b20-74afe3884367'
# chp_find_url(chp)

# chp_download_all('https://cmdxd98sb0x3yprd.mangadex.network', '98b8dd88a5569ec186b046469be0c934', ['1-1bb03fd29ada4db64d0baf9141200acfaab1b6acb0c81cffe902bbffbb36b675.png'], data_saver= False)

def batch_chps(chp_ids: list[str], data_saver: bool= True):

    for chp_id in chp_ids:
        one_chp(chp_id, data_saver= False)