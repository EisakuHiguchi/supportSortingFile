import os
import shutil

import getMetafile
import copy

from datetime import datetime

dict_indexer = getMetafile.loadJson("indexer.json")

dict_dest = {}

for key in dict_indexer.keys():
  temp = dict_indexer[key]
  temp_name = temp["name"]
  if temp_name not in dict_dest:
    dict_dest[temp_name] = temp
    continue
  else:
    comp = dict_dest[temp_name]
    
    comp_create = comp["create"]
    temp_create = temp["create"]
    if comp_create == temp_create:  
      comp_uptime = comp["update"]
      temp_uptime = temp["update"]
      if comp_uptime < temp_uptime:
        dict_dest[temp_name] = temp
    else:
      counter = 1
      while (temp_name + ".a" + str(counter)) in dict_dest:
        counter += 1
      dict_dest[temp_name + ".a" + str(counter)] = temp

##

PATH_SORT_DIR = "result"
counter = 1
dict_save = {}

if not os.path.exists(PATH_SORT_DIR):
  os.mkdir(PATH_SORT_DIR)

for key in dict_dest.keys():
  temp = dict_dest[key]
  temp_tags = temp["tag"]
  temp_tag1 = temp_tags[0]
  temp_path_abs = temp["abspath"]

  if temp_tag1 is "REMOVE":
    os.remove(temp_path_abs)
  if temp_tag1 is "DONTMOVE":
    print("don't move:" + temp_path_abs)
  else:
    path_moveto = PATH_SORT_DIR + "/" + temp_tag1
    if not os.path.exists(path_moveto):
      os.mkdir(path_moveto)  
    if not os.path.exists(temp_path_abs):
      print("not exist: " + temp_path_abs)
    else:
      path_moveto_name = path_moveto + "/" + key
      shutil.move(temp_path_abs, path_moveto_name)
      temp["abspath"] = os.path.abspath(path_moveto_name)

      dict_save["file" + str(counter)] = temp
      counter += 1

# 

PATH_LOGDIR = "logs"
PATH_NEW_INDEXER = "indexer.json"
#nowtime = datetime.now().strftime("%Y%m%d_%H%M%S")
nowtime = ""

"""
if not os.path.exists(PATH_LOGDIR):
  os.mkdir(PATH_LOGDIR)

path_temp = PATH_LOGDIR + nowtime + "_" + PATH_NEW_INDEXER
getMetafile.savejson(path_temp, dict_save)
getMetafile.savejson(path_temp + ".copy", dict_indexer)

#os.remove("indexer.json")
"""

getMetafile.savejson(PATH_NEW_INDEXER, dict_save)
getMetafile.savejson(PATH_NEW_INDEXER + ".copy", dict_indexer)

