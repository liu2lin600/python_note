import sys


f = open('file_example','r',encoding='utf-8')

for l in f:
    print(l)

f.close()