# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:59:29 2017

@author: carlos.arana
"""

# Librerias utilizadas
import os
import urllib.request
import datetime
import zipfile
import pandas as pd
from simpledbf import Dbf5

# Descargar y descomprimir la base de datos del Sistema Urbano Nacional en formato SHP
url = r'http://internet.contenidos.inegi.org.mx/contenidos/Productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463142683_s.zip'
filename = r'.\00_RawData\00_Geo\Mgeo\{}_mgeo.zip'.format(datetime.datetime.today().strftime('%Y%m%d_%H%M_'))


if not os.path.isdir(r'.\00_RawData\00_Geo\Mgeo\conjunto_de_datos'):
    print('Retrieving Data ...'); urllib.request.urlretrieve(url, filename); print('DONE')
    zip_ref = zipfile.ZipFile(filename, 'r')
    print('Extracting Data ...'); zip_ref.extractall(r'.\00_RawData\00_Geo\Mgeo'); print('done')
    zip_ref.close()
else: print('La información ya se había extraido')

# Convertir datos descargados como dbf a Pandas Dataframe.
mdbf = Dbf5(r'.\00_RawData\00_Geo\Mgeo\conjunto_de_datos\areas_geoestadisticas_municipales.dbf')
edbf = Dbf5(r'.\00_RawData\00_Geo\Mgeo\conjunto_de_datos\areas_geoestadisticas_estatales.dbf')
mun_df = mdbf.to_dataframe()
edo_df = edbf.to_dataframe()

# Combinar dataframes y producir un CSV
mun_df = mun_df.set_index('CVE_ENT')
edo_df = edo_df.set_index('CVE_ENT')
mgeo = mun_df.merge(edo_df, on = 'CVE_ENT')

mgeo.to_csv(r'.\00_RawData\00_Geo\Mgeo\GeoMex\indice_geoestadistico.csv')