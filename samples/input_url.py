# -*-coding:utf-8-*-
# input external file

file = open("URL.txt","r",encoding="UTF-8")
lines = file.readlines()
for line in lines:
    type(line)
    print(line)
    type(line)
    print("-----")
