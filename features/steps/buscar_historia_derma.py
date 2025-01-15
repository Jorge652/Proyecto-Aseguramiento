from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

@given('que estoy en la página de búsqueda de historia clínica dermatológica')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:5000/buscar_historia_d')

@when('ingreso la cédula del propietario de la historia clínica dermatológica')
def step_impl(context):
    browser = context.browser
    cedula_input = browser.find_element(By.NAME, 'cedula_d')
    cedula_input.send_keys('1727457788')

@when('hago clic en el botón de buscar historia dermatológica')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

@when('hago clic en el botón de "OK" en el cuadro de diálogo de la busqueda de historia clínica dermatológica')
def step_impl(context):
    alert = context.browser.switch_to.alert
    alert.accept()

@then('debería ver los resultados de la búsqueda de historias clínicas dermatológicas')
def step_impl(context):
    assert 'Resultados de la Búsqueda de Historias Clínicas Dermatológicas' in context.browser.page_source
    context.browser.quit()