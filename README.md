# Automatic file sorting program

This program automatically sorts files.
This use metafiles to decide where to go one file.
You only set a tag to each files. 

If this program finds out same file, it choices newly files.
Moreover, if it finds out same file and file has different create time, it saves each files.

----

## Usage

1. run **createIndex.py -f FILE_DIR**
2. add tags to metafile.json in FILE_DIR
3. run createIndex.py -f FILE_DIR to update manage file
4. run **AutomaticSort.py**
5. there are sorted files in folder that named "result"

## Attention

This program sort files with **first** metafile tag. 
So, When you add tags to metafile.json, you write tag in beggining of list.

To add same tag to files in same folder, you can use the option "-t" in createIndex.py. That is, run **createIndex.py -f FILE_DIR -t TAG**.

## want to initialize data

execute **check_sorted_index.py**.
This creates a new indexer.json from now sorted files in result folder.
