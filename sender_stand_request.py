import configuration
import requests
import data


#Crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, headers=data.headers)

response_user = post_new_user(data.user_body);
print(response_user.status_code)
print(response_user.json())

#Crear un kit
def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body, headers=auth_token)

response_kit = post_new_client_kit(data.kit_body.copy(), data.headers.copy())
print(response_kit.status_code)
print(response_kit.json())
