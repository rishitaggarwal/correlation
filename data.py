import csv
import numpy as np
def getDataSource(data_path):
    sizeOftv = []
    avgTimeSpent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeOftv.append(float(row["Size of TV"]))
            avgTimeSpent.append(float(row["	Average time spent watching TV in a week (hours)"]))

    return{"x":sizeOftv,"y":avgTimeSpent}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correletion between size of tv and average time spent wathcing tv : \n",correlation[0,1])
def setup():
    data_path = "./Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()