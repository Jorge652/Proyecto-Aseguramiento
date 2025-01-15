Feature: Crear Historia Clínica Dermatológica

    @crear_historia_derma
    Scenario: Crear una nueva historia clínica dermatológica
        Given que estoy en la página de nueva historia clinica dermatológica
        When ingreso los datos de la historia clínica dermatológica
        And hago clic en el botón de crear historia dermatológica
        And hago click en el botón de "OK" en el cuadro de diálogo
        Then debería ver la página de historia dermatológica creada con éxito