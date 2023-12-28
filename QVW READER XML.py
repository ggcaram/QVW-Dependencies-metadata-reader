#QVW READER XML 

import os
import sys
# Ruta de la carpeta que quieres recorrer: completar con la carpeta donde estan los .QVWs
ruta_carpeta = r''

# Lista para almacenar los archivos con extensión .qvw
archivos_qvw = []

# Recorrer la carpeta
for nombre_archivo in os.listdir(ruta_carpeta):
    # Verificar si el archivo termina en ".qvw"
    if nombre_archivo.lower().endswith(".qvw"):
        # Construir la ruta completa del archivo
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
        nombre_qvw= nombre_archivo
        # Agregar la ruta completa a la lista
        archivos_qvw.append(ruta_completa)
        # Imprimo los nombres y las rutas completas de los qvws
        print('nombreQVWCreador: ', nombre_qvw)
        print('rutaQVWCreador: ', ruta_carpeta + '\\' + nombre_qvw)

# Flag para indicar si estamos dentro de la sección <LineageInfo>
inside_lineage_info = False

# Lista para almacenar las líneas que contienen <LineageInfo> y <Discriminator>
lineage_info_lines = []

# Lista para pasar los datos limpios, sin etiquetas, etc.
listado_limpio = []

# Imprimir la lista de archivos .qvw
for archivo_qvw in archivos_qvw:
    try:
        with open(archivo_qvw, 'rb') as qv_file:
            for line in qv_file:
                # Decodifico la línea usando 'latin-1' para manejar caracteres no UTF-8
                decoded_line = line.decode('latin-1', errors='ignore')
                # Verificamos si estamos dentro de la sección <LineageInfo>
                if "<LineageInfo>" in decoded_line:
                    inside_lineage_info = True
                    lineage_info_lines.append(decoded_line)
                elif "</LineageInfo>" in decoded_line:
                    inside_lineage_info = False
                    lineage_info_lines.append(decoded_line)
                # Verificamos si la línea contiene la subetiqueta <Discriminator>
                elif inside_lineage_info:
                    if "<Discriminator>" in decoded_line:
                        lineage_info_lines.append(decoded_line)

            # Agregamos las líneas que contienen <LineageInfo> y <Discriminator> reemplazando las etiquetas por espaciados
            for line in lineage_info_lines:
                cleaned_line = line.replace("<LineageInfo>", " ")
                cleaned_line2= cleaned_line.replace("</LineageInfo>", " ")
                cleaned_line3= cleaned_line2.replace("<Discriminator>", " ")
                cleaned_line4= cleaned_line3.replace("</Discriminator>", " ")
                cleaned_line5= cleaned_line4.strip()
                listado_limpio.append(cleaned_line5)
    # Agregamos excepciones con los errores             
    except FileNotFoundError:
        print(f"No se encontró el archivo QVW especificado: '{archivo_qvw}'")
    except Exception as e:
        print(f"Hubo un error: {str(e)}")

# Convierte el conjunto de valores únicos de nuevo a una lista
listado_unicos = list(set(listado_limpio))

# Tomo solo las lineas storeadas
qvdCreado_linea = [linea for linea in listado_unicos if 'STORE' in linea]

# Lo convierto a string
#qvdCreado_string = qvdCreado_linea[0]

# Lo convierto a string
qvdCreado_string= list(qvdCreado_linea)

# Creo la lista de los qvs consumidos 
lista_qvd_creado= [] 
lista_rutas_qvd_creado= [] 

# Descarto la ruta completa para solo tomar los nombres de los qvs 
for elemento in qvdCreado_string:
    ultima_barraqvdcreado= elemento.rsplit('\\', 1)[-1]
    lista_rutas_qvd_creado.append(elemento)
    lista_qvd_creado.append(ultima_barraqvdcreado)

# Listo solo los qvds consumidos 
# Tomo solo las lineas que contengan la ruta del disco {chequear}
qvdConsumido_linea = [linea for linea in listado_unicos if ':\\' in linea.lower()]

# Lo convierto a string
qvdConsumido_string= list(qvdConsumido_linea)

# Creo la lista de los qvs consumidos 
lista_qvd_consumido= [] 
lista_rutas_qvd_consumido= [] 

# Descarto la ruta completa para solo tomar los nombres de los qvs 
for elemento in qvdConsumido_string:
    ultima_barraqvdConsumido= elemento.rsplit('\\', 1)[-1]
    lista_rutas_qvd_consumido.append(elemento)
    lista_qvd_consumido.append(ultima_barraqvdConsumido)


# Edito la lista para que sea facilmente visualizable, es solo para testing
listado_visualizacion= "\n".join(listado_unicos)


for qvdconsumido in lista_qvd_consumido:
    print('nombreQVDConsumido: ', qvdconsumido)

for rutaqvdconsumido in lista_rutas_qvd_consumido:
    print('rutaQVDConsumido: ', rutaqvdconsumido)

for qvdcreado in lista_qvd_creado:  
    print('nombreQVDCreado ', qvdcreado)

for rutaqvdcreado in lista_rutas_qvd_creado:  
    print('rutaQVDCreado ', rutaqvdcreado)
