Feature: Дилер для игры в 21

  Scenario: : Раздача начальных карт
    Given дилер
    When начинается раунд
    Then дилер берет себе две карты

  Scenario Outline: : Получение итога руки
    Given <hand>
    When дилер суммирует карты
    Then <total> верен

    Examples: Руки
      | hand  | total |
      | 5,7   | 12    |
      | 5,Q   | 15    |
      | Q,Q,A | 21    |
      | Q,A   | 21    |
      | A,A,A | 13    |

  Scenario Outline: : Дилер играет по правилам
    Given рука с итогом <total>
    When дилер определяет свой ход
    Then <play> верен

    Examples: Руки
      | total | play  |
      | 10    | hit   |
      | 15    | hit   |
      | 16    | hit   |
      | 17    | stand |
      | 18    | stand |
      | 19    | stand |
      | 20    | stand |
      | 21    | stand |
      | 22    | stand |

  Scenario: : Дилер всегда может сделать ход
    Given дилер
    When начинается раунд
    Then дилер выбирает ход
