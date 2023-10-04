import sender_stand_request
import data
import pytest

#Función para recibir el authToken de un nuevo usuario o usuaria
def get_new_user_token_test():
    user_body = data.user_body.copy()
    return user_body

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] == data.auth_token


#Función para cambiar el valor del parámetro "name"
def get_kit_body(new_name):
    current_body = data.kit_body.copy()
    current_body["name"] = new_name
    return current_body

#Función de prueba positiva
def positive_assert_test(new_name):
    kit_body = get_kit_body(new_name)
    auth_token = get_new_user_token_test()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201

#Función de prueba negativa para el error 400 "No se enviaron los parámetros requeridos"
def negative_assert_code_400_test(new_name):
    kit_body = get_kit_body(new_name)
    auth_token = get_new_user_token_test()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400

    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 1 - Kit creado con éxito. El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert_test("a")

# Prueba 2 - Kit creado con éxito. El número permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert_test("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3 - Error. El número de caracteres es menor a la cantidad permitida (0)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400_test("")

# Prueba 4 - Error. El número de caracteres es mayor a la cantidad permitida (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400_test("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
            "dabcdabcD")

# Prueba 5 - Kit creado con éxito. Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert_test("""№%@",""")

# Prueba 6 - Kit creado con éxito. Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert_test("A Aaa")

# Prueba 7 - Kit creado con éxito. Se permiten números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert_test("123")

# Prueba 8 - Error. El parámetro no se pasa en la solicitud. Falta el parámetro 'name'
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400_test(kit_body)

# Prueba 9 - Error. Se ha pasado un parámetro diferente (número)
def test_create_kit_number_type_name_fet_error_response():
    kit_body = get_kit_body(12)
    auth_token = get_new_user_token_test()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400
