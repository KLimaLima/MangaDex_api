import requests

from CONSTANTS import *

# FIXME: Refactor to be similar to get_list
def get_list_all(manga_id: str):

    response = requests.get(
        f'{URL_BASE}/manga/{manga_id}/feed'
        )
    
    # print(response.json())
    response = response.json()
    # print('data', response[KEY_DATA])
    return response[KEY_DATA]

def get_list(manga_id: str, languages: list[str] = [ENGLISH]):

    response = requests.get(
        f'{URL_BASE}/manga/{manga_id}/feed',
            
        params= {
            'translatedLanguage[]': languages,
            'includes[]': 'manga'
            }
    )

    '''
    available keys are: result, response, data, limit, offset, total

    data is list of chapters in dict

    each chapters(referring to index) has (in dict) keys: id, type, chapters, attributes(a dict) and relationships
    attributes has keys: volume, chapter, title, createdAt, updatedAt, pages, version, translatedLanguage, externalUrl, publishAt, readableAt
    '''
    response = response.json()

    # for i in response[KEY_DATA]:
    #     print('chp_id, get_list=>', i)

    # print('result: ', response[KEY_DATA][0]['relationships'][1]['attributes']['title']['en'])
    # for i in response[KEY_DATA]:
    #     print('result', i['relationships'][1]['attributes']['title']['en'])

    # print('chp_id, get_list=>', response.keys())
    # print('chp_id, get_list[data]=>', response[KEY_DATA])
    # print('chp_id, get_list[data]=>', response[KEY_DATA][0])

    return response[KEY_DATA]