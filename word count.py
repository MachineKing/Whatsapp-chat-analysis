
import re


input_file = open("phatic.txt", "r", encoding='utf-8')
lines = input_file.read().splitlines()
emoji_messages=0
media_count=0
total_emoji=0
total_emoticons=0
total_messages = len(lines)
word_count=0

emoticons=[':)', ':(', ':|', ":/", ';)']

for line in lines:
    if "<Media omitted>" not in line:   
        word_count=word_count+(len(line.split())-5)


print (total_messages)
print (word_count/total_messages)
