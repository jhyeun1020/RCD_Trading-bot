import ccxt
from datetime import datetime
import pandas as pd

binance = ccxt.binance() # ccxt 모듈에서 바이낸스 객체 생성
ohlc = binance.fetch_ohlcv('BTC/USDT') # 날짜, 시가, 고가, 저가, 종가, 거래량을 리스트로 가져옴
df = pd.DataFrame(ohlc) # 리스트로 가져온 ohlcv 정보를 데이터 프레임으로 전환
df.to_excel("BTC_USDT.xlsx") # 데이터 프레임 엑셀로 내보냄