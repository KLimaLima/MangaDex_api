import chapter

from CONSTANTS import *

# TODO: make log file to get data about url used and to check success or failure
# as of now hero killer and some other manga cannot response with image if using data-saver?
# could be 

# FIXME: solve issue where program is making too much request causing request to be blocked/rejected

'''
some comics don't have volume, so chapter could get 'volume': None
'''

hero_killer = '163306e6-1700-42a4-882f-26db124cbec2'

ol_vtuber_to_oshi_jk_chan = '6d216412-2453-451b-91b6-bedfcd9639d4'

Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life = '23aadc44-d2fe-46ca-83a6-6c86fd36ee12'

the_beginner_formerly_ranked_number_one_in_the_world = '7139b5c1-3740-4bf4-a157-2888af7f2420'

chp_ids = chapter.ids_get_filtered(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life)
chapter.all_chps(chp_ids, data_saver= False)
