Feature: Buscar Historia Clínica General

    @buscar_historia_derma
    Scenario: Buscar una historia clínica existente
        Given que estoy en la página de búsqueda de historia clínica 
        When ingreso la cédula del propietario de la historia clínica 
        And hago clic en el botón de buscar historia 
        And hago clic en el botón de "OK" en el cuadro de diálogo de la busqueda de historia clínica 
        Then debería ver los resultados de la búsqueda de historias clínicas 
