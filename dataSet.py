import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import numpy as np

import matplotlib.pyplot as plt

#datasetportfolio@barbara-python.iam.gserviceaccount.com
#con esta linea lo conecto directo de la pagina web
#dataSet=pd.read_csv("https://www.fdic.gov/bank/individual/failed/banklist.csv", on_bad_lines="skip", encoding="ISO-8859-1")

# Ruta al archivo CSV descargado
ruta_csv = "C:\\Users\\barba\\OneDrive\\Documentos\\Python practica\\dataHR.csv"

dataHR=pd.read_csv(ruta_csv)

# Configura las credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('clave.json', scope)
client = gspread.authorize(creds)

sh = client.open_by_url('https://docs.google.com/spreadsheets/d/1UISnMoJfMteg96yeKrTS3PEfar0dafddmop1bcrhqmc/edit#gid=0')

#spreadsheet_id = '1UISnMoJfMteg96yeKrTS3PEfar0dafddmop1bcrhqmc'
#service = build('sheets', 'v4', credentials=creds)
#sheet = service.spreadsheets()

worksheet = sh.worksheet("uno")

worksheet.clear()

# Convertir el DataFrame a una lista de listas
values_to_update = [dataHR.columns.values.tolist()] + dataHR.values.tolist()
valor = values_to_update

# Actualizar la hoja de cálculo con los datos del DataFrame
worksheet.update(valor, 'uno! 1:1473')


print(dataHR.info())

#para tener la info de una columna en especifico
#print(dataHR.Age.describe())


#si solo quiero ver las columnas de texto quito la libreria numpy y sustituyo por la palabra "object"
print(dataHR.describe(include=[object]))

print(dataHR.describe(include=[np.number], percentiles=[.1,.9]))

#ofrece los 5 1eros registros 
print(dataHR.head)
print(dataHR.tail())
#para ver la cantidad de filas y columnas en ese orden
print(dataHR.shape)

print (dataHR.columns)

x=[1,2,3,4,5,6]
y=[21,22,23,24,25,26]

plt.bar(x,y)