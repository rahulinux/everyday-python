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
   result = ""
   for word in data.split():
      if (len(result) + len(word)) > 30: 
          return result
      result = (result + " " + word).strip()
   return result
 
     
def smart_substring_2(text):
   number = 30
   text_arr = text.split(" ")
   final_string = ""
   for text_val in text_arr:
   	if (len(text_val) + len(final_string)) > number:
   		return final_string
   	final_string = (final_string + " " + text_val).strip()
   return final_string

print smart_substring("Featuring stylish rooms and moornings for recreation boats")
print smart_substring_2("Featuring stylish rooms and moornings for recreation boats")
print smart_substring_2("Welcome to the linux world we are going to start learning")
print smart_substring_2("Breaking news, interchangeably termed late-breaking news and also known as a special report or special coverage or news bulletin, is a current issue that broadcasters feel warrants the interruption of")



      
