import os
import json
from argparse import ArgumentParser

import getMetafile

def init_indexer():
  global counter
  dict_indexer = getMetafile.loadJson(FILE_INDEXER)
  if dict_indexer == -1:
    getMetafile.savejson(FILE_INDEXER,{})
    dict_indexer = {}
  counter = 1
  if len(dict_indexer.keys()) > 0:
    counter = len(dict_indexer.keys()) + 1
  return dict_indexer

def updateIndexer(filepath):
  global counter
  dict_meta = getMetafile.loadJson(filepath)
  if dict_meta != -1:
    for key in dict_meta.keys():
      dict_indexer[key] = dict_meta[key]
      counter += 1
    getMetafile.savejson(FILE_INDEXER,dict_indexer)
  else:
    print("update error")


def main(filename):
  global FILE_DIRNAME
  global dict_indexer
  FILE_DIRNAME = filename
  filepath = FILE_DIRNAME + "/metafile.json"
  print("now initializing...")
  dict_indexer = init_indexer()
  if not os.path.exists(FILE_DIRNAME + "/metafile.json"):
    print("create new metafile")
    getMetafile.getMetafile(FILE_DIRNAME)
  print("updating...")
  updateIndexer(filepath)

def addTag(filename, tag):
  global FILE_DIRNAME
  global dict_indexer
  FILE_DIRNAME = filename
  filepath = FILE_DIRNAME + "/metafile.json"
  print("now initializing...")
  dict_indexer = init_indexer()

  dict_meta = getMetafile.loadJson(filepath)
  for key in dict_meta.keys():
    temp = dict_meta[key]
    taglist = temp["tag"]
    if "," in tag:
      splitted = tag.split(",")
      for t in splitted:
        taglist.insert(0, t)
    else:
      taglist.insert(0, tag)
  getMetafile.savejson(filepath, dict_meta)
  print("updating...")
  updateIndexer(filepath)

def taggingbyId(jsondata, id, add_tag):
  data = jsondata["file" + id]
  tag = data["tag"]
  
  if "," in add_tag:
    list_tag = add_tag.split(",")
    for e in list_tag:
      tag.insert(-2, e)
  else:
    tag.insert(-2, add_tag)
  
def addTag_range(filepath, range):
  global FILE_DIRNAME
  global dict_indexer

  r1 = int(range[0])
  r2 = int(range[1])
  print("range: " + str(r1) + " to " + str(r2))

  FILE_DIRNAME = filename
  filepath = FILE_DIRNAME + "/metafile.json"
  print("now initializing...")
  dict_indexer = init_indexer()

  dict_meta = getMetafile.loadJson(filepath)
  for i in range(r1,r2):
    dict_meta = taggingbyId(dict_meta, i, args.tag)

  getMetafile.savejson(filepath, dict_meta)
  print("updating...")
  updateIndexer(filepath)


## 
FILE_DIRNAME = ""
filepath = FILE_DIRNAME + "/metafile.json"

FILE_INDEXER = "indexer.json"
counter = 1

if __name__ == "__main__":
  argparser = ArgumentParser()
  argparser.add_argument("-f", "--file", type=str, default="None")
  argparser.add_argument("-t", "--tag", type=str, default="None")
  argparser.add_argument("-r", "--range", type=str, default="None")
  args = argparser.parse_args()

  if args.file is "None":
    print("error: require filename")
  elif not (args.tag is "None"):
    print("add same tag")
    addTag(args.file, args.tag)
    if not (args.range is "None"):
      range = args.range.split(",")
      if len(range) == 2:
        addTag_range(args.filepath, range)
  else:
    main(args.file)
