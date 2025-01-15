Feature: Buscar Historia Clínica Dermatológica

    @buscar_historia_derma
    Scenario: Buscar una historia clínica dermatológica existente
        Given que estoy en la página de búsqueda de historia clínica dermatológica
        When ingreso la cédula del propietario de la historia clínica dermatológica
        And hago clic en el botón de buscar historia dermatológica
        And hago clic en el botón de "OK" en el cuadro de diálogo de la busqueda de historia clínica dermatológica
        Then debería ver los resultados de la búsqueda de historias clínicas dermatológicas