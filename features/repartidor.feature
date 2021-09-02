Feature: Dealer 21
    Funciones que tiene un repartidor en el juego de 21

Scenario: Repartir 2 Cartas
    Given un repartidor
    When el juego inicia
    Then el repartidor toma dos cartas

Scenario Outline: Conocer el valor de la mano
    Given una mano <mano> 
    When el repartidor sume las cartas
    Then el resultado <valor> sea correcto
    Examples: Manos y valor
        | mano     | valor    |
        | 5, 7     | 12       |
        | A, 10, 5 | 16       |
        | A, A, 3  | 15       |
        | J, K, 8  | 28       |

Scenario Outline: Determinar jugada del repartidor
    Given el valor de la mano <jugador> del jugador y el valor de la mano <repartidor> del repartidor
    When el repartidor determina la jugada
    Then la jugada <jugada> es correcta
    Examples: Valores y jugada
        |  jugador  |   repartidor   | jugada    |
        |    10     |     10         | plantar   |
        |    21     |     10         | jugar     |
        |    18     |     21         | plantar   |
        |    10     |     5          | jugar     |
        |    28     |     10         | plantar   |
        |    21     |     19         | jugar     |
