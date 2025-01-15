from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('que estoy en la página de edición de la historia clínica dermatológica con ID 1')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:5000/editar_historia_d/1')

@when('cambio el nombre del medicamento 1 a "Nuevo Medicamento Dermatológico"')
def step_impl(context):
    browser = context.browser
    medicamento_1_input = browser.find_element(By.NAME, 'medicamento_1_d')
    medicamento_1_input.clear()
    medicamento_1_input.send_keys('Nuevo Medicamento Dermatológico')

@when('hago clic en el botón de actualizar historia dermatológica')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

@then('debería ver la página de historia dermatológica actualizada con éxito')
def step_impl(context):
    time.sleep(1)  # Esperar a que la redirección se complete
    assert context.browser.current_url == 'http://localhost:5000/historia_actualizada'
    context.browser.quit()