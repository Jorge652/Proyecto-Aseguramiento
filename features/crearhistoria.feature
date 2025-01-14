Feature: Crear una nueva historia clínica

    Scenario: Crear una nueva historia clínica con datos válidos
        Given que estoy en la página de creación de una nueva historia clínica
        When completo el formulario con los datos requeridos
        And envío el formulario
        Then debería ser redirigido a la página de confirmación
        And debería ver el mensaje "Historia creada con éxito"