Feature: Editar Historia Clínica General

    @editar_historia
    Scenario: Editar el nombre de un medicamento en una historia clínica general
        Given que estoy en la página de edición de la historia clínica general con ID 4
        When cambio el nombre del medicamento 1 a "Nuevo Medicamento"
        And hago clic en el botón de actualizar historia
        Then debería ver la página de historia actualizada con éxito