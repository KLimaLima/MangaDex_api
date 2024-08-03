import requests
import json
import sys

from CONSTANTS import *

'''
available keys are: result, response, data, limit, offset, total

data is list of chapters in dict

each chapters(referring to index) has (in dict) keys: id, type, chapters, attributes(a dict) and relationships
attributes has keys: volume, chapter, title, createdAt, updatedAt, pages, version, translatedLanguage, externalUrl, publishAt, readableAt
'''

# FIXME: Refactor to be similar to get_list
def get_all(manga_id: str):

    response = requests.get(
        f'{URL_BASE}/manga/{manga_id}/feed'
        )
    
    response = response.json()
    return response[KEY_DATA]

# TODO: do pagination if exist
def get_filtered(manga_id: str, languages: list[str] = [ENGLISH]):

    try:
        response = requests.get(
            f'{URL_BASE}/manga/{manga_id}/feed',
            params= {
                'translatedLanguage[]': languages,
                'includes[]': 'manga',
                'order[chapter]': 'asc'
            }            
        )        
    except Exception as error:
        print(f'Error: {error}\nSkipped: could not get response, check internet connection')
        sys.exit(0)

    response = response.json()

    return response[KEY_DATA]