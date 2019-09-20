# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:36:55 2019

@author: lydia
"""

#==========================================
# Purpose:
#   Returns the sound a dog is likely to make given the dog's weight
# Input Parameter(s):
#   weight - the weight of a given dog, rounded to the nearest pound
# Return Value(s):
#   A string representing what the dog’s bark would probably sound like
#==========================================

def sound(weight):
    if weight < 13:
        return 'Yip'
    elif weight <= 30:
        return 'Ruff'
    elif weight <= 70:
        return 'Bark'
    else:
        return 'Boof'
    
    
#==========================================
# Purpose:
#   To create a simple Interactive Fiction game
# Input Parameter(s):
#   text - a string representing the prompt for a choice in a text 
#          adventure game
#   option1 - a string representing option 1
#   option2 - a string representing option 2
#   option3 - a string representing option 3        
# Return Value(s):
#   The string ('1', '2', or '3') that represents the user’s choice        
#==========================================    
        
def choice(text,option1,option2,option3):
    print(text)
    print('1.', option1)
    print('2.', option2)
    print('3.', option3)
    decision = input("Choose 1, 2, or 3: ")
    while decision != '1' and decision != '2' and decision != '3':
        print("Invalid option")
        decision = input("Choose 1, 2, or 3: ")
    return decision
    

#==========================================
# Purpose:
#   An Interactive Fiction game, which gives the user a sequence of choices, 
#   leading to one of several endings.
# Input Parameter(s):
#   None       
# Return Value(s):
#   The boolean value True if the story ending is good. False if it is bad.         
#========================================== 

def adventure ():
    diamond2 = 0
    diamond3 = 0
    diamond4 = 0
    diamond5 = 0
    diamond1 = choice("You were offered a job at a cool start-up.",\
                      "Vow never to work again.","Accept the offer.",\
                      "Pursue your PhD instead.")
    if diamond1 == '1':
        print("You run out of money and move back in with your parents.")
        return False
    if diamond1 == '2':
        diamond2 = choice("Work at the start-up is challenging.",\
                          "Buy a lottery ticket and hope for the best",\
                          "Maintain a positive attitude and stick with it",\
                          "Start your own company instead.")
    if diamond1 == '3':
        diamond3 = choice("You got your PhD. Congrats. Now what?",\
                          "Vow never to work again.",\
                          "Start your own company.","Become a professor.")
    if diamond2 == '1':
        print("It worked. You won the lottery!")
        return True
    if diamond2 == '2':
        print("The start-up failed so you start your own company instead.")
        diamond4 = choice("Business is good. You have the opportunity to sell.",\
                          "Sell your company and retire early",\
                          "Sell your company to pursue your dream of teaching",\
                          "Never! Buy out the competition instead.")
    if diamond3 == '1':
        print("You run out of money and move back in with your parents.")
        return False
    if diamond2 == '3' or diamond3 == '2':
        diamond4 = choice("Business is good. You have the opportunity to sell.",\
                          "Sell your company and retire early",\
                          "Sell your company to pursue your dream of teaching",\
                          "Never! Buy out the competition instead.")
    if diamond4 == '1':
        print("Sit back and enjoy the good life.")
        return True
    if diamond4 == '3':
        print("You've become a greedy workaholic. Too bad.")
        return False
    if diamond3 == '3' or diamond4 == '2':
        diamond5 = choice("What is your teaching philosophy?",\
                          "Tough but fair.","Easy. Give everyone a B.",\
                          "Do everything you can to help your students.")
    if diamond5 == '2':
        print("Unfortunately, the administration does not agree.")
        return False
    else:
        print("Enjoy a long and happy career.")
        return True 