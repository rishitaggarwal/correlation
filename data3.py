import csv
import numpy as np
def getDataSource(data_path):
    marks = []
    dp = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            dp.append(float(row["Days Present"]))

    return{"x":marks,"y":dp}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correletion between marks and days present : \n",correlation[0,1])
def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()