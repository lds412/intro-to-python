# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:23:00 2019

@author: lydia
"""

#==========================================
# Purpose: 
#   Identifies the first word of every sentence in a file
# Input Parameter(s): 
#   fname is a string representing the name of a file
# Return Value(s): 
#   A list of the first word in every sentence in that file, 
#   in order, including duplicates.
#==========================================

def first_words(fname):
    fp = open(fname)
    first=[]
    for row in fp:
        line=row.split(' ')
        first.append(line[0])
    fp.close()
    return first

#==========================================
# Purpose: 
#   Keeps track of every word in a file and which words follow it
# Input Parameter(s): 
#   fname is a string representing the name of a file
# Return Value(s): 
#   A dictionary where the keys are each word in the file, 
#   and the value is a list of every word that follows that key 
#   in the file, in order, including duplicates. 
#==========================================

def next_words(fname):
    fp = open(fname)
    words={}
    for row in fp:
        row = row.strip()
        line = row.split(' ')
        for i in range(len(line)-1):
            if line[i] in words:
                words[line[i]] += [line[i+1]]
            else:    
                words[line[i]] = [line[i+1]]
    fp.close()
    return words

#==========================================
# Purpose: 
#   Takes in a file and prints 10 ‘sentences’ based on that file
# Input Parameter(s): 
#   fname is a string representing the name of a file
# Return Value(s): 
#   None 
#==========================================

import random
    
def fanfic(fname):
    words=next_words(fname)
    for i in range(10):
        word=random.choice(first_words(fname))
        string=word
        while word != '.': 
            options = words[word] 
            word = random.choice(options)
            string += ' ' + word
        print(string)    
    return

#==========================================
# Purpose: 
#   Calculates the total memory in bytes being used by txt files in a directory    
# Input Parameter(s):
#   directory is a nested dictionary representing a directory    
# Return Value(s): 
#   The total memory in bytes being used by txt files in the directory    
#==========================================

def total_txt_size(directory):
    total = 0
    for key in directory:
        if type(directory[key]) == dict:
            total += total_txt_size(directory[key])
        elif '.txt' in key:
            total += directory[key]
    return total
