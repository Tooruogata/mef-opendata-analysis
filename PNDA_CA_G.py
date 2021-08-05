# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:11:04 2021

@author: tooru
"""

import urllib.request
import zipfile
import pandas as pd
from datetime import datetime

startTime = datetime.now()
print('#########Inicio del Script###########')
print(datetime.now() - startTime)

###########################################################
# Definición de URL, Paths y Filenames
###########################################################

url = r'https://www.datosabiertos.gob.pe/sites/default/files/2021.zip'
path_dl = r'working directory'

path_dl_file    = path_dl + '\\' + '2021.zip'
path_csv_file   = path_dl + '\\' + '2021.csv'
path_xlsx_file  = path_dl + '\\' + '2021.xlsx'

###########################################################
# Descarga del PNDA
###########################################################
print('#Inicio de la descarga')
try: 
    urllib.request.urlretrieve(url, path_dl_file)
    print('#Fin de la descarga')

except:
    print('#Error en descarga, volver a intentar')

###########################################################
# Descomprimir ZIP
###########################################################

print('#Inicio de la extracción del zip')
zf=zipfile.ZipFile(path_dl_file, "r")
for i in zf.namelist():
    zf.extract(i, path=path_dl)
print('#Fin de la extracción del zip')

###########################################################
# Abrir CSV y Filtrar
###########################################################

df = pd.read_csv(path_csv_file, low_memory=False, nrows = 1000)
df.columns
#df = df.query('(TIPO_GOBIERNO == "M" & FUNCION == "20") | (TIPO_GOBIERNO == "R") | (TIPO_GOBIERNO == "E" & SECTOR == "11")')
df = df.query('(TIPO_GOBIERNO == "R")')

###########################################################
# GroupBy - Collapse - Agrupacion
###########################################################

df.MONTO_PIA = df.MONTO_PIA.apply(float)
df.MONTO_PIM = df.MONTO_PIM.apply(float)
df.MONTO_CERTIFICADO = df.MONTO_CERTIFICADO.apply(float)
df.MONTO_COMPROMETIDO_ANUAL = df.MONTO_COMPROMETIDO_ANUAL.apply(float)
df.MONTO_COMPROMETIDO = df.MONTO_COMPROMETIDO.apply(float)
df.MONTO_DEVENGADO = df.MONTO_DEVENGADO.apply(float)
df.MONTO_GIRADO = df.MONTO_GIRADO.apply(float)

df = df.groupby(['ANO_EJE',
            'TIPO_GOBIERNO'])[['MONTO_PIA',
                                        'MONTO_PIM',
                                        'MONTO_CERTIFICADO',
                                        'MONTO_COMPROMETIDO_ANUAL',
                                        'MONTO_COMPROMETIDO',
                                        'MONTO_DEVENGADO',
                                        'MONTO_GIRADO']].apply(sum).reset_index()
                                       
###########################################################
# Export a Excel
###########################################################

df.to_excel(path_xlsx_file, index = False)

print('#########Fin del Script###########')
print(datetime.now() - startTime)
