Feature: Mostrar Todas las Historias Disponibles

    @mostrar_historias
    Scenario: Ver todas las historias clínicas disponibles
        Given que estoy en la página de inicio
        When hago clic en el botón de "Mostrar Todas las Historias Disponibles"
        Then debería ver la página con todas las historias clínicas disponibles