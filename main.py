#!/usr/bin/python

import sys
import pandas as pds
from pull import fetch
import numpy as np
from matplotlib import pyplot as plt
import time

if "-f" in sys.argv:
	fetch(refresh=True)
else:
	fetch(refresh=False)

df = pds.read_csv("India_series.csv")
delta = np.array(df["Cases"].diff().values, np.int32)
dates = list(df["Date"].values)

window = 30

plt.figure()
plt.title("New Cases w.r.t Date %d"%(df["Cases"].values[-1]))
plt.plot(list(range(window)), delta[-window:], "b*-")
plt.xticks(ticks=list(range(window))[::2], labels=[date[5:] for date in dates[-window::2]])
plt.annotate("%d cases!"%(delta[-1]), (window-1, delta[-1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()
