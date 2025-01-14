# filepath: features/steps/crear_historia_steps.py
from behave import given, when, then
from flask import Flask
from flask.testing import FlaskClient

@given('que estoy en la página de creación de una nueva historia clínica')
def step_impl(context):
    context.client = FlaskClient(Flask(__name__))
    context.response = context.client.get('/nueva_historia')
    assert context.response.status_code == 200

@when('completo el formulario con los datos requeridos')
def step_impl(context):
    context.form_data = {
        'propietario': 'Juan Perez',
        'cedula': '1234567890',
        'direccion': 'Calle Falsa 123',
        'medico_responsable': 'Dr. Smith',
        'fecha_creacion': '2023-10-01',
        'telefono': '0987654321',
        'nombre_paciente': 'Firulais'
    }

@when('envío el formulario')
def step_impl(context):
    context.response = context.client.post('/nueva_historia', data=context.form_data)
    assert context.response.status_code == 302

@then('debería ser redirigido a la página de confirmación')
def step_impl(context):
    context.response = context.client.get('/historia_creada')
    assert context.response.status_code == 200

@then('debería ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje.encode() in context.response.data