# Сервис взаимодействия с Ozon Seller API

### Запуск проекта
1. Для создания виртуального окружения введите команду в консоли
```
python -m venv .venv
```
2. Создайте файл .env в корне проекта. Файл .env.example приведен в качестве примера.
Замените переменные CLIENT_ID и API_KEY на личные
3. Используйте команду из Makefile, чтобы скачать необходимые библиотеки
```
run install_requirements
```
4. Выберите нужный метод запроса и вставьте ссылку в переменную method (7 строка в app.py).
##### Список методов:
| Метод запроса  |         Наименование         |        Ожидаемый результат         |
|:------------:  |:----------------------------:|:----------------------------------:|
|      POST      |       /v2/product/list       |   Получение списка товаров         |
|      POST      |    /v2/product/info/list     | Информация о товарах по product_id |
|      POST      | /v1/product/info/description |   Описание товара по product_id    |

5. Используйте команду из Makefile для выгрузки данных из личного кабинета продавца в зависимости от выбранного запроса
```
run get_excel_data
```
После выполнения кода в папке tables отобразится нужный файл с наименованием '<метод>_<дата>.xlsx'