#read data and convert into data frame
import pandas as pd


with open("MLTathastuSampledata_Task1.csv", 'r') as f:
    with open("data_frame.csv", 'w') as f1:
        for line in f:
            f1.write(line.replace('\x00', ''))

df = pd.read_csv('data_frame.csv')
print(df)