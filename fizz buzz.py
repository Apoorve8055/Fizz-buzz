# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:19:58 2018

@author: APOORVE
"""
def fizzbuzz(): 
    for i in range(1,50):
        if i%3==0 and i%5==0 :
            print("fizz buzz",i)
        elif i%5==0:
            print("buzz",i)
        elif i%3==0:
            print("fizz",i)
        else:
            print(i)
        
fizzbuzz()