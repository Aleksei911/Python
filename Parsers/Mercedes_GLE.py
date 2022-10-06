import random
import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json

url = "https://auto.ru/cars/mercedes/gle_klasse_coupe_amg/all/"
user = UserAgent().random

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": """suid=594a0ea770784dae47b5d0a52b69fc6a.00fc352c52db97a8ef0cf3ab8a343911; autoru_sid=a%3Ag633d63e52hp5rdj37v8l1tee8qhg0at.ab4237f257ded5d43d2e650e9a21dcd9%7C1664967653590.604800.EjxSMC3k-RxlX_9C-v34AA.rAoBSE-adfJfCMzipQwJ19z2J65MbJhVCDOF1aANVrQ; autoruuid=g633d63e52hp5rdj37v8l1tee8qhg0at.ab4237f257ded5d43d2e650e9a21dcd9; autoru_gdpr=1; yuidlt=1; yandexuid=8771909861632904379; crookie=tX4r5lcWA3PluP2tnLujv1nrKQFi4ckBIS2n6RbofAQgI0tmoAZGLQOU9e0YiNK3x5b1NNjIoIFr47XW0y4ObTETqKw=; cmtchd=MTY2NDk2NzY2MjQ3Nw==; gdpr=0; _ym_uid=1664967665900790393; yandex_login=BiznesPokypka; i=dp7yWxk2p/G4aFwyNu2kVsyzBtd69o+Tv9Fl4gPZjtVI7pMiYyMEySDJscSfixf9wAFo25wGa/3aTCLIcCsUyG5J7rg=; los=1; _csrf_token=1b842195b136e1cfcc111d5d5cfc8bf46b813b1a10b8df50; from=direct; Session_id=3:1665049284.5.0.1661875882622:YeP8Vw:85.1.2:1|751477880.0.2|61:10007914.773459.kvL62T10lnbpYmu-vU8gF08ywcE; ys=udn.cDpCaXpuZXNQb2t5cGth#c_chck.2799693636; mda2_beacon=1665049284069; _ym_isad=1; sso_status=sso.passport.yandex.ru:synchronized; _yasc=y/1yyMHP/8I4aBgl5t4m0gr/UZhQ3da0D/JIZr3NgY7hW647; from_lifetime=1665049430872; _ym_d=1665049505; layout-config={"win_width":1028,"win_height":757}""",
    "Host": "auto.ru",
    "User-Agent": user
}

cars_data_list = []

iteration_count = 5

for i in range(1, 5):

    req = requests.get(url + f"?page={i}", headers=header).content.decode("utf-8")

    soup = BeautifulSoup(req, "lxml")

    all_cars = soup.find_all("div", class_="ListingItem")

    for car in all_cars:

        car_link = car.find("div", class_="ListingItem__summary").find("a", class_="Link ListingItemTitle__link").get("href")
        car_name = car.find("div", class_="ListingItem__summary").find("a", class_="Link ListingItemTitle__link").text
        params_auto = car.find("div", class_="ListingItem__summary").find_all("div", class_="ListingItemTechSummaryDesktop__cell")
        try:
            engine = params_auto[0].text
        except Exception:
            engine = "No date for the engine"

        try:
            transmission = params_auto[1].text
        except Exception:
            transmission = "No date for the transmission"

        try:
            car_type = params_auto[2].text
        except Exception:
            car_type = "No date for the car_type"

        try:
            drive = params_auto[3].text
        except Exception:
            drive = "No date for the drive"

        try:
            year = car.find("div", class_="ListingItem__year").text
        except Exception:
            year = "No year"

        try:
            odometer = car.find("div", class_="ListingItem__kmAge").text
        except Exception:
            odometer = "No odometr"

        try:
            price_RUB = car.find("div", class_="ListingItemPrice__content").find("span").text
        except Exception:
            price_RUB = "No price"

        cars_data_list.append(
            {
                "Ссылка на авто": car_link,
                "Название авто": car_name,
                "Тип двигателя": engine.replace(" ", "").replace(" ", ""),
                "Трансмиссия": transmission,
                "Тип авто": car_type,
                "Привод": drive,
                "Год выпуска": year,
                "Пробег": odometer.replace(" ", ","),
                "Цена в российских рублях": price_RUB.replace(" ", ",")
            }
        )

    iteration_count -= 1
    print(f"Итерация № {i} завершена. Осталось {iteration_count} итераций")
    if iteration_count == 0:
        print("Сбор данных завершен")

    time.sleep(random.randrange(2, 4))

with open("cars.json", "a", encoding="utf-8") as file:
    json.dump(cars_data_list, file, indent=4, ensure_ascii=False)

