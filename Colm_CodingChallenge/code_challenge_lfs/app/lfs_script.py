#----------------------------------------------------------------------------
# Created By  : Colm Stringer
# Created Date: 14 July 2022
# version ='1.0'
# ---------------------------------------------------------------------------

# COMMAND ----------

#Imports
import pandas as pd
from faker import Faker

# COMMAND ----------

# Filepath is the path in which the generated csv will be stored. This function generates a small csv file containing first, last name, address and date of birth for two individuals. 
def generate_csv(filepath):
  data = {"first_name": ['Jacob', 'Abe'],
          "last_name": ['Smith', 'McDonald'],
          "address": ['5 Mountain Rd Seaford, VIC, 3867', '5 Golden Rd Chadstone, VIC, 3148'],
          "date_of_birth": ['15/06/1980', '24/05/1994']}
  df = pd.DataFrame(data)
  df.to_csv(filepath,index=False)
  return df

# COMMAND ----------

#Test if function works
try:
  generate_csv('data/data.csv')
except:
  print("Error. Failed to generate Sample DataFrame")

# COMMAND ----------

# Input_path is the filepath you passed when generating the csv. Output_path is the filepath where the anonymised data will be stored.
# This function takes our original data and make first, last name and address randomly anonymised by iterating through each row. Ensuring robustness regardless of the data being inputted.
def anonymise(input_path,output_path):
  fake = Faker('en_AU')
  df = pd.read_csv(input_path)
  i = list(df.index)
  for x in i:
    df['first_name'][x] = fake.first_name()
    df['last_name'][x] = fake.last_name()
    df['address'][x] = fake.address()
  df.to_csv(output_path,index=False)
  return df

# COMMAND ----------

#Test if function works
try:
  anonymise('data/data.csv', 'data/anonymised.csv')
except:
  print("Error. Failed to generate anonymised csv")

# COMMAND ----------

print("Script ran successfully")
