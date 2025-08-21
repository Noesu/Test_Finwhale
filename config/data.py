from dataclasses import dataclass


BASE_URL = "https://priority.finwhale.ru/"


@dataclass
class Company:
    INN: str = "7713486996"
    NAME: str = 'АО "77"'
    ADDRESS: str = "г Москва, Кутузовский пр-кт, д 35, кв 160"
    SEGMENT: str = "Интернет-магазин"

    USER_FIRST_NAME: str = "Иван"
    USER_MIDDLE_NAME: str = "Иванович"
    USER_LAST_NAME: str = "Иванов"
    USER_PHONE: str = "+79999999999"
    USER_EMAIL: str = "widgfxl@shitmail.me"
    USER_CURATOR: str = "STparts.ru"
