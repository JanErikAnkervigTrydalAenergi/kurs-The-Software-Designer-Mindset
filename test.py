#!/usr/bin/env python3
import os

print(os.getcwd())
# print all files in the current folder

for file in os.listdir():

    print(file)


def hi(name: int):
    print("name:", name)
