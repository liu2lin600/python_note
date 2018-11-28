

# 列表推导式，字典推导式，集合推导式

## 1. 列表推导式

print([x for x in range(0, 9)])
print([(x, y) for x in range(1, 3) for y in range(10, 13)])

list = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

### 普通写法
l2 = []
for l1 in list:
    for x in l1:
        if x % 3 == 0:
            l2.append(x)

print(l2)

### 列表推导式写法
print([x for l1 in list for x in l1 if x % 3 == 0])

### 判断数据类型
l3 = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in l3 if isinstance(x, str)])


## 2. 字典推导式

list4 = [('name', 'lili'), ('age', 22), ('weight', 110)]
print({k:v for k, v in list4})


for i in {'j':22, 'rr':33}.values():
    print(i)


## 3. 元组推导式

print({n for n in range(9) if n % 3 == 0})


## 元组没有推导式，它的结果是一个生成器对象