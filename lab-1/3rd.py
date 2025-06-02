# presenting data in tablular form
import pandas as pd
from tabulate import tabulate

A=[['Ram',10,'Dharan'],
   ['Hari',11,'Itahari'],
   ['Shyam',12,'Biratnagar']]

df=pd.DataFrame(A,columns=['Name','Age','Address'])
print(tabulate(df,headers='keys',tablefmt='grid'))