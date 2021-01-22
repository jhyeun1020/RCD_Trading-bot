from random import randint
import time

def app(position):
    a = 300
    b = -300
    if randint(0,1):
        step = randint(0,a) # 변화량
        a -= 5
        b = 300
    else:
        step = randint(b,0)
        b += 5
        a= 300
    
    if position > 0:
        position += step
    
    walk.append(position)
    return position

def gap(a,b):
    if a > b:
        return -(a-b)
    elif a < b:
        return b-a
    else:
        return 0

for _ in range(100):

    # 기본 설정
    money = 100000 # 기초 자산
    walk = []
    start = 0
    pos = 0
    dall = 10000 # 시작 주가
    count = 1 # 회차
    last = 11000 # 어제자 평균치
    dall = app(dall)

    while(money > 0 or money < 200000):
        time.sleep(0.5)
        before = dall
        dall = app(dall)
        after = dall
        delta = gap(before,after)
        print("현재 주가 : ",dall)

        if last > dall and delta > 0:
            buy = int(money/dall)//2
            money = money - dall*buy
            now = dall
            output_limit = now*(1.11)
            print("* 구매 가격 : ",now)

            while 1:
                time.sleep(0.5)
                before = dall
                dall = app(dall)
                after = dall
                delta = gap(before,after)
                print("현재 주가 : ",dall)

                if output_limit < dall and delta < 0:
                    money = money + int((dall*buy)*(0.99))
                    count += 1
                    last = (now+last)//2
                    print("* 판매 가격 : ",dall)
                    print("* 남은 돈: ",money)
                    break