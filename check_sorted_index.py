import os

import getMetafile


PATH_RESULT = "result"
list_dirpath = os.listdir(PATH_RESULT)

dict_indexer = {}
counter = 1

for e in list_dirpath:
  list_temp = os.listdir(PATH_RESULT + "/" + e)

  for ee in list_temp:
    myfilepath = PATH_RESULT + "/" + e + "/" + ee
    dict_temp = {}
    # create time (ephoch)
    dict_temp["create"] = os.path.getctime(myfilepath)
    # update time (ephoch)
    dict_temp["update"] = os.path.getmtime(myfilepath)
    dict_temp["parents"] = getMetafile.get_dir_parents(myfilepath)
    dict_temp["name"] = os.path.basename(myfilepath)
    dict_temp["tag"] = [e ,os.path.basename(myfilepath)]
    dict_temp["ext"] = os.path.splitext(myfilepath)[-1]
    dict_temp["abspath"] = os.path.abspath(myfilepath)

    dict_indexer["file" + str(counter)] = dict_temp
    counter += 1

getMetafile.savejson("indexer.json", dict_indexer)


