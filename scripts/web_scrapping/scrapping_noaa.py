import requests
import json

# Tu clave de API de NOAA
api_key = "ozbZoNEGlCBQYZQgFUlZzPkAWfbknKlJ"

# URL base de la API
base_url = "https://www.ncei.noaa.gov/cdo-web/api/v2/locations?datasetid=GHCND"

# ID del dataset que quieres consultar
# dataset_id = "GSOY"  # Cambia esto al ID que necesites

# Encabezados para la solicitud
headers = {"token": api_key}

# Realizar la solicitud
response = requests.get(f"{base_url}", headers=headers)

# Verificar la respuesta
if response.status_code == 200:
    # Parsear los datos en formato JSON
    data = response.json()
    print("Información del Dataset:")
    # print(data)


# Supongamos que tienes la respuesta en formato JSON
response_data = response.json()  # Convierte la respuesta a un diccionario de Python

# Explora los datos disponibles
print(
    json.dumps(response_data, indent=4)
)  # Muestra toda la estructura de los datos de manera legible

# Extrae información específica
if "name" in response_data:
    dataset_name = response_data["name"]
    # print(f"Nombre del Dataset: {dataset_name}")

else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
