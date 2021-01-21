import os
import random
from random import randint
import matplotlib.pyplot as plt

# 시작 돈
money = 100000

walk = []

# 시작점
start = 0

# 변화량
pos = 100

# 주식 시작점
dall = 10000

def app(position):
    for i in range(100):
        
        if random.randint(0,1):
            step = randint(0,300) # 변화량
        else:
            step = randint(-300,0)
        
        if position > 0:
            position += step
        
        walk.append(position)

    return position

def pri(steps,start):
    x = range(steps)
    plt.title("SamSung JuGa")
    plt.plot(x,walk[start:start+100])
    plt.show()

dall = app(dall)
count = 1

while(money > 0):
    pri(100,start)
    print("{}회차 구매".format(count))
    print("현재 남은 돈: {}".format(money))
    print("현재 주가: {}".format(dall))

    before = dall
    poss = money/dall
    possible = int(poss)

    print("최대 구매 가능 주: {}".format(possible))

    buy = int(input("몇 주를 구매하시겠습니까: "))
    money = money - dall*buy
    gumae = dall*buy
    dall = app(dall)
    start = start + 100
    money = money + dall*buy
    panme = dall*buy
    count = count + 1
    after = dall

    print("주가 변동 {} -> {}".format(before,after))
    print("손익: {}".format(panme-gumae))
    print("\n")

print("탕진했습니다.")