import time
import pandas as pd
from selenium import webdriver

from sklearn import tree
import matplotlib.pyplot as plt

def grade(division):
    if division >= 60:
        return '  pass  1st'
    if division >= 50:
        return '  pass  2nd'
    if division >= 40:
        return '  pass  3rd'
    else:
        return '  fail     '
def readExcel():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)


    df = pd.read_csv('class.csv')
    rollno = df["rollno"]
    name = df["name"]
    chemistry = df["chemistry"]
    physics = df["physics"]
    math = df["math"]
    df["Total"]= chemistry+physics+math
    total=df["Total"]
    df['division']=(total/3)
    df['grade'] = df['division'].apply(grade)
    print(df)
    return name, chemistry, physics, rollno, math
name, chemistry, physics, rollno, math = readExcel()
