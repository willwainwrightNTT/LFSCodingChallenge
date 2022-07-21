# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Joshua Failla
# Created Date: 22 June 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Runs the test of the fwf_parser """ 
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import json
import os

from helpers import FwfParser, create_fwf_file

try:
    f = open('spec.json')
    data = json.load(f)
    f.close()
    spec_provided = True
except:
    print("No specification file was given please include a spec.json file in the directory")
    spec_provided = False

if spec_provided:
    column_names = data['ColumnNames']
    offsets = data['Offsets']
    columns = tuple(map(tuple, zip(column_names, list(map(int, offsets)))))
    
    # Test if the test file has been provided
    if not(os.path.exists('./fwf_lfs_test_file.txt')):
        create_fwf_file(offsets)
    fwf_parser = FwfParser(column_names,offsets)
    fwf_parser.fwf_parse('./fwf_lfs_test_file.txt')
    