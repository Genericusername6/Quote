#!/usr/bin/env python
import random 
feeling = input("How are you feeling today?\n")

f = open("happyquotes")
text = f.read()
happyquotes = text.split("\n")
f.close()

with open("sadquotes") as f:
    text = f.read()
    sadquotes = text.split("\n")

if feeling.lower() == "happy":
    print(random.choice(happyquotes))
    f = open("puppygood")
    text = f.read()
    print(text)
    f.close()
    
elif feeling.lower() == "sad":
    print(random.choice(sadquotes))