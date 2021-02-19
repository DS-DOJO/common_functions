# -*- coding: utf-8 -*-
"""
@author: Rahul Pandey

Beginner Python Project: Hangman Game with Python
"""

import numpy as np
import pandas as pd
import random as rd

data = pd.read_csv("./data/BollywoodMovieDetail.csv")
data['count'] = data['title'].str.len()
play="Y"
enter_val = False
while(play == "Y"):
     play = input("Should we start the good old game of HANG THE MAN ??? [Y/N]")
     if(play.upper() == "Y" or play.upper() == "N"):         
         while(enter_val == False and play.upper() == "Y"):
             words = input("How many letter movie you want to guess between 2 and 59? [2-59]")
             try:
                 value = int(words)
                 enter_val == True
                 if (value >= 2 and value <= 59):
                     print("Good!!, You have 7 chances to guess the movie")
                     enter_val == True
                     play="N"
                     data_filter = data.loc[(data['count'] <= value)]
                     imdbid_list = data_filter.iloc[:,1].values.tolist()
                     rd.shuffle(imdbid_list)
                     movie_name = rd.sample(imdbid_list,1)
                     movie_df = data_filter.loc[(data_filter['title'] == movie_name[0])]
                     print("Movie was released in "+str(movie_df.iloc[:,2].values.tolist()[0]))
                     print("Movie genre is "+str(movie_df.iloc[:,4].values.tolist()[0]))
                     print("Actors in Movie "+str(movie_df.iloc[:,6].values.tolist()[0]))
                     print("Number of words in this movie is " + str(len(movie_name[0].split())))
                     list_word = movie_name[0].split()
                     astr = ""
                     list_movie_name = list(movie_name[0].upper())
                     data_movie = pd.DataFrame({"VALUE":list_movie_name})
                     for var in list_word:
                         astr = len(var)*'*'+" "+astr
                         #print(var)
                     print("YOU HAVE 5 CHANCES : GUESS THE MOVIE")    
                     print(astr)
                     astr_dataframe_list = list(astr)                     
                     count = 1
                     count_row = 1
                     while(count<=7):                         
                         val_str = input("Enter character:")
                         if (len(val_str)!=0):
                             if (len(val_str)==1):
                                 string_guessed = data_movie.loc[(data_movie['VALUE'] == val_str.upper())]
                                 if(string_guessed.shape[0] > 0):
                                     for index_val in string_guessed.index:
                                         astr_dataframe_list[index_val] = val_str.upper()
                                     astr_dataframe = pd.DataFrame({"VALUE":astr_dataframe_list})
                                     print("".join(astr_dataframe_list))
                                     count_astr = astr_dataframe.loc[(astr_dataframe['VALUE'] == "*")]
                                     count_row = count_astr.shape[0]
                                     if (count_row<1):
                                         print("You got it!!!!")
                                         break
                                 else:
                                     count = count+1
                                     print("WRONG!!! "+str(8-count)+" turns left")
                                 
                             else:
                                  count = count+1
                                  print("WRONG!!! "+str(8-count)+" turns left")                                                                          
                         else:
                             print("I do not understand your plan. Without entering how are you going to win?")
                     if(count>=7 and count_row>0):
                        print("You loose!!! Name of the movie was " + str(movie_name[0]))
                 else:
                     print("value should be between 2 and 59. Try Again!!!!")
                     enter_val == False
             except ValueError:
                 print("Are you serious? Enter numeric value. Try Again!!!!")
     else:
         play="Y"
