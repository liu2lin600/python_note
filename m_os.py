import os
import sys

print(os.getcwd())                  # 当前目录
print(os.chdir('..'))               # 切换目录
# os.removedirs('/tmp/a')           # 删多个空目录
# os.remove('/tmp/a')               # 删单文件
# os.makedirs('/tmp/a/b')           # 创建多级目录
# os.mkdir('/tmp/b')                # 创建单目录
# os.rename(a,b)                    # 重命名
# os.listdir('/tmp')                # 列出指定目录下的目录和文件
print(os.stat('/tmp'))              #
print(os.name)                      # 当前系统平台
# os.system('ls')                   # 执行系统命令


print(os.path.dirname(__file__))    # 路径
print(os.path.basename(__file__))   # 文件名
print(os.path.split(__file__))      # 路径 + 文件名
print(os.path.splitext(__file__))   # 文件名 + 后续
print(os.path.abspath(__file__))    # 绝对路径
print(os.path.isdir(__file__))
print(os.path.isfile(__file__))
print(os.path.join('/tmp', 'abc'))  # 连接
print(os.path.exists('/tmp/sss'))

for a,b,c in os.walk('/tmp'):
    #print(a)
    #print(b)
    #print(c)
    pass

