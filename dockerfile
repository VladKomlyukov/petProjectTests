FROM ubuntu:22.04

# Установка Python и pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Устанавливаем рабочую директорию
WORKDIR /api_tests
# Устанавливаем Allure-pytest плагин
RUN pip install allure-pytest

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости 
RUN pip3 install -r requirements.txt
# Создаем директорию для отчетов
RUN mkdir -p /api_tests/test_results

# Команда для запуска тестов
CMD ["pytest", "-s", "-v", "--tb=short", "--alluredir=/api_tests/test_results"]


