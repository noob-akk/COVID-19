import json
import os

def fetch(refresh=True):
	if refresh:
		os.system('wget "https://pomber.github.io/covid19/timeseries.json" -O timeseries.json')
	data = json.load(open("./timeseries.json"))["India"]

	f = open("./India_series.csv", "w+")
	f.write("Date,Cases,Deaths,Recoveries\n")
	for day in data:
		f.write("%s,%s,%s,%s\n"%(day["date"], day["confirmed"], day["deaths"], day["recovered"]))
	f.close()
