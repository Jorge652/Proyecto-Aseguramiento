Feature: Editar Historia Clínica Dermatológica

    @editar_historia_derma
    Scenario: Editar el nombre de un medicamento en una historia clínica dermatológica
        Given que estoy en la página de edición de la historia clínica dermatológica con ID 1
        When cambio el nombre del medicamento 1 a "Nuevo Medicamento Dermatológico"
        And hago clic en el botón de actualizar historia
        Then debería ver la página de historia actualizada con éxito