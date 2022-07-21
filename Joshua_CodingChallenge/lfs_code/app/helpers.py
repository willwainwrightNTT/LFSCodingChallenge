import csv
import struct
import sys
import string
from random import randint, choice

class FwfParser:
  """
    Parser class that can be used for any fixed-width-file implementation. The expectation
    is that the column_names and offsets are extracted separately into a list.
    Inputs:
      column_names: The headings for the resultant csv
      offsets: the fixed width of each column
  """
  def __init__(self,column_names: list, offsets: list):
    self.column_names = column_names
    self.offsets = offsets
  
  def fwf_parse(self,text_file_path, csv_file_path = './output/fwf_as_csv.csv'):
    """
      Function that creates the csv from a fixed width file using formatting
      structs. These structs are used to adhere to the offset structure for 
      each line. Structs are used as they are implemented in c and thus are 
      incredibly fast. This should scale to any length fixed width file.
      Inputs:
        column_names: The headings for the resultant csv
        offsets: the fixed width of each column
      Ouputs:
        fwf_as_csv.csv: csv of the fixed width file that was parsed.
    """
    string_format = ' '.join('{}{}'.format(abs(int(offset)), 'x' if int(offset) < 0 else 's')
                        for offset in self.offsets)
    text_struct = struct.Struct(string_format)
    unpack = text_struct.unpack_from
    parse = lambda line: tuple(s.decode() for s in unpack(line.encode()))
    with open(text_file_path, 'r') as text_file:
        lines = text_file.readlines()
    with open(csv_file_path, 'w', encoding='utf-8',newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(self.column_names)
        for line in lines:
          writer.writerow(parse(line))

def string_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(choice(chars) for _ in range(size))
         
def create_fwf_file(offsets):
   """
       If no fixed width file is defined then one is created.
       Randomly chooses 1 to 1000 lines and creates random
       strings to fill out the spec provided. A space is added
       in between each one to make it visually easier to understand
       the resultant csv.
   """
   x = randint(1, 1000)
   with open('./fwf_lfs_test_file.txt','w', encoding='utf-8') as f:
       for i in range(1,x):
           for offset in offsets:
               random_string = string_generator(int(offset)-1)
               random_string = random_string + ' '
               f.write(random_string)
           f.write('\n')