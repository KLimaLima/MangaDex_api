import manga.manga as manga
import util.response as response

Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life = '23aadc44-d2fe-46ca-83a6-6c86fd36ee12'

# manga_test = manga.Manga(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life, 'en')

# manga_test.update_manga_metadata()

# manga_test.create_chapters()

# my_room_dungeon_rest = '6e018caf-86c6-4740-b1db-d5a040430d2b'

lazy_dungeon_master = '0051e50a-e30c-4bb2-b378-c3da82463ee1'

akmkdsm = 'a04d4899-54c7-4f2e-a0a9-2338999ad6ac'

manga_test2 = manga.Manga(akmkdsm, 'en')

manga_test2.update_manga_metadata()

manga_test2.create_chapters_aggregate()

manga_test2.cbz_chp_all()

# manga_test.title = {'en': 'Bouken ni wa, Buki ga Hitsuyou da! ~Kodawari Rudy no Kajiya Gurashi~', 'ja': '冒険には、武器が必要だ！～こだわりルディの鍛冶屋ぐらし～'}

# manga_test.chapters_num = [1, 2, 3, 4, 5, 5.5, 6.1, 6.2]

# manga_test.zip_cbz_chp()

# print(util_response.dict_1_value_chooser(manga_test.title, manga_test.pref_lang))

# import chapter

# from CONSTANTS import *

# # TODO: make log file to get data about url used and to check success or failure
# # as of now hero killer and some other manga cannot response with image if using data-saver?
# # could be 

# # FIXME: solve issue where program is making too much request causing request to be blocked/rejected

# '''
# some comics don't have volume, so chapter could get 'volume': None
# '''

# hero_killer = '163306e6-1700-42a4-882f-26db124cbec2'

# ol_vtuber_to_oshi_jk_chan = '6d216412-2453-451b-91b6-bedfcd9639d4'

# Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life = '23aadc44-d2fe-46ca-83a6-6c86fd36ee12'

# the_beginner_formerly_ranked_number_one_in_the_world = '7139b5c1-3740-4bf4-a157-2888af7f2420'

# chp_ids = chapter.ids_get_filtered(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life)
# chapter.download_all(chp_ids, data_saver= False)

# # chp_ids = chapter.ids_get_filtered('a04d4899-54c7-4f2e-a0a9-2338999ad6ac')
# # chapter.all_chps(chp_ids, data_saver= False)

# # chp_ids = chapter.ids_get_filtered('0051e50a-e30c-4bb2-b378-c3da82463ee1')
# # chapter.all_chps(chp_ids, data_saver= False)

# # # chp_ids = chapter.ids_get_filtered('6d0d6cb1-1f5d-441f-957a-8e0268a6f913') # FIXME: bad filename
# # # chapter.all_chps(chp_ids, data_saver= False)

# # chp_ids = chapter.ids_get_filtered('e5f13b1a-eabd-4752-863a-cc3930a20d24')
# # chapter.all_chps(chp_ids, data_saver= False)

# # chp_ids = chapter.ids_get_filtered('e3d88382-a2c4-4958-8311-f8bd9a3f1e21')
# # chapter.all_chps(chp_ids, data_saver= False)

# # chp_ids = chapter.ids_get_filtered(Every_Adventure_Needs_Weapons_The_Meticulous_Rudys_Blacksmith_Life)
# # chapter.all_chps(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered(the_beginner_formerly_ranked_number_one_in_the_world)
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('a0f5d36b-3af9-412a-ae65-8973bad10245')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('0051e50a-e30c-4bb2-b378-c3da82463ee1')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('9a414441-bbad-43f1-a3a7-dc262ca790a3')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('1b72739a-7626-495e-a50d-fd1f52bc4397')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('0a4915d7-e84e-4d14-b7bf-c14a3a0995e0')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('f817d19e-e377-4fe3-b3e7-a334e80fb6f7')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('51b8571f-7277-4e48-b6e5-58c3ebca1143')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('7bf163e3-123a-41c1-b2bc-8254dbe5a09b') # FIXME: ????
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('c3911129-c183-402a-a415-cfd4a08aa746')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('bcf927d8-52e3-4d6f-a2da-4eb37abe91c9')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('7bd45a18-27d4-43ba-b3b9-2293f9a957d0')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('a3c09565-47aa-410c-a137-a3a6e6bfa8a8')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('c268a95f-e3d6-4414-981b-6c83c6447f5a')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('28f0d967-4110-4a8c-8426-2aeea4489111')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('15996a52-7166-4ac5-9d96-11a7d3592eec')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('d3de0128-f60b-4fd2-acc6-fa4735659a34')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('36306bbb-d12a-471d-af54-413c6b00c14e')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('52fd1967-2c5a-43e6-b7bd-977431424434')
# chapter.download_all(chp_ids, data_saver= False)

# # chp_ids = chp_id.ids_get_filtered('74ad3ad0-41e2-4919-a3dd-e5061c3444da') # FIXME: bad filename(must not include " in file name)
# # chapter.all_chps(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('5c0a6150-502b-4d88-a46e-50b83768fe8f')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('ffae8d53-9870-4fdf-9247-02567f87f982')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('bd1bf883-c7d4-4f4d-857c-29e2470cb693')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('6cc0f7c2-0db6-432b-8189-fcedbcdda888')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('8e8b281f-a931-45c2-93e8-e350b0ed58b0')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('826aec63-3fa8-413d-9a40-d2d1ef262725')
# chapter.download_all(chp_ids, data_saver= False)

# chp_ids = chapter.ids_get_filtered('6e018caf-86c6-4740-b1db-d5a040430d2b')
# chapter.download_all(chp_ids, data_saver= False)
