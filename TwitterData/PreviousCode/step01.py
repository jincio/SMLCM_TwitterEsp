import pandas as pd
import sys
import numpy
import os

file2=str(sys.argv[1])  # first argument is the file 'datacandidatos'
file = pd.ExcelFile(file2)
Candidatos = pd.read_excel(file, 'Data')
paises=Candidatos.Country.unique()
numpy.savetxt("CountryList.txt", paises, delimiter=",",fmt='%s')
print(paises)

# Creating directories
for i in paises: 
    path="./"+i
    if (os.path.exists(path)==False):
        os.makedirs(path)
    else: 
        print("Country included")

# Creating files within directories

Test=Candidatos.loc[:,("Country","Candidate","Twiterhandle")]
Test["Twiterhandle"]=Test["Twiterhandle"].str.replace('@','')
Test["Twitterhande"]=Test["Twiterhandle"].str.replace(' ','')
Test=Test.drop_duplicates()
for i in paises:
    subset=Test[Test["Country"]==i]
    name="./"+i+"/"+"candidatos_"+i
    subset.to_csv(name)