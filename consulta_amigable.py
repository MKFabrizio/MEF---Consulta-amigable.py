import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

E1=[]
E2=[]
E3=[]
E4=[]
E5=[]
E6=[]

anho=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
funcion=['20','15','22','18','10','03','19']
gob=['M','R']
dpto=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

for a in anho:
    for f in funcion:
        for g in gob:
            ab = "https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&1="
            url = ab+str(g)+"&8="+str(f)+"&5=&y="+str(a)+"&ap=Proyecto&cpage=1&psize=3000"
            r = requests.get(url)
            soup = BeautifulSoup(r.text,'lxml')
            htmltable_1 = soup.find('table', { 'class' : 'Data' })
            for element in np.arange(1,len(htmltable_1.find_all('td'))):
                if element%10==1:
                    A= str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                    E1.append(str(a))
                    E2.append(A[4:])
                    E3.append(str(g))
                    E4.append(str(f))
                if element%10==3:
                    Y=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                    E5.append(Y)
                if element%10==7:
                    Z=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                    E6.append(Z)
        
        ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&"
        url=ab+"8="+str(f)+"&5=&y="+str(a)+"&ap=Proyecto&cpage=1&psize=3000"
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        htmltable_1 = soup.find('table', { 'class' : 'Data' })
        for element in np.arange(1,len(htmltable_1.find_all('td'))):
            if element%10==1:
                A= str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                E1.append(str(a))
                E2.append(A[4:])
                E3.append("Total")
                E4.append(str(f))
            if element%10==3:
                Y=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                E5.append(Y)
            if element%10==7:
                Z=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
                E6.append(Z)
    
    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&"
    url=ab+"5=&y="+str(a)+"&ap=Proyecto&cpage=1&psize=3000"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    htmltable_1 = soup.find('table', { 'class' : 'Data' })
    for element in np.arange(1,len(htmltable_1.find_all('td'))):
        if element%10==1:
            A= str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
            E1.append(str(a))
            E2.append(A[4:])
            E3.append("Total")
            E4.append("Total")
        if element%10==3:
            Y=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
            E5.append(Y)
        if element%10==7:
            Z=str(htmltable_1.find_all('td')[element].text.strip("\r\n").strip())
            E6.append(Z)


df=pd.DataFrame(columns=['Año','Departamento','Gobierno','Funcion','PIM','Devengado'])
df["Año"]=E1
df["Departamento"]=E2
df["Gobierno"]=E3
df["Funcion"]=E4
df["PIM"]=E5
df["Devengado"]=E6

df.to_excel("Gasto_MEF_2021_a.xlsx",index=False)