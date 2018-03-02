#!/usr/bin/env python

"""
"Smart substring" 
Write a function that takes maximum 30 characters from a string but without cutting the words. 

Full description: 
"Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam." 

First 30 characters: 
"Featuring stylish rooms and mo" 

Smarter approach (max 30 characters, no words are broken): 
"Featuring stylish rooms and"
"""



def smart_substring(data):
   i = 0 
   result = []
   for ch in data:
      if i >= 26 and ch.strip() == '': 
          break
      result.append(ch)
      i+=1
   return ''.join(result)
 
     


print smart_substring("Featuring stylish rooms and moornings for recreation boats")
print smart_substring("Welcome to the linux world we are going to start learning")
print smart_substring("Breaking news, interchangeably termed late-breaking news and also known as a special report or special coverage or news bulletin, is a current issue that broadcasters feel warrants the interruption of")



      
