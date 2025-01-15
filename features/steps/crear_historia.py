from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

@given('que estoy en la página de nueva historia clinica general')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:5000/nueva_historia')

@when('ingreso los datos de la historia clínica')
def step_impl(context):
    browser = context.browser
    browser.find_element(By.NAME, 'cedula').send_keys('1727521435')
    browser.find_element(By.NAME, 'propietario').send_keys('Juan Perez')
    browser.find_element(By.NAME, 'direccion').send_keys('Calle Falsa 123')
    browser.find_element(By.NAME, 'direccion_d').send_keys('Calle Falsa 456')
    browser.find_element(By.NAME, 'medico_responsable').send_keys('Dr. Smith')
    
    # Enviar fechas directamente al campo de entrada
    fecha_creacion = browser.find_element(By.NAME, 'fecha_creacion')
    fecha_creacion.send_keys(Keys.CONTROL + "a")
    fecha_creacion.send_keys(Keys.DELETE)
    fecha_creacion.send_keys('2025-01-14')
    
    browser.find_element(By.NAME, 'telefono').send_keys('0987654321')
    browser.find_element(By.NAME, 'nombre_paciente').send_keys('Firulais')
    
    fecha_nacimiento = browser.find_element(By.NAME, 'fecha_nacimiento')
    fecha_nacimiento.send_keys(Keys.CONTROL + "a")
    fecha_nacimiento.send_keys(Keys.DELETE)
    fecha_nacimiento.send_keys('2020-01-01')
    
    browser.find_element(By.NAME, 'especie').send_keys('Perro')
    browser.find_element(By.NAME, 'raza').send_keys('Labrador')
    browser.find_element(By.NAME, 'sexo').send_keys('Macho')
    browser.find_element(By.NAME, 'color').send_keys('Negro')
    browser.find_element(By.NAME, 'vacuna_1').send_keys('Rabia')
    
    fecha_vacuna_1 = browser.find_element(By.NAME, 'fecha_vacuna_1')
    fecha_vacuna_1.send_keys(Keys.CONTROL + "a")
    fecha_vacuna_1.send_keys(Keys.DELETE)
    fecha_vacuna_1.send_keys('2021-01-01')
    
    browser.find_element(By.NAME, 'vacuna_2').send_keys('Parvovirus')
    
    fecha_vacuna_2 = browser.find_element(By.NAME, 'fecha_vacuna_2')
    fecha_vacuna_2.send_keys(Keys.CONTROL + "a")
    fecha_vacuna_2.send_keys(Keys.DELETE)
    fecha_vacuna_2.send_keys('2021-06-01')
    
    browser.find_element(By.NAME, 'vacuna_3').send_keys('Moquillo')
    
    fecha_vacuna_3 = browser.find_element(By.NAME, 'fecha_vacuna_3')
    fecha_vacuna_3.send_keys(Keys.CONTROL + "a")
    fecha_vacuna_3.send_keys(Keys.DELETE)
    fecha_vacuna_3.send_keys('2021-12-01')
    
    browser.find_element(By.NAME, 'vacuna_4').send_keys('Hepatitis')
    
    fecha_vacuna_4 = browser.find_element(By.NAME, 'fecha_vacuna_4')
    fecha_vacuna_4.send_keys(Keys.CONTROL + "a")
    fecha_vacuna_4.send_keys(Keys.DELETE)
    fecha_vacuna_4.send_keys('2022-01-01')
    
    browser.find_element(By.NAME, 'vacuna_5').send_keys('Leptospirosis')
    
    fecha_vacuna_5 = browser.find_element(By.NAME, 'fecha_vacuna_5')
    fecha_vacuna_5.send_keys(Keys.CONTROL + "a")
    fecha_vacuna_5.send_keys(Keys.DELETE)
    fecha_vacuna_5.send_keys('2022-06-01')
    
    fecha_ultima_desparasitacion = browser.find_element(By.NAME, 'fecha_ultima_desparasitacion')
    fecha_ultima_desparasitacion.send_keys(Keys.CONTROL + "a")
    fecha_ultima_desparasitacion.send_keys(Keys.DELETE)
    fecha_ultima_desparasitacion.send_keys('2023-01-01')
    
    browser.find_element(By.NAME, 'motivo_consulta').send_keys('Consulta general')
    browser.find_element(By.NAME, 'sintomatologia').send_keys('Ninguna')
    browser.find_element(By.NAME, 'tratamiento').send_keys('Ninguno')
    browser.find_element(By.NAME, 'diagnostico_diferencial').send_keys('Ninguno')
    browser.find_element(By.NAME, 'examenes_complementarios').send_keys('Ninguno')
    browser.find_element(By.NAME, 'diagnostico_definitivo').send_keys('Saludable')
    browser.find_element(By.NAME, 'tratamiento_final').send_keys('Ninguno')
    browser.find_element(By.NAME, 'medicamento_1').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_1').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_2').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_2').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_3').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_3').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_4').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_4').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_5').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_5').send_keys('Ninguna')
    
    proxima_cita = browser.find_element(By.NAME, 'proxima_cita')
    proxima_cita.send_keys(Keys.CONTROL + "a")
    proxima_cita.send_keys(Keys.DELETE)
    proxima_cita.send_keys('2023-12-01')

@when('hago clic en el botón de crear historia')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

@when('hago click en el botón de "OK" en el cuadro de diálogo que dice "Cédula correcta"')
def step_impl(context):
    alert = context.browser.switch_to.alert
    alert.accept()

@then('debería ver la página de historia creada con éxito')
def step_impl(context):
    assert 'Historia creada con éxito' in context.browser.page_source
    context.browser.quit()