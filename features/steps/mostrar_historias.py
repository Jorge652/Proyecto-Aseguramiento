from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que estoy en la página de inicio')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:5000/')

@when('hago clic en el botón de "Mostrar Todas las Historias Disponibles"')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, 'Mostrar Todas las Historias Disponibles').click()

@then('debería ver la página con todas las historias clínicas disponibles')
def step_impl(context):
    assert 'Historias Generales' in context.browser.page_source
    assert 'Historias Dermatológicas' in context.browser.page_source
    context.browser.quit()