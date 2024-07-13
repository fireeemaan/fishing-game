import pandas as pd
import os
import random as rd

# os.system("cls")

os.chdir('D:\Python Learn\Semester 2\[PROJECT] Fishing Game\database')
# print(6 * 0.5)
file = "fishList.csv"
df = pd.read_csv(file)
print(len(df.index))

namaIkan = input("Nama Ikan : ")
beratIkan = float(input("Berat Ikan (kg) : "))
exp = int(input("Poin Ikan : "))
value = exp / beratIkan




df.loc[len(df.index)] = [namaIkan, beratIkan, exp, value, rd.randint(2, 10)]

df.to_csv(file, index=False)



