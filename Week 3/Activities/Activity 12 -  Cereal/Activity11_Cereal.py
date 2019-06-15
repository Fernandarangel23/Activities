import csv
import os 

cereal_csv = os.path.join("cereal.csv")

with open(cereal_csv, 'r', newline='') as cerealFile:
    d_reader = csv.DictReader(cerealFile)
    headers = d_reader.fieldnames
    cerealDF = csv.reader(cerealFile, delimiter=',')
    next(cerealDF, None) #Skip headers
    print(headers)
    for i in cerealDF:
        if i[7] > str(4):
            print(i)