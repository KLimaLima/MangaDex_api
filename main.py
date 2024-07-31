import manga_download
import chp_id
# import manga_search
# import susun

from CONSTANTS import *

hero_killer = '163306e6-1700-42a4-882f-26db124cbec2'

ol_vtuber_to_oshi_jk_chan = '6d216412-2453-451b-91b6-bedfcd9639d4'

Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life = '23aadc44-d2fe-46ca-83a6-6c86fd36ee12'

chp_ids = chp_id.get_list(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life)

manga_download.batch_chps(chp_ids)