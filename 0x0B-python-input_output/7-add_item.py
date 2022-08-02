#!/usr/bin/python3
""" a script that saves argv via json to file """
import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
try:
    my_list = load_from_json_file(file)
except:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, file)