# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:38:32 2020

@author: Queenie
"""

questions = ['UAE', 'UK', 'Philippines', 'Belgium', 'Egypt', 'China']
answers = ['Abu Dhabi', 'london', 'Manila', 'Brussels', 'Cairo', 'Beijing']
correct = []
score = len(correct)
print("The Capital quiz")
name = input('What is your name: ')

def intro(name):
        print ("Hello ", name)
 

def rating(score):
    print("your score is ",score)
    if score == len(questions):
        print("Perfect! You're a walking atlas")
    elif score >= len(questions) * 0.7:
        print("Wow! You're quite great at geography")
    else:
        print("Tough luck, pal. Study more and you'll get there")


def quiz(questions, answers):
    i=0
    for question in questions:
        print("What is the capital of ",question,"?")
        your_ans = input('answer:')
    
        if your_ans.title() == answers[i].title():
            print("Correct!")
            correct.append('yes')
            i = i+1
        else:
            print("Wrong!")
            i = i+1
            
intro(name)
quiz(questions, answers)
score = len(correct) 
rating(score)
          
       
          
#question, why zero when declared at top


