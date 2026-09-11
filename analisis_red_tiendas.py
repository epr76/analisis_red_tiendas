import numpy as np
import pandas as pd


#csv inventories
df_csv_inventories = pd.read_csv('inventories.csv')
#csv sales
df_csv_sales = pd.read_csv('sales.csv')
#csv satisfaction
df_csv_satisfaction = pd.read_csv('satisfaction.csv')

#implementamos los dropna
inventories = df_csv_inventories.dropna()
sales =  df_csv_sales.dropna()
satisfaction =  df_csv_satisfaction.dropna()

#Calculamos la venta total de las tiendas.
productos_vendidos =  sales.groupby("Producto")["Cantidad_Vendida"].sum()
productos_vendidos_tienda =  sales.groupby("ID_Tienda")["Cantidad_Vendida"].sum()
print("Cantidad de productos vendidos:\n",productos_vendidos.to_string())

print("Cantidad de productos vendidos , clasificado por tienda:\n",productos_vendidos_tienda.to_string())

#Calculamos los ingresos totales por tienda
sales["Venta_Total"] = sales["Cantidad_Vendida"] * sales["Precio_Unitario"]
ventas_tienda = sales.groupby("ID_Tienda")["Venta_Total"].sum()
print("Calculo ingresos por tienda:\n",ventas_tienda.to_string())

#Generacion del describe
resumen_sales = sales.describe()
print("Resumen con el metodo describe:\n",resumen_sales)