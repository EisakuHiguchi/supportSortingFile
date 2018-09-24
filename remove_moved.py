import os
from argparse import ArgumentParser


argparser = ArgumentParser()
argparser.add_argument("-f", "--file", type=str, default="None")
args = argparser.parse_args()

if not (args.file is "None"):
  list_dirpath = os.listdir(args.file)
  for e in list_dirpath:
    if os.path.isdir(e):
      list_e = os.listdir(e)
      if len(list_e) and (liste[0] is "metafile.json"):
        print("remove:" + e)
        os.removedirs(e)

      

