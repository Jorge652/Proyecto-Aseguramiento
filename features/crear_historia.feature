Feature: Crear Historia Clínica

    @crear_historia
    Scenario: Crear una nueva historia clínica
        Given que estoy en la página de nueva historia clinica general
        When ingreso los datos de la historia clínica
        And hago clic en el botón de crear historia
        And hago click en el botón de "OK" en el cuadro de diálogo que dice "Cédula correcta"
        Then debería ver la página de historia creada con éxito