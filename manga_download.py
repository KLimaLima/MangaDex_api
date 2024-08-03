import requests
import os
import sys

import util
from CONSTANTS import *

# THIS IS CHAPTER ID, NOT MANGA ID
def chp_get_component(chp_id: str):

    response = requests.get(
        f'{URL_CHP_ID}/{chp_id}'
        )
    
    response = response.json()

    return response[KEY_CHP_URL], response[KEY_CHP][KEY_CHP_HASH], response[KEY_CHP][KEY_DATA], response[KEY_CHP]['dataSaver']

# TODO: extract data for chp volume and description
# FIXME: data_saver is not working(only high quality is working)
# FIXME: maybe can print downloading and skipped message here(do before doing get request; chp_get_component())
# Problem is probably due to chp_id being passed is the high quality data
# not suitable with link data-saver as link data-saver use different chp_id
# FIXME: handle folder(if downloading failed, delete the folder indicating that the download is not successful)
def one_chp(chp_id: str, data_saver: bool= True):

    try:
        manga_title = chp_id['relationships'][1]['attributes']['title']['en']
        chp_number = chp_id['attributes']['chapter']
        folder_path = f'MangaDex/{manga_title}/chp{chp_number}'
        os.makedirs(folder_path)
    except FileExistsError:
        print('Skipped:', manga_title, 'chapter', chp_number, 'already exists')
        return
    
    try:
        url, hash, pages_original, pages_low_quality = chp_get_component(chp_id[KEY_ID])
    except:
        print('Skipped: could not get response, check internet connection')
        os.rmdir(folder_path)
        # sys.exit(0)
        return
    
    # url, hash, pages_original, pages_low_quality = chp_get_component(chp_id[KEY_ID])
    # os.makedirs(folder_path, exist_ok= True)

    quality = KEY_DATASAVER
    pages = pages_low_quality
    if(not data_saver):
        quality = KEY_DATA
        pages = pages_original

    print('Downloading:', manga_title, 'chapter' ,chp_number)

    for page in pages:

        file_type = util.get_file_type(page)
        page_number = util.get_page_number(page)

        try:
            downloading = requests.get(
                f'{url}/{quality}/{hash}/{page}',
                timeout= 3
            )
            with open(f'{folder_path}/{manga_title}_chp{chp_number}_{page_number}.{file_type}', 'wb') as writing:
                writing.write(downloading.content)
        except TimeoutError:
            print('Took too long to response:', manga_title, 'chapter' ,chp_number)
        except Exception as error:
            print(error)
            print('Failed:', manga_title, 'chapter' ,chp_number)
            # writing.close()
        # downloading = requests.get(
        #     f'{url}/{quality}/{hash}/{page}'
        # )

        # with open(f'{folder_path}/{manga_title}_chp{chp_number}_{page_number}.{file_type}', 'wb') as writing:
        #     writing.write(downloading.content)
    # TODO: dont write when exception occurs, put in else
    print('Successful:', manga_title, 'chapter' ,chp_number)

def all_chps(chp_ids: list[str], data_saver: bool= True):

    for chp_id in chp_ids:
        one_chp(chp_id, data_saver= data_saver)
        # try:
        #     manga_title = chp_id['relationships'][1]['attributes']['title']['en']
        #     chp_number = chp_id['attributes']['chapter']
        #     folder_path = f'MangaDex/{manga_title}/chp{chp_number}'
        #     os.makedirs(folder_path)
        # except FileExistsError:
        #     # there is already chp[number] here, meaning already downloaded this one
        #     # so skip(no need to redownload again)
        #     print('Skipped:', manga_title, 'chapter', chp_number, 'already exists')
        #     continue
        # else:
        #     print('Downloading:', manga_title, 'chapter' ,chp_number)
        #     one_chp(chp_id, data_saver= data_saver)