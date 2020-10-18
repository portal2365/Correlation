import plotly.express as px
import csv
import numpy as np


def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter (df,a="The Days They Were Present", b="Marks In Percentages")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["The Days They Were Present"]))
    
    return {"a" : marks_in_percentage, "b": days_present}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["a"], datasource["b"])
    print("Correlation between Marks in percent and The Days They Were Present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
