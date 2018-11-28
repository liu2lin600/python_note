import re

# 元字符： ^ $ . * + ? [] {} () \ |
#
# 个数 +=>{1,}; ?=>{0,1}; *=>{0,}; {2}; {1,8};
# 范围 [a-Z] [0-9] [^name]=>非
# \d=>[0-9] \D=>[^0-9] \s=>[\t\n\r\f\v] \S \w=>[a-Z0-9_] \W \b=>空格, &, #

res = re.findall('[a-z].\d+', 'fsdfsd34fgdfg56kjhkgh78gbfg')
re1 = re.findall('abc*', 'abcccc')
re2 = re.findall('abc*?', 'abcccc')
re3 = re.findall('\(\d\-\d\)', '43+43*3-5*(3-1)')

re4 = re.findall('ab|c', 'acbbabc')
re5 = re.findall('a[b|c] ', 'abccacb')

re9 = re.findall('(?:ab)+', 'abababab')                 # 如果没的 ?: 的话，只会匹配出来 ab

re6 = re.search('\d+', 'fsd98fswer34jkl8lkj').group()   # 从字符开始处匹配

re7 = re.sub('\d+', "AA", 'hhhh4pppp48rrrr89ttt', 2)    # 匹配替换，可指定个数

com = re.compile('\d+')         # 如果多次用一个规则，可以先把规则编译
com.findall('fsdf6fds7fds')
com.findall('dd8gg0uu9ee')

print(res)
print(re1)
print(re2)
print(re3)
print(re4)
print(re5)
print(re6)
print(re7)
print(re9)