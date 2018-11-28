

## int 数字

print('1==>: ', 23 + 34 - 78 * 2 / 3)
print('2==>: ', 12 // 5, 9 % 4)
a, b = divmod(9, 7)
print(a, b)
print(int('88'), float(99))


## string 字符串
aa = 'abcdefghijklmn'
bb = 'aaa_bbb_ccc_ddd'
cc = 'nIce TO meet YoU'
print(type(str(333)), 'aaa\naaa', 'bbb\tbbb', 'cc\"cc', 'ddd' + 'eee', 'abc' * 3)
print(aa[3], aa[-2], aa[:], aa[-3:], aa[:5], aa[3:6], aa[4::3], aa[::-1])
print(bb.split('_'))
print('=='.join(bb.split('_')))
print(len(aa), aa.startswith('a'), aa.endswith('d'), aa.find('fg'), bb.count('_'), bb.isalnum())
print(cc.upper(), cc.lower(), cc.title(), cc.swapcase())
print('居中：' + cc.center(30))
print('左对齐：' + cc.ljust(30))
print('右对齐：' + cc.rjust(30))

print(bb.replace('_', '^^', 2))

print(type({1,2}))


## list 列表，有序，可变

l1 = ['aa', 'bb', 'cc', 'dd', ['ball', 'light', 'zero'], ]
l2 = [11, 22, 33]
l3 = ['Tom', 'Mei', 'You']
print(l1[:], l1[::2], l1[::-1])
print('+: ', l1 + l2)

l1.append(l2)
print('append: ', l1)

l2.extend(l1)
print('extend: ', l2)

l2.insert(2, 'fff')
print(l2)

l4 = '##'.join(l3)
print(l4)

'''del, remove(), pop(), index(), in, count(), sort(), len(), '''

## tuple 元组，有序，不可变

t1 = 'a',
t2 = ('aa', 'bb', 'cc')
a,b,c = t2

print(a, b, c)


## dict 字典，无序，可变 get() keys() values() items()

d1 = {}
d2 = {
    'name': 'lilei',
    'age': 33
}
d3 = {
    'aa': 222,
    'bb': 555
}

print(d3.get('aa'))
print(d3.keys())
print(d3.values())

d2['age'] = 35
print(d2['age'])

d2.update(d3)
print(d2)

del d2['bb']
print(d2)

# d2.clear()

# d2.values(), d2.items()
print(list(d2.keys()))

## set 集合，无序，不重复

s1 = set()
s2 = {1, 2, 3, 5}










