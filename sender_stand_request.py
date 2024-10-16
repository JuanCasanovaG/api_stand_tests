import configuration
import requests
import data


def post_new_user(body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # Concatenación de URL base y ruta.
                         json=body,  # Datos a enviar en la solicitud.
                         headers=data.headers)  # Encabezados de solicitud.


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())  # Muestra del resultado en la consola
