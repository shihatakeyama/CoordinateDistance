import numpy as np

'''
原点(0,0)と各座標を結ぶ線分の長さを平方根で表示します。

出力結果の見方。左上が原点(0,0) 右方向がx、下方向がy
・(0,0)と(0,2)間の距離はsqrt(4)
・(0,0)と(3,1)間の距離はsqrt(10)

[0, 1, 4, 9, 16, 25,：：：
[1, 2, 5, 10, 17, 26,：：：
：：：

'''

def diag(x, y):
    suba = np.abs(x - y)
    return (suba * suba) + (x * y) * 2


for i in range(20):
    line = []
    for j in range(40):
        line.append(diag(j,i))
    print (line )


