from locators import *
BASE_URL= 'https://qa-scooter.praktikum-services.ru/'
BASE_URL_ORDER ='https://qa-scooter.praktikum-services.ru/order'
USER_DATA = {
    "user_1": {
        "name": "Аида",
        "surname": "Аидовна",
        "metro": "Черизовская",
        "telephone": "777777777766",
        "address": "Москва",
        "date_order": '//div[text()="29"]',
        "order_period": RENT_PERIOD_1,
        "scooter_color": ORDER_CHECKBOX_BLACK,
        "comment": "без комментариев"
    },
    "user_2": {
        "name": "Иван",
        "surname": "Иванов",
        "metro": "Сокольники",
        "telephone": "777777777555",
        "address": "Минск",
        "date_order": '//div[text()="29"]',
        "order_period": RENT_PERIOD_2,
        "scooter_color": ORDER_CHECKBOX_GRAY,
        "comment": "привезти до 12:00"
    }
}
