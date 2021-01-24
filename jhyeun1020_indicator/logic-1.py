import ccxt
from datetime import datetime
import pandas as pd

binance = ccxt.binance() # ccxt 모듈에서 바이낸스 객체 생성
ohlc = binance.fetch_ohlcv('BTC/USDT') # 날짜, 시가, 고가, 저가, 종가, 거래량을 리스트로 가져옴
for i in ohlc: # 모든 날짜 데이터를 데이트타임 타입에서 읽기 쉬운 타입으로 변경
    i[0] = datetime.fromtimestamp(i[0]/1000).strftime('%Y-%m-%d %H:%M:%S')
 # 리스트로 가져온 ohlcv 정보를 데이터 프레임으로 전환
 # 데이터프레임의 각 열을 읽기 쉽게 인덱싱
df = pd.DataFrame(ohlc,columns=['date','open','high','low','close','volume'])
# 변동성 돌파 전략을 위한 range 열을 데이터프레임에 추가
df['range'] = (df['high']-df['low']) * 0.5
# range 변수를 보기 쉽게 한칸 내림
df['range_shift1'] = df['range'].shift(1)
# 변동성 돌파 전략 목표가를 계산하기 위해 shift() 메서드를 사용하여 현재 싯가에 전날의 range 값을 더함
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel('BTC_USDT.xlsx')
