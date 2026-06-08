import csv
import json

productos = []

with open("productos.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:

        fila["id_producto"] = int(fila["id_producto"])
        fila["precio"] = float(fila["precio"])
        fila["cantidad"] = int(fila["cantidad"])
        fila["producto"] = fila["producto"].strip()

        productos.append(fila)

with open("proveedores.json", encoding="utf-8") as archivo:
    proveedores = json.load(archivo)

proveedores_dict = {}

for proveedor in proveedores:

    proveedor_limpio = proveedor.copy()

    proveedor_limpio["id_producto"] = int(proveedor_limpio["id_producto"])
    proveedor_limpio["proveedor"] = proveedor_limpio["proveedor"].strip()

    fecha = str(proveedor_limpio["fecha_entrega"])

    if len(fecha) == 8:
        fecha = fecha[:4] + "-" + fecha[4:6] + "-" + fecha[6:]

    proveedor_limpio["fecha_entrega"] = fecha

    proveedores_dict[proveedor_limpio["id_producto"]] = proveedor_limpio

resultado = []

for producto in productos:

    if producto["id_producto"] in proveedores_dict:

        proveedor = proveedores_dict[producto["id_producto"]].copy()

        del proveedor["id_producto"]

        objeto_final = {**producto, **proveedor}

        resultado.append(objeto_final)

for fila in resultado:
    print(fila)

# -------- JSON COMBINADO --------

with open("productos_combinados.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)