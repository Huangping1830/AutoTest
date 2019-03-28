#coding:utf-8
import re
f = open("test.txt",'r')
str = f.read()
print str
reObj = re.compile('\b?(\w+)\b?')
word = reObj.findall(str)
print word
d = dict()
for w in word:
    if w.lower() in wordDict:
        d[word.lower()] += 1
    else:
        wordDict[word] = 1

s = '111'
dict()