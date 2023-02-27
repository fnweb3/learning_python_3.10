
# Mensaje de la Aplicación
print("--- REALIZAR UNA VENTA ----")

# Entrada de datos
vv = float(input('Ingrese valor de venta: '))

# Operaciones
igv = vv * 0.18
pv = vv + igv

# Salida de datos
print ('='*25)
print(' --- FACTURA DE VENTA ---')
print ('='*25)
print ('Valor de venta ', vv)
print ('IGV: ', igv)
print ('Precio de venta: ', pv)
print ('='*25)
