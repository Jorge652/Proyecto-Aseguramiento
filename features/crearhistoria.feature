Feature: Suma de dos números
  Como un usuario
  Quiero sumar dos números
  Para verificar que el resultado sea correcto

  Scenario: Sumar dos números positivos
    Given tengo los números 3 y 5
    When los sumo
    Then el resultado debe ser 8