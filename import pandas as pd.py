# Información General (OF 123456.xls)
# import pandas as pd
# import numpy as np

# # Definir el número de OFs (lotes)
# num_of = 50

# # Generar datos simulados
# ordenes = np.arange(10001, 10001 + num_of)
# numero_material = ['123456'] * num_of
# texto_material = ['Antígeno XYZ'] * num_of
# lotes = ordenes
# fecha_inicio = pd.date_range(start='2024-01-01', periods=num_of, freq='2D')
# fecha_fin = fecha_inicio + pd.to_timedelta(np.random.randint(1, 5, size=num_of), unit='D')
# cantidad_entregada = np.round(np.random.uniform(1000, 2000, num_of), 2)
# unidad_medida = ['litros'] * num_of

# # Crear DataFrame
# df_of = pd.DataFrame({
#     'Orden': ordenes,
#     'Número de material': numero_material,
#     'Texto breve material': texto_material,
#     'Lote': lotes,
#     'Fecha de inicio real': fecha_inicio,
#     'Fecha de fin real': fecha_fin,
#     'Cantidad entregada': cantidad_entregada,
#     'Unidad de medida': unidad_medida
# })

# # Mostrar el DataFrame
# print(df_of.head())

# df_of.to_excel('OF_123456.xlsx', index=False)

#Datasets Fases: Preinóculo, Inóculo y Cultivo Final (Fases producción.xls)

# import numpy as np
# import pandas as pd

# # Definir el número de lotes
# num_lotes = 100

# # Simulación de la fase de Preinóculo
# lotes = np.arange(10001, 10001 + num_lotes)
# ph_linea_1 = np.random.uniform(6.5, 7.5, num_lotes)
# ph_linea_2 = np.random.uniform(6.5, 7.5, num_lotes)
# ph_linea_3 = np.random.uniform(6.5, 7.5, num_lotes)
# turbidez_linea_1 = np.random.uniform(0.3, 0.7, num_lotes)
# turbidez_linea_2 = np.random.uniform(0.3, 0.7, num_lotes)
# turbidez_linea_3 = np.random.uniform(0.3, 0.7, num_lotes)

# linea_1_utilizada = (ph_linea_1 < ph_linea_3).astype(int)
# linea_2_utilizada = (ph_linea_2 < ph_linea_3).astype(int)
# linea_3_utilizada = ((linea_1_utilizada + linea_2_utilizada) == 0).astype(int)

# df_preinoculo = pd.DataFrame({
#     'Lote': lotes,
#     'Fecha/hora inicio': pd.date_range(start='2024-01-01', periods=num_lotes, freq='12H'),
#     'Fecha/hora fin': pd.date_range(start='2024-01-01', periods=num_lotes, freq='12H') + pd.Timedelta(hours=10),
#     'pH línea 1': ph_linea_1,
#     'pH línea 2': ph_linea_2,
#     'pH línea 3': ph_linea_3,
#     'Turbidez línea 1': turbidez_linea_1,
#     'Turbidez línea 2': turbidez_linea_2,
#     'Turbidez línea 3': turbidez_linea_3,
#     'Línea 1 utilizada': linea_1_utilizada,
#     'Línea 2 utilizada': linea_2_utilizada,
#     'Línea 3 utilizada': linea_3_utilizada
# })

# # Simulación de la fase de Inóculo
# id_bioreactor = np.random.choice(['BR1', 'BR2', 'BR3'], num_lotes)
# volumen_cultivo = np.random.uniform(400, 500, num_lotes)
# turbidez_inicio_cultivo = np.random.uniform(0.1, 0.3, num_lotes)
# turbidez_final_cultivo = np.random.uniform(0.4, 0.8, num_lotes)
# viabilidad_final_cultivo = np.random.uniform(0.8, 1.0, num_lotes)

# df_inoculo = pd.DataFrame({
#     'Lote': lotes,
#     'ID bioreactor': id_bioreactor,
#     'Fecha/hora inicio': pd.date_range(start='2024-01-01', periods=num_lotes, freq='12H') + pd.Timedelta(hours=12),
#     'Fecha/hora fin': pd.date_range(start='2024-01-02', periods=num_lotes, freq='12H') + pd.Timedelta(hours=22),
#     'Volumen de cultivo': volumen_cultivo,
#     'Turbidez inicio cultivo': turbidez_inicio_cultivo,
#     'Turbidez final cultivo': turbidez_final_cultivo,
#     'Viabilidad final cultivo': viabilidad_final_cultivo
# })

# # Simulación de la fase de Cultivo Final
# orden_encadenado = np.random.choice([1, 2, 3], num_lotes)
# lote_parental = np.where(orden_encadenado == 1, np.nan, lotes - 1)
# volumen_inoculo = np.random.uniform(200, 300, num_lotes)
# id_centrifuga = np.random.choice(['C1', 'C2'], num_lotes)
# centrifugacion_1_turbidez = np.random.uniform(0.4, 0.7, num_lotes)
# centrifugacion_2_turbidez = np.random.uniform(0.3, 0.6, num_lotes)
# producto_1 = np.random.uniform(0.9, 1.2, num_lotes)
# producto_2 = np.random.uniform(0.8, 1.1, num_lotes)

# df_cultivo_final = pd.DataFrame({
#     'Lote': lotes,
#     'Orden en el encadenado': orden_encadenado,
#     'Lote parental': lote_parental,
#     'ID bioreactor': id_bioreactor,
#     'Fecha/hora inicio': pd.date_range(start='2024-01-03', periods=num_lotes, freq='12H'),
#     'Fecha/hora fin': pd.date_range(start='2024-01-04', periods=num_lotes, freq='12H'),
#     'Volumen de inóculo': volumen_inoculo,
#     'Turbidez inicio cultivo': turbidez_inicio_cultivo,
#     'Turbidez final cultivo': turbidez_final_cultivo,
#     'Viabilidad final cultivo': viabilidad_final_cultivo,
#     'ID centrífuga': id_centrifuga,
#     'Centrifugación 1 turbidez': centrifugacion_1_turbidez,
#     'Centrifugación 2 turbidez': centrifugacion_2_turbidez,
#     'Producto 1': producto_1,
#     'Producto 2': producto_2
# })

# # Guardar los datasets en archivos Excel
# df_preinoculo.to_excel('Fase_Preinoculo.xlsx', index=False)
# df_inoculo.to_excel('Fase_Inoculo.xlsx', index=False)
# df_cultivo_final.to_excel('Fase_Cultivo_Final.xlsx', index=False)

#Datasets Bioreactores (Bioreactor XXXXX.xls)

# import pandas as pd
# import numpy as np

# # Definir el número de puntos de datos
# num_puntos = 96  # 4 días de datos, uno cada 15 minutos

# # Definir las variables simuladas
# fechas = pd.date_range(start='2024-01-01', periods=num_puntos, freq='15T')
# agitation_pv = np.random.uniform(50, 150, num_puntos)
# air_sparge_pv = np.random.uniform(0.1, 1.0, num_puntos)
# biocontainer_pressure_pv = np.random.uniform(0.8, 1.2, num_puntos)
# do_1_pv = np.random.uniform(20, 100, num_puntos)
# do_2_pv = np.random.uniform(20, 100, num_puntos)
# gas_overlay_pv = np.random.uniform(0.5, 1.5, num_puntos)
# load_cell_net_pv = np.random.uniform(200, 300, num_puntos)
# ph_1_pv = np.random.uniform(6.5, 7.5, num_puntos)
# ph_2_pv = np.random.uniform(6.5, 7.5, num_puntos)
# pump_1_pv = np.random.uniform(0, 1, num_puntos)
# pump_1_total = np.cumsum(pump_1_pv)
# pump_2_pv = np.random.uniform(0, 1, num_puntos)
# pump_2_total = np.cumsum(pump_2_pv)
# single_use_do_pv = np.random.uniform(20, 100, num_puntos)
# single_use_ph_pv = np.random.uniform(6.5, 7.5, num_puntos)
# temperatura_pv = np.random.uniform(35, 37, num_puntos)

# # Crear el DataFrame
# df_bioreactor = pd.DataFrame({
#     'DateTime': fechas,
#     'Agitation_PV': agitation_pv,
#     'Air_Sparge_PV': air_sparge_pv,
#     'Biocontainer_Pressure_PV': biocontainer_pressure_pv,
#     'DO_1_PV': do_1_pv,
#     'DO_2_PV': do_2_pv,
#     'Gas_Overlay_PV': gas_overlay_pv,
#     'Load_Cell_Net_PV': load_cell_net_pv,
#     'pH_1_PV': ph_1_pv,
#     'pH_2_PV': ph_2_pv,
#     'PUMP_1_PV': pump_1_pv,
#     'PUMP_1_TOTAL': pump_1_total,
#     'PUMP_2_PV': pump_2_pv,
#     'PUMP_2_TOTAL': pump_2_total,
#     'Single_Use_DO_PV': single_use_do_pv,
#     'Single_Use_pH_PV': single_use_ph_pv,
#     'Temperatura_PV': temperatura_pv
# })

# # Guardar el dataset en un archivo Excel
# df_bioreactor.to_excel('Bioreactor_13171.xlsx', index=False)

# # cintetico IPC
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# # Función para generar fechas y horas aleatorias
# def generate_random_dates(start_date, end_date, n):
#     start = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
#     end = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
#     return [start + timedelta(minutes=np.random.randint(0, int((end - start).total_seconds() / 60))) for _ in range(n)]

# # Generar datos para "Cinéticos IPC" pestaña Inóculos
# def generate_cineticos_inoculos():
#     n = 100  # Número de observaciones
#     lotes = np.random.choice(range(1000, 1100), size=n)  # Números de lotes aleatorios
#     fechas = generate_random_dates("2024-01-01 00:00:00", "2024-01-30 23:59:59", n)
#     turbidez = np.random.uniform(0.1, 5.0, size=n)
#     viabilidad = np.random.uniform(50, 100, size=n)
    
#     df_inoculos = pd.DataFrame({
#         'Lote': lotes,
#         'Fecha': fechas,
#         'Turbidez': turbidez,
#         'Viabilidad': viabilidad
#     })
#     return df_inoculos

# # Generar datos para "Cinéticos IPC" pestaña Cultivos finales
# def generate_cineticos_cultivos_finales():
#     n = 100  # Número de observaciones
#     lotes = np.random.choice(range(1000, 1100), size=n)  # Números de lotes aleatorios
#     fechas = generate_random_dates("2024-01-01 00:00:00", "2024-01-30 23:59:59", n)
#     turbidez = np.random.uniform(0.1, 5.0, size=n)
#     viabilidad = np.random.uniform(50, 100, size=n)
#     glucosa = np.random.uniform(0.1, 10.0, size=n)
    
#     df_cultivos = pd.DataFrame({
#         'Lote': lotes,
#         'Fecha': fechas,
#         'Turbidez': turbidez,
#         'Viabilidad': viabilidad,
#         'Glucosa': glucosa
#     })
#     return df_cultivos

# # Generar datos para "Cinéticos IPC" pestaña Centrifugación
# def generate_cineticos_centrifugacion():
#     n = 100  # Número de observaciones
#     lotes = np.random.choice(range(1000, 1100), size=n)  # Números de lotes aleatorios
#     centrifugas = np.random.choice(['Centrífuga 1', 'Centrífuga 2', 'Centrífuga 3'], size=n)
#     centrifugada = np.random.choice([1, 2], size=n)  # 1 o 2 para indicar primera o segunda centrifugación
#     volumen = np.random.uniform(0.5, 10.0, size=n)
#     turbidez = np.random.uniform(0.1, 5.0, size=n)
    
#     df_centrifugacion = pd.DataFrame({
#         'Lote': lotes,
#         'Centrífuga': centrifugas,
#         'Centrifugada': centrifugada,
#         'Volumen centrifugado': volumen,
#         'Turbidez': turbidez
#     })
#     return df_centrifugacion

# # Guardar datasets en archivos Excel
# def save_datasets():
#     df_inoculos = generate_cineticos_inoculos()
#     df_cultivos = generate_cineticos_cultivos_finales()
#     df_centrifugacion = generate_cineticos_centrifugacion()
    
#     with pd.ExcelWriter('Cinéticos_IPC.xlsx', engine='openpyxl') as writer:
#         df_inoculos.to_excel(writer, sheet_name='Inóculos', index=False)
#         df_cultivos.to_excel(writer, sheet_name='Cultivos finales', index=False)
#         df_centrifugacion.to_excel(writer, sheet_name='Centrifugación', index=False)

# # Ejecutar la función para guardar los datasets
# save_datasets()

# Fase de Centrifugación
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# # Función para generar fechas y horas aleatorias
# def generate_random_dates(start_date, end_date, n):
#     start = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
#     end = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
#     return [start + timedelta(minutes=15 * i) for i in range(n)]

# # Generar datos en tiempo real para una centrífuga
# def generate_centrifuga_data(equipo, start_date, end_date):
#     n = (datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")).seconds // 900 + 1
#     dates = generate_random_dates(start_date, end_date, n)
#     data = {
#         f"{equipo}_CTF0101.EN_Parcial": np.random.randint(0, 100, size=n),
#         f"{equipo}_CTF0101.EN_Total": np.random.randint(0, 200, size=n),
#         f"{equipo}_D01780551.PV": np.random.uniform(0, 10, size=n),
#         f"{equipo}_D01906041.PV": np.random.uniform(0, 5, size=n),
#         f"{equipo}_D01916047.PV": np.random.uniform(0, 2, size=n),
#         f"{equipo}_D01916503.PV": np.random.uniform(0, 8, size=n),
#         f"{equipo}_D01919022.PV": np.random.uniform(0, 12000, size=n)
#     }
    
#     df = pd.DataFrame(data, index=dates)
#     return df

# # Generar datos para el archivo de horas de inicio/fin de centrifugación
# def generate_horas_inicio_fin():
#     equipos = ['12912', '14246', '17825']
#     n = 50  # Número total de eventos
#     data = {
#         'Equipo': np.random.choice(equipos, size=n),
#         'Operación': np.random.choice(['Inicio 1', 'Fin 1', 'Inicio 2', 'Fin 2'], size=n),
#         'Orden': np.random.choice([123456, 123457, 123458], size=n),
#         'DateValue': [datetime.now() - timedelta(minutes=np.random.randint(0, 10080)) for _ in range(n)]
#     }
    
#     df = pd.DataFrame(data)
#     return df

# # Guardar datos en archivos Excel
# def save_datasets():
#     equipos = ['12912', '14246', '17825']
#     start_date = "2024-01-01 00:00:00"
#     end_date = "2024-01-31 23:59:59"
    
#     with pd.ExcelWriter('Centrífuga_Datos.xlsx', engine='openpyxl') as writer:
#         for equipo in equipos:
#             df = generate_centrifuga_data(equipo, start_date, end_date)
#             df.to_excel(writer, sheet_name=f'Centrífuga_{equipo}', index=True)
    
#     # Guardar el archivo de horas de inicio/fin
#     df_horas = generate_horas_inicio_fin()
#     df_horas.to_excel('Horas_inicio_fin_centrifugas.xlsx', index=False)

# # Ejecutar la función para guardar los datasets
# save_datasets()

# # Materias Primas Utilizadas

# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# # Función para generar fechas aleatorias
# def generate_random_dates(start_date, end_date, n):
#     start = datetime.strptime(start_date, "%Y-%m-%d")
#     end = datetime.strptime(end_date, "%Y-%m-%d")
#     return [start + timedelta(days=np.random.randint(0, (end - start).days)) for _ in range(n)]

# # Función para generar el dataset de materias primas utilizadas
# def generate_materias_primas_data(num_entries):
#     materiales = ['Material_A', 'Material_B', 'Material_C', 'Material_D']
#     num_lotes = 10
#     num_lotes_proveedor = 5
#     start_date = "2023-01-01"
#     end_date = "2023-12-31"
    
#     data = {
#         'Lote': np.random.randint(1000, 1100, size=num_entries),
#         'Material': np.random.choice(materiales, size=num_entries),
#         'Lote interno': np.random.randint(2000, 2100, size=num_entries),
#         'Lote proveedor': np.random.randint(3000, 3100, size=num_entries),
#         'Qty': np.random.uniform(10, 500, size=num_entries).round(2),
#         'Fecha recepción': generate_random_dates(start_date, end_date, num_entries),
#         'Fecha traslado': generate_random_dates(start_date, end_date, num_entries)
#     }
    
#     df = pd.DataFrame(data)
#     df['Fecha recepción'] = pd.to_datetime(df['Fecha recepción'])
#     df['Fecha traslado'] = pd.to_datetime(df['Fecha traslado'])
    
#     # Asegurarse de que Fecha traslado sea posterior a Fecha recepción
#     df['Fecha traslado'] = df.apply(
#         lambda row: row['Fecha recepción'] + timedelta(days=np.random.randint(1, 10)) if row['Fecha traslado'] < row['Fecha recepción'] else row['Fecha traslado'],
#         axis=1
#     )
    
#     return df

# # Guardar el dataset en un archivo Excel
# def save_materias_primas_dataset():
#     num_entries = 100  # Número total de entradas en el dataset
#     df = generate_materias_primas_data(num_entries)
#     df.to_excel('Materias_Primas_Utilizadas.xlsx', index=False)

# # Ejecutar la función para guardar el dataset
# save_materias_primas_dataset()

# Temperaturas y Humedades

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Función para generar fechas aleatorias
def generate_random_dates(start_date, end_date, n):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return [start + timedelta(minutes=np.random.randint(0, (end - start).total_seconds() // 60)) for _ in range(n)]

# Función para generar el dataset de temperaturas y humedades
def generate_temperaturas_humedades_data(num_entries):
    start_date = "2024-01-01"
    end_date = "2024-12-31"
    
    data = {
        'DateTime': generate_random_dates(start_date, end_date, num_entries),
        '06299_TI1302.PV': np.random.uniform(18, 25, size=num_entries).round(2),  # Temperatura sala biorreactores
        '06299_MI1302.PV': np.random.uniform(40, 60, size=num_entries).round(2),  # Humedad sala biorreactores
        '06299_TI1402.PV': np.random.uniform(18, 25, size=num_entries).round(2),  # Temperatura sala centrifugas
        '06299_MI1402.PV': np.random.uniform(40, 60, size=num_entries).round(2),  # Humedad sala centrifugas
        '07633_TI0601.PV': np.random.uniform(10, 20, size=num_entries).round(2),  # Temperatura almacén principal
        '07633_HI0101.PV': np.random.uniform(30, 50, size=num_entries).round(2),  # Humedad almacén principal
        '07781_TI1501.PV': np.random.uniform(15, 25, size=num_entries).round(2),  # Temperatura almacén producción
        '07781_MI1501.PV': np.random.uniform(40, 60, size=num_entries).round(2),  # Humedad almacén producción
    }
    
    df = pd.DataFrame(data)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    
    return df

# Guardar el dataset en un archivo Excel
def save_temperaturas_humedades_dataset():
    num_entries = 1000  # Número total de entradas en el dataset
    df = generate_temperaturas_humedades_data(num_entries)
    df.to_excel('Temperaturas_y_Humedades.xlsx', index=False)

# Ejecutar la función para guardar el dataset
save_temperaturas_humedades_dataset()