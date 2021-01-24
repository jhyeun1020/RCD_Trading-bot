# 1. First day plan (2021/01/19)

![first plan](img/img.png)
![first plan](img/flowchart)
# "BTC_USDT.xlsx" 파일 읽는 방법
> * date -> 해당 행(OHLCV)의 기준이 되는 시간
> * open -> 코인의 시가
> * high -> 코인의 고가
> * low -> 코인의 저가
> * close -> 코인의 종가
> * volume -> 코인의 거래량
> * range -> 변동성 전략 기법을 사용하기 위한 range 값   
(이전 행의 고가에서 저가를 뺀 값에 변수 k를 곱한 값)   
@ 변수 k는 0~1 사이에서 변동할 수 있으며 "BTC_USDT.xlsx" 에서는 0.5를 사용
> * range_shift1 -> range 값을 계산의 편의를 위해 한 행 아래로 내린 값
> * target -> 목표 거래가로 시가에 range_shift1 값을 더한 값
> * ma5 -> 이동평균선을 추가적으로 지표로 사용하기 위한 값   
(이전 다섯 행의 종가의 평균 값)
> * bull -> 해당 행의 시가가 ma5 이상인지를 판단하기 위한 bool 값
> * ror -> 수익률
> * hpr -> 해당 행까지의 총 수익률
> * dd -> MDD(최대 누적 손실 값) 값
