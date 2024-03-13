"""
Autor: Luis Dominguez

Args:
    input: data.csv
    
Returns:
    Este script crea imagenes para la interpretación de resultados 


Fecha de creación: 6 de marzo de 2024
"""

import pandas as pd
import matplotlib.pyplot as plt

import os

from pathlib import Path, PurePath

plt.rcParams['text.usetex'] = True

# Editar el tamaño de la fuente
font = {'size': 18}
plt.rc('font', **font)

# Creación del directorio
try:
    os.makedirs("images_jona")
except FileExistsError:
    pass

PurePath.joinpath(Path.cwd(),'images_jona', 'A VS BEA').mkdir(parents=True,exist_ok=True)
PurePath.joinpath(Path.cwd(),'images_jona', 'Z VS BEA').mkdir(parents=True,exist_ok=True)

df_path_pred = 'data_predict_transfer/data/data_General.csv'
df_path_t = 'Input/data_LD_t.csv'
df_path_LD = 'data/dataset_LD.csv'
df_path_ws4 = 'data/dataset_WS4.csv'
df_path_sly4 = 'data/dataset_Sly4.csv'

df_pred = pd.read_csv("data_General.csv")
df_t = pd.read_csv('data_LD_t.csv')
df_LD = pd.read_csv('dataset_LD.csv')
df_ws4 = pd.read_csv('dataset_WS4.csv')
df_sly4 = pd.read_csv('dataset_Sly4.csv')

df_pred = df_pred.values
df_t = df_t.values
df_LD = df_LD.values
df_ws4 = df_ws4.values
df_sly4 = df_sly4.values

z_pred = df_pred[:,1]
a_pred = df_pred[:,3]
bea_pred = df_pred[:,7]

z_t = df_t[:,2]
a_t = df_t[:,3]
bea_t = df_t[:,4]

z_LD = df_LD[:,1]
a_LD = df_LD[:,3]
bea_LD = df_LD[:,7]

z_ws4 = df_ws4[:,1]
a_ws4 = df_ws4[:,3]
bea_ws4 = df_ws4[:,7]

z_sly4 = df_sly4[:,1]
a_sly4 = df_sly4[:,3]
bea_sly4 = df_sly4[:,7]

################## Para gráficas A vs BEA

#### Predicción vs Experimentales
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(a_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(a_t, bea_t, label='EXPERIMENTALES', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$Ajjsj$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EAjjsj}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs Experimentales")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/A VS BEA/PREDvsEXPERI.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs Gota Liquida
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(a_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(a_LD, bea_LD, label='GOTA LÍQUIDA', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$A$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs GOTA LÍQUIDA")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/A VS BEA/PREDvsLD.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs WS4
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(a_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(a_ws4, bea_ws4, label='WS4', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$A$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs WS4")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/A VS BEA/PREDvsWS4.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs Sly4
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(a_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(a_sly4, bea_sly4, label='Sly4', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$A$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs Sly4")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/A VS BEA/PREDvsSLY4.png',dpi=600)

#plt.show()  # Mostrar el gráfico

################################ Para gráficas z vs BEA

#### Predicción vs Experimentales
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(z_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(z_t, bea_t, label='EXPERIMENTALES', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$Z$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs Experimentales")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/Z VS BEA/PREDvsEXPERI.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs Gota Liquida
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(z_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(z_LD, bea_LD, label='GOTA LÍQUIDA', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$Z$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs GOTA LÍQUIDA")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/Z VS BEA/PREDvsLD.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs WS4
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(z_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(z_ws4, bea_ws4, label='WS4', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$Z$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs WS4")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/Z VS BEA/PREDvsWS4.png',dpi=600)

#plt.show()  # Mostrar el gráfico

#### Predicción vs Sly4
fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

# Graficar los datos
ax.scatter(z_pred, bea_pred, label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
ax.scatter(z_sly4, bea_sly4, label='Sly4', color='green', alpha=0.5, marker=".")
ax.set_aspect('auto', adjustable='datalim')
ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

# Configurar los ejes
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_label_position('bottom')
ax.yaxis.set_label_position('left')

# Agregar etiquetas a los ejes
ax.set_xlabel(r'$Z$') #se crea la etiqueta del eje x en formato latex
ax.set_ylabel(r'$B{\scriptstyle EA}\ {\rm KeV}$') #se crea la etiqueta del eje y en formato latex
ax.set_title("Predicción vs Sly4")
legend = ax.legend(loc='lower right', fontsize='small')

# Cambiar tamaño de los puntos en la leyenda
legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (EXPERIMENTALES)

plt.savefig('images_jona/Z VS BEA/PREDvsSLY4.png',dpi=600)

#plt.show()  # Mostrar el gráfico


#### FORMA RECURSIVA
# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# from pathlib import Path

# def plot_and_save(df1, df2, x_label, y_label, title, output_path):
#     fig, ax = plt.subplots(figsize=(12, 8))  # Crear una sola figura

#     # Graficar los datos
#     ax.scatter(df1[:, 0], df1[:, 1], label='PREDICCIÓN', color='red', alpha=0.75, marker=".")
#     ax.scatter(df2[:, 0], df2[:, 1], label='DATOS', color='green', alpha=0.5, marker=".")
#     ax.set_aspect('auto', adjustable='datalim')
#     ax.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black')

#     # Configurar los ejes
#     ax.xaxis.set_ticks_position('both')
#     ax.yaxis.set_ticks_position('both')
#     ax.xaxis.set_label_position('bottom')
#     ax.yaxis.set_label_position('left')

#     # Agregar etiquetas a los ejes
#     ax.set_xlabel(x_label) #se crea la etiqueta del eje x en formato latex
#     ax.set_ylabel(y_label) #se crea la etiqueta del eje y en formato latex
#     ax.set_title(title)
#     legend = ax.legend(loc='lower right', fontsize='small')

#     # Cambiar tamaño de los puntos en la leyenda
#     legend.legend_handles[0]._sizes = [200]  # Cambia el tamaño del punto para la primera entrada (PREDICCIÓN)
#     legend.legend_handles[1]._sizes = [200]  # Cambia el tamaño del punto para la segunda entrada (DATOS)

#     plt.savefig(output_path, dpi=600)
#     plt.close()

# plt.rcParams['text.usetex'] = True

# # Editar el tamaño de la fuente
# font = {'size': 18}
# plt.rc('font', **font)

# # Creación del directorio
# output_directory = "images_jona"
# try:
#     os.makedirs(output_directory)
# except FileExistsError:
#     pass

# # Definir los conjuntos de datos y sus rutas
# datasets = [
#     ('data_predict_transfer/data/data_General.csv', 'Input/data_LD_t.csv', 'A VS BEA', 'PREDvsEXPERI'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_LD.csv', 'A VS BEA', 'PREDvsLD'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_WS4.csv', 'A VS BEA', 'PREDvsWS4'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_Sly4.csv', 'A VS BEA', 'PREDvsSLY4'),
#     ('data_predict_transfer/data/data_General.csv', 'Input/data_LD_t.csv', 'Z VS BEA', 'PREDvsEXPERI'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_LD.csv', 'Z VS BEA', 'PREDvsLD'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_WS4.csv', 'Z VS BEA', 'PREDvsWS4'),
#     ('data_predict_transfer/data/data_General.csv', 'data/dataset_Sly4.csv', 'Z VS BEA', 'PREDvsSLY4')
# ]

# for df_path_pred, df_path_data, directory, filename in datasets:
#     df_pred = pd.read_csv(df_path_pred)
#     df_data = pd.read_csv(df_path_data)

#     if 'Input/data_LD_t.csv' in df_path_data:
#         df_data_values = df_data.values[:, [3, 4]]  # A, BEA
#     else:
#         df_data_values = df_data.values[:, [3, 7]]  # A, BEA

#     df_pred_values = df_pred.values[:, [3, 7]]  # A, BEA

#     output_path = os.path.join(output_directory, directory, filename + '.png')
#     Path(output_path).parent.mkdir(parents=True, exist_ok=True)

#     plot_and_save(df_pred_values, df_data_values, r'$A$', r'$B{\scriptstyle EA}\ {\rm KeV}$', filename, output_path)

# for df_path_pred, df_path_data, directory, filename in datasets:
#     df_pred = pd.read_csv(df_path_pred)
#     df_data = pd.read_csv(df_path_data)

#     if 'Input/data_LD_t.csv' in df_path_data:
#         df_data_values = df_data.values[:, [2, 4]]  # Z, BEA
#     else:
#         df_data_values = df_data.values[:, [1, 7]]  # Z, BEA

#     df_pred_values = df_pred.values[:, [1, 7]]  # Z, BEA

#     output_path = os.path.join(output_directory, directory, filename + '.png')
#     Path(output_path).parent.mkdir(parents=True, exist_ok=True)

#     plot_and_save(df_pred_values, df_data_values, r'$A$', r'$B{\scriptstyle EA}\ {\rm KeV}$', filename, output_path)