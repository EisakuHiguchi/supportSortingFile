# coding=utf-8
import time
from datetime import datetime
import os
import json
from argparse import ArgumentParser

FILE_DIRNAME = "../20180801"
FILE_METAFILE = "metafile.json"


def datetime_to_epoch(d):
    return int(time.mktime(d.timetuple()))

def epoch_to_datetime(epoch):
    return datetime(*time.localtime(epoch)[:6])

def get_dir_parents(filepath):
  parents = []
  temp = os.path.dirname(filepath)
  while not (temp is ""):
    parents.append(temp.split("/")[-1])
    temp = os.path.dirname(temp)
  return parents

def loadJson(filepath):
  try:
    if os.path.exists(filepath):
      f = open(filepath, "r", encoding="utf-8")
      temp = json.load(f)
      f.close()
      return temp
    else:
      return -1
  except:
    print("catch error")
    return -1

def savejson(filename, dict_data):
  f = open(filename,"w",encoding="utf-8")
  json.dump(dict_data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
  f.close()

def getNextCount():
  FILE_INDEXER = "indexer.json"
  dict_indexer = loadJson(FILE_INDEXER)
  if dict_indexer == -1:
    savejson(FILE_INDEXER, {})
    dict_indexer = {}
    return 1
  if len(dict_indexer.keys()) > 0:
    return len(dict_indexer.keys()) + 1
  return 1

    

"""
now = datetime.now()
# => 2012-10-10 21:12:17.544219

epoch = datetime_to_epoch(now)
# =>  1349871137
print(epoch)

epoch_to_datetime(epoch)
# => 2012-10-10 21:12:17
"""
def cheackMetadata(dict_temp,metadata):
  for key in metadata.keys():
    if metadata[key]["name"] is dict_temp["name"]:
      return False
  return True

def extracter(myfilepath):
  dict_temp = {}
  # create time (ephoch)
  dict_temp["create"] = os.path.getctime(myfilepath)
  # update time (ephoch)
  dict_temp["update"] = os.path.getmtime(myfilepath)
  # dict_temp["parents"] = get_dir_parents(myfilepath)
  dict_temp["parents"] = os.path.dirname(myfilepath)
  dict_temp["name"] = os.path.basename(myfilepath)
  dict_temp["tag"] = [os.path.basename(myfilepath)]
  dict_temp["ext"] = os.path.splitext(myfilepath)[-1]
  dict_temp["abspath"] = os.path.abspath(myfilepath)
  return dict_temp


def find_all_files(directory):
  for root, dirs, files in os.walk(directory):
    yield root
    for file in files:
      yield os.path.join(root, file)
"""
for file in find_all_files('/tmp/test'):
    print file
"""

def getMetafile(dirname):
  metadata = loadJson(dirname + "/metafile.json")
  FILE_DIRNAME = dirname
  dict_jsontemp = {}

  count = getNextCount()

  for myfilepath in find_all_files(dirname):
    #myfilepath = FILE_DIRNAME + "/" + e
    if os.path.isdir(myfilepath):
      continue
    dict_temp = extracter(myfilepath)

    if dict_temp["name"] in "metafile.json":
      print("metafile")
      continue
    elif metadata == -1:
      dict_jsontemp["file" + str(count)] = dict_temp
      count += 1
    else:
      if cheackMetadata(dict_temp,metadata):
        dict_jsontemp["file" + str(count)] = dict_temp
        count += 1

  f = open(FILE_DIRNAME + "/" + FILE_METAFILE, "w", encoding="utf-8")
  json.dump(dict_jsontemp, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
  f.close()

"""
def getMetafile(dirname):
  metadata = loadJson(dirname + "/metafile.json")
  FILE_DIRNAME = dirname
  list_files = os.listdir(FILE_DIRNAME)
  dict_jsontemp = {}

  count = getNextCount()
  for e in list_files:
    myfilepath = FILE_DIRNAME + "/" + e
    if os.path.isdir(myfilepath):
      continue
    dict_temp = {}
    # create time (ephoch)
    dict_temp["create"] = os.path.getctime(myfilepath)
    # update time (ephoch)
    dict_temp["update"] = os.path.getmtime(myfilepath)
    dict_temp["parents"] = get_dir_parents(myfilepath)
    dict_temp["name"] = os.path.basename(myfilepath)
    dict_temp["tag"] = [os.path.basename(myfilepath)]
    dict_temp["ext"] = os.path.splitext(myfilepath)[-1]
    dict_temp["abspath"] = os.path.abspath(myfilepath)

    if dict_temp["name"] in "metafile.json":
      print("metafile")
      continue
    elif metadata == -1:
      dict_jsontemp["file" + str(count)] = dict_temp
      count += 1
    else:
      if cheackMetadata(dict_temp,metadata):
        dict_jsontemp["file" + str(count)] = dict_temp
        count += 1

  f = open(FILE_DIRNAME + "/" + FILE_METAFILE, "w", encoding="utf-8")
  json.dump(dict_jsontemp, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
  f.close()
"""

if __name__ == "__main__":
  argparser = ArgumentParser()
  argparser.add_argument("-f", "--file", type=str, default="None")
  args = argparser.parse_args()

  if args.file is "None":
    print("error: require filename")
  else:
    getMetafile(args.file)
    
      


