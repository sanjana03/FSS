from test import O
from dom import mainDom
from unsuper import main
import re, sys, random, math


@O.k
def testDom():
    print("\nweatherLong.csv\n")
    mainDom("weatherLong.csv")

    print("\nauto.csv\n")
    mainDom("auto.csv")

    print("\nweatherLong.csv\n")
    main('weatherLong.csv')
