# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:59:29 2017

@author: carlos.arana
"""

# Librerias utilizadas
import urllib.request
import datetime
import zipfile

# Descargar y descomprimir la base de datos del Sistema Urbano Nacional en formato SHP
url = r'http://internet.contenidos.inegi.org.mx/contenidos/Productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463142683_s.zip'
filename = r'.\00_RawData\00_Geo\Mgeo\{}_mgeo.zip'.format(datetime.datetime.today().strftime('%Y%m%d_%H%M_'))
print('Retrieving Data ...'); urllib.request.urlretrieve(url, filename); print('DONE')

zip_ref = zipfile.ZipFile(filename, 'r')
print('Extracting Data ...'); zip_ref.extractall(r'.\00_RawData\00_Geo\Mgeo'); print('done')
zip_ref.close()

# Convertir datos descargados como CSV a Pandas Dataframe.
