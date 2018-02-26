#!/usr/local/bin python

"""
Goal is to compare data structure : list and dict

- Create list with 10-15 names
- Create datasets with random numbers of entry of given list
- Store data in file
- Create function which will read data sets and stores counts in 
  list on the same index where that element exist
- Create function which will do same thing as above but using dict 

"""


import random
from time import time
from functools import wraps

countries = [ "India", "China", "Canada", "Netherlands", "Japan", "Russia", 
               "Nepal", "Ukraine", "America", "France", "Italy", "Bhutan", 
               "Austrelia", "Dubai", "Srilanka", "Germany", "Austin", "Hongkong" ]

data_sets_file = "/tmp/data.txt"


def timeit(f):
   @wraps(f)
   def wrapper(*args,**kwargs):
      start = time()
      result = f(*args,**kwargs)
      end = time()
      print "Elapsed time {0:.2} seconds".format(end-start)
      return result
   return wrapper

@timeit
def create_datasets():
    numbers_of_entries = 10000000
    f = open(data_sets_file,"w")
    for i in range(numbers_of_entries):
       f.write(random.choice(countries)+"\n")
    f.close()

@timeit
def read_datasets_list():
      countries_counts = [ 0 for country in countries ]
      with open(data_sets_file) as f:
         for line in f:
            line = line.strip()
            if line != "":
                 countries_counts[countries.index(line)] += 1
      print countries_counts
      
@timeit
def read_datasets_dict():
       countries_counts = dict((k,0) for k in countries)
       with open(data_sets_file) as f:
          for country in f:
             country = country.strip()
             if country != "":
                countries_counts[country] += 1
       print countries_counts

if __name__ == "__main__":
  create_datasets()
  read_datasets_list()
  read_datasets_dict()
