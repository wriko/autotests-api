import logging




def get_logger(name: str) -> logging.Logger:  # функция для создания логгера
    logger = logging.getLogger(name)  # создание логгера c указанным именем
    logger.setLevel(logging.DEBUG)  # установка минимального уровня логирования для логгера. logging.DEBUG — это самый низкий уровень (0), означающий, что будут выводиться все сообщения: DEBUG, INFO, WARNING, ERROR, CRITICAL.

    handler = logging.StreamHandler()  # создание обработчика, который будет выводить сообщения в консоль
    handler.setLevel(logging.DEBUG)  # минимальный уровень логирования для обработчика

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s')  # создание форматтера, который определяет, как должны выглядеть строки логов.
    handler.setFormatter(formatter)  # Применяет созданный форматтер к обработчику логов.

    logger.addHandler(handler)  # добавление обработчика к логгеру

    return logger  # возвращает созданный логгер

"""
Теперь, при вызове методов logger.debug(), logger.info() и т.д., 
логи будут отправляться в указанный обработчик (в данном случае — в консоль) в заданном формате.
"""

# logger = get_logger("test")
# logger.info("123")