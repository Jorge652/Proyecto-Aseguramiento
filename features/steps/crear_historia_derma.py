from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('que estoy en la página de nueva historia clinica dermatológica')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:5000/nueva_historia_d')

@when('ingreso los datos de la historia clínica dermatológica')
def step_impl(context):
    browser = context.browser
    browser.find_element(By.NAME, 'cedula_d').send_keys('1234567890')
    browser.find_element(By.NAME, 'propietario_d').send_keys('Juan Perez')
    browser.find_element(By.NAME, 'direccion_d').send_keys('Calle Falsa 123')
    browser.find_element(By.NAME, 'medico_responsable_d').send_keys('Dr. Smith')
    browser.find_element(By.NAME, 'fecha_creacion_d').send_keys('2023-10-10')
    browser.find_element(By.NAME, 'telefono_d').send_keys('0987654321')
    browser.find_element(By.NAME, 'nombre_paciente_d').send_keys('Firulais')
    browser.find_element(By.NAME, 'fecha_nacimiento_d').send_keys('2020-01-01')
    browser.find_element(By.NAME, 'especie_d').send_keys('Perro')
    browser.find_element(By.NAME, 'raza_d').send_keys('Labrador')
    browser.find_element(By.NAME, 'sexo_d').send_keys('Macho')
    browser.find_element(By.NAME, 'color_d').send_keys('Negro')
    browser.find_element(By.NAME, 'vacuna_1_d').send_keys('Rabia')
    browser.find_element(By.NAME, 'fecha_vacuna_1_d').send_keys('2021-01-01')
    browser.find_element(By.NAME, 'vacuna_2_d').send_keys('Parvovirus')
    browser.find_element(By.NAME, 'fecha_vacuna_2_d').send_keys('2021-06-01')
    browser.find_element(By.NAME, 'vacuna_3_d').send_keys('Moquillo')
    browser.find_element(By.NAME, 'fecha_vacuna_3_d').send_keys('2021-12-01')
    browser.find_element(By.NAME, 'vacuna_4_d').send_keys('Hepatitis')
    browser.find_element(By.NAME, 'fecha_vacuna_4_d').send_keys('2022-01-01')
    browser.find_element(By.NAME, 'vacuna_5_d').send_keys('Leptospirosis')
    browser.find_element(By.NAME, 'fecha_vacuna_5_d').send_keys('2022-06-01')
    browser.find_element(By.NAME, 'fecha_ultima_desparasitacion_d').send_keys('2023-01-01')
    browser.find_element(By.NAME, 'motivo_consulta_d').send_keys('Consulta general')
    browser.find_element(By.NAME, 'sintomatologia_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'tratamiento_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'diagnostico_diferencial_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'otras_mascotas_d').send_keys('No')
    browser.find_element(By.NAME, 'nin_casa_d').send_keys('No')
    browser.find_element(By.NAME, 'familia_problema_d').send_keys('No')
    browser.find_element(By.NAME, 'tipo_comida_d').send_keys('Balanceada')
    browser.find_element(By.NAME, 'golosinas_d').send_keys('No')
    browser.find_element(By.NAME, 'caida_pelo_d').send_keys('No')
    browser.find_element(By.NAME, 'se_rasca_d').send_keys('No')
    browser.find_element(By.NAME, 'ambiente_d').send_keys('Casa')
    browser.find_element(By.NAME, 'pasa_sol_d').send_keys('No')
    browser.find_element(By.NAME, 'pasa_tierra_d').send_keys('No')
    browser.find_element(By.NAME, 'defecacion_d').send_keys('Normal')
    browser.find_element(By.NAME, 'parte_enrojecida_d').send_keys('No')
    browser.find_element(By.NAME, 'fecha_ectoparasitos_d').send_keys('2023-01-01')
    browser.find_element(By.NAME, 'descrip_ectoparasitos_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'duchas_casa_d').send_keys('Mensual')
    browser.find_element(By.NAME, 'alergia_comida_d').send_keys('No')
    browser.find_element(By.NAME, 'rasp_cutaneo_d').send_keys('No')
    browser.find_element(By.NAME, 'tricograma_d').send_keys('No')
    browser.find_element(By.NAME, 'lampara_wood_d').send_keys('No')
    browser.find_element(By.NAME, 'reflejo_otopodal_d').send_keys('No')
    browser.find_element(By.NAME, 'biopsia_d').send_keys('No')
    browser.find_element(By.NAME, 'citologia_d').send_keys('No')
    browser.find_element(By.NAME, 'antibiograma_d').send_keys('No')
    browser.find_element(By.NAME, 'diagnostico_definitivo_d').send_keys('Saludable')
    browser.find_element(By.NAME, 'tratamiento_final_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'medicamento_1_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_medicamento_1_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_2_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_medicamento_2_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_3_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_medicamento_3_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_4_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_medicamento_4_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'medicamento_5_d').send_keys('Ninguno')
    browser.find_element(By.NAME, 'posologia_medicamento_5_d').send_keys('Ninguna')
    browser.find_element(By.NAME, 'proxima_cita_d').send_keys('2023-12-01')

@when('hago clic en el botón de crear historia dermatológica')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

@when('hago click en el botón de "OK" en el cuadro de diálogo')
def step_impl(context):
    time.sleep(1)  # Esperar a que aparezca el cuadro de diálogo
    alert = context.browser.switch_to.alert
    alert.accept()

@then('debería ver la página de historia dermatológica creada con éxito')
def step_impl(context):
    assert 'Historia creada con éxito' in context.browser.page_source
    context.browser.quit()