import csv
import numpy as np
def getDataSource(data_path):
    coffe = []
    hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffe.append(float(row["Coffee in ml"]))
            hours.append(float(row["sleep in hours"]))

    return{"x":coffe,"y":hours}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correletion between coffe and sleep : \n",correlation[0,1])
def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()