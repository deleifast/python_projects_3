import os, time, subprocess, shutil, os.path, sys, glob, glob2, configparser

my_file = open('lj01.verpdv_101.txt')
all_the_lines = my_file.readlines()
items = []
for i in all_the_lines:
    items.append(i.replace("\\n", ""))
print(items)

