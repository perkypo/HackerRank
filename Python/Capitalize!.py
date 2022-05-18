"""
You are asked to ensure that the first and last names of people begin 
with a capital letter in their passports. For example, alison heck 
should be capitalised correctly as Alison Heck.

akhi eldho =>Akhi Eldho  

Given a full name, your task is to capitalize the name appropriately.
"""

name=input()
words=name.split()

for i in range(len(words)):
    letters = list(words[i])
    letters[0] = letters[0].upper()
    words[i] = ''.join(letters)
print(' '.join(words))