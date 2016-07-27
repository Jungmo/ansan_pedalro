# [안산 페달로](http://www.pedalro.kr/station/station.do?method=stationState&menuIdx=st_01)

안산시 공공자전거 페달로 정거장 현황을 가지고와서 csv파일로 저장합니다.


## 파라미터

* interval - 몇 초에 한번씩 긁어올지.. 처리에 필요한 시간이 있어서 적어도 10초 이상 해줘야 합니다.

```
$ python main.py --interval 20
```
위 예는 20초에 한번씩 긁어옵니다.
