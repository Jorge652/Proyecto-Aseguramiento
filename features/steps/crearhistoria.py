from behave import given, when, then

# Variables globales para los números y el resultado
numeros = {}
resultado = None

@given("tengo los números {num1:d} y {num2:d}")
def step_given_tengo_los_numeros(context, num1, num2):
    numeros["num1"] = num1
    numeros["num2"] = num2

@when("los sumo")
def step_when_los_sumo(context):
    global resultado
    resultado = numeros["num1"] + numeros["num2"]
@then("el resultado debe ser {esperado:d}")
def step_then_el_resultado_debe_ser(context, esperado):
    assert resultado == esperado, f"Esperado {esperado}, pero fue {resultado}"