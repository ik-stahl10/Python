import pandas as pd
fajl=pd.ExcelFile(r"C:\Users\Celikot\Desktop\G_kniga_blanko.xlsx")
niza=[]
for i in fajl.sheet_names:
    niza.append(fajl.parse(i))
    
df=pd.DataFrame(niza)
df.keys()

fajl2=pd.read_excel(r"C:\Users\Celikot\Desktop\G_kniga_blanko.xlsx")

pd.ExcelWriter("vezba.xlsx")