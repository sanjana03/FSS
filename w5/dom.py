import rows as R
import math
from random import random
from test import O

def dom(dataset, row1, row2):
    s1, s2, n= 0, 0, 0
    for c, w in dataset.w.items():
        a0 = round(float(row1[c]),2)
        b0 = round(float(row2[c]),2)
        a = R.numNorm(dataset.nums[c], a0)
        b = R.numNorm(dataset.nums[c], b0)
        s1 = s1 - math.pow (10,(w * (a - b) / n))
        s2 = s2 - math.pow (10,(w * (b - a) / n))
    return (s1 / n) < (s2 / n)


def doms(dataset):
    n = 100
    name = "WeatherLong"
    c = len(name)
    name = name + ",>dom"
    for r1 in range(len(dataset.rows)):
        row1 = dataset.rows[r1]
        row1.append(0)
        for s in range(1,n):
            row2 = another(r1, dataset.rows)
            s = dom(t, row1, row2) and 1/n or 0
            row1[c] = row1[c] + s 
    return dataset.rows


def another(row_i, rows):
    value = math.floor(0.5 + random() * len(rows))-1
    rows_max = max(0, value)
    if row_i == rows_max:
        return another(row_i, rows)
    else:
        return rows[rows_max]


def weatherLong():
    global dataset
    dataset = R.rows("weatherLong.csv")
    res = doms(dataset)
    headers, rows = res[0], res[1]
    print("\t".join(headers))

    for row in rows:
        content = ""
        for cell in row:
            content += f'{cell}\t\t'
        print(content)


@O.k
def test1():
    weatherLong()
