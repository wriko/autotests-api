import platform
import sys

from config import settings


# функция, которая будет автоматически создавать файл environment.properties
def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Добавляем информацию о системе
    items.append(f'os_info={platform.system()}, {platform.release()}')
    # Добавляем информацию о версии интерпретатора Python
    items.append(f'python_version={sys.version}')
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties) # Записываем переменные в файл