import requests
import re

import manga_download
import chp_id

from CONSTANTS import *

# TODO: make log file to get data about url used and to check success or failure
# as of now hero killer and some other manga cannot response with image if using data-saver?
# could be 

hero_killer = '163306e6-1700-42a4-882f-26db124cbec2'

ol_vtuber_to_oshi_jk_chan = '6d216412-2453-451b-91b6-bedfcd9639d4'

Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life = '23aadc44-d2fe-46ca-83a6-6c86fd36ee12'

the_beginner_formerly_ranked_number_one_in_the_world = '7139b5c1-3740-4bf4-a157-2888af7f2420'

chp_ids = chp_id.get_filtered('0051e50a-e30c-4bb2-b378-c3da82463ee1')
manga_download.all_chps(chp_ids, data_saver= False)

# chp_ids = chp_id.get_list(ol_vtuber_to_oshi_jk_chan)
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life)
# manga_download.all_chps(chp_ids, False)

# res = requests.get(
#     'https://api.mangadex.org/manga/02b80fce-8fd0-46dc-a6e4-a65f701fde4a/feed',
#     params= {
#         'translatedLanguage[]': ['en'],
#         # 'includes[]': 'manga'
#         }
# )

# print(res.json())

# match = re.findall(r'\'translatedLanguage\': \'([\w-]*)\'', str(res.json()))

# print(match)

# chp_ids = chp_id.get_list(the_beginner_formerly_ranked_number_one_in_the_world)
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('a0f5d36b-3af9-412a-ae65-8973bad10245')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('0051e50a-e30c-4bb2-b378-c3da82463ee1')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('9a414441-bbad-43f1-a3a7-dc262ca790a3')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('1b72739a-7626-495e-a50d-fd1f52bc4397')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('0a4915d7-e84e-4d14-b7bf-c14a3a0995e0')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('f817d19e-e377-4fe3-b3e7-a334e80fb6f7')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('51b8571f-7277-4e48-b6e5-58c3ebca1143')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('7bf163e3-123a-41c1-b2bc-8254dbe5a09b')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('c3911129-c183-402a-a415-cfd4a08aa746')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('bcf927d8-52e3-4d6f-a2da-4eb37abe91c9')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('7bd45a18-27d4-43ba-b3b9-2293f9a957d0')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('a3c09565-47aa-410c-a137-a3a6e6bfa8a8')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('c268a95f-e3d6-4414-981b-6c83c6447f5a')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('28f0d967-4110-4a8c-8426-2aeea4489111')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('15996a52-7166-4ac5-9d96-11a7d3592eec')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('d3de0128-f60b-4fd2-acc6-fa4735659a34')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('36306bbb-d12a-471d-af54-413c6b00c14e')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('52fd1967-2c5a-43e6-b7bd-977431424434')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('74ad3ad0-41e2-4919-a3dd-e5061c3444da')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('5c0a6150-502b-4d88-a46e-50b83768fe8f')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('ffae8d53-9870-4fdf-9247-02567f87f982')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('bd1bf883-c7d4-4f4d-857c-29e2470cb693')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('6cc0f7c2-0db6-432b-8189-fcedbcdda888')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('8e8b281f-a931-45c2-93e8-e350b0ed58b0')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('826aec63-3fa8-413d-9a40-d2d1ef262725')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('6e018caf-86c6-4740-b1db-d5a040430d2b')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('8e8b281f-a931-45c2-93e8-e350b0ed58b0')
# manga_download.all_chps(chp_ids)

# chp_ids = chp_id.get_list('8e8b281f-a931-45c2-93e8-e350b0ed58b0')
# manga_download.all_chps(chp_ids)


'''
some comics don't have volume, so manga_download could get 'volume': None
'''