import csv
import numpy as np
def getDataSource(data_path):
    Temperature = []
    sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Temperature.append(float(row["Temperature"]))
            sales.append(float(row["Ice-cream Sales"]))

    return{"x":Temperature,"y":sales}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correletion between temepature and ice cream sales : \n",correlation[0,1])
def setup():
    data_path = "Ice-Cream vs Cold-Drink.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()