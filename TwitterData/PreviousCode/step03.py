import sys
import twint
import pandas as pd
import time
import os

file2=str(sys.argv[1])
with open (file2) as f:
    countries=f.readlines()

countries=[line.rstrip('\n') for line in countries]
print(countries)

for country in countries:
    folder=country
    fileClean=folder+'/candidatos_'+folder+'_Clean'
    with open(fileClean) as f:
        candidatos=f.readlines()
        candidatos=[line.rstrip('\n') for line in candidatos]
        for i in candidatos:
            username=i
            path=folder+"/"+username+".txt"
            if os.path.isfile(path):
               print("file_ready")
            else:
               c = twint.Config()
               c.Username = username
               #c.Limit = 100
               c.Stats = True
               c.Output = path
               twint.run.Search(c)
               time.sleep(1)
