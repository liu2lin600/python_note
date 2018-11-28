import random

print(random.random())              # [0,1)
print(random.randint(1, 3))         # [1,3]
print(random.randrange(1, 9, 2))    # [1,3,5,7,9] 中取一值
print(random.choice([11, 22, 33]))  # 取一个值
print(random.uniform(1, 9))         # 1-9随机符点数

l1 = [1, 2, 3, 4, 5, 6 ]
print(random.sample(l1,3))          # 取指定长度
random.shuffle(l1)                  # 修改原值
print(l1)