from compareFiles import CompareFiles

folderMain = r'C:\Users\Александр\PycharmProjects\compareFiles\main'
folderNew = r'C:\Users\Александр\PycharmProjects\compareFiles\new'
folderCheck = r'C:\Users\Александр\Desktop\Фото new'
comp = CompareFiles(folderMain, folderNew)

# comp.hash_folder_main()
# comp.check_folder_new()
# print(comp.hash_main)
#print(comp.dublicate_files)
# for file in comp.dublicate_files:
#     print(file)
#comp.remove_dublicate_files()

comp.find_dublicate_in_folder(folderNew)
for key in comp.dict_files:
    if len(comp.dict_files.get(key, [])) > 1:
        print(comp.dict_files.get(key, []))
comp.remove_dublicate_in_folder()
print('Done')