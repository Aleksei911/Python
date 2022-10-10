import csv
import random
import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json

cours_USD = float(input("Введите курс доллара к российскому рублю: ").replace(",", "."))
cours_BYN = float(input("Введите курс белорусского рубля к российскому рублю: ").replace(",", "."))

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

for i in range(1, 6):

    req = requests.get(url + f"?page={i}", headers=header).content.decode("utf-8")

    soup = BeautifulSoup(req, "lxml")

    all_cars = soup.find_all("div", class_="ListingItem")

    car_urls = []
    for car in all_cars:
        car_url = car.find("div", class_="ListingItem__summary").find("a").get("href")
        car_urls.append(car_url)

    for link in car_urls:
        car_req = requests.get(link, headers=header).content.decode("utf-8")

        car_page = BeautifulSoup(car_req, "lxml")

        try:
            car_name = car_page.find("div", class_="CardHead__topRow").find("h1", class_="CardHead__title").text
        except Exception:
            car_name = "information not found"

        try:
            price = car_page.find("div", class_="CardHead__topRow").find("span",
                                                                         class_="OfferPriceCaption__price").text.replace(
                " ", "").strip("₽")
        except Exception:
            price = "information not found"

        car_info = car_page.find("div", class_="CardOfferBody__leftColumn")

        try:
            year = car_info.find("li", class_="CardInfoRow CardInfoRow_year").find_all("span")
            year_value = year[1].text
        except Exception:
            year_value = "information not found"

        try:
            odometer = car_info.find("li", class_="CardInfoRow CardInfoRow_kmAge").find_all("span")
            odometer_value = odometer[1].text.replace(" ", " ")
        except Exception:
            odometer_value = "information not found"

        try:
            car_type = car_info.find("li", class_="CardInfoRow CardInfoRow_bodytype").find_all("span")
            car_type_value = car_type[1].text
        except Exception:
            car_type_value = "information not found"

        try:
            color = car_info.find("li", class_="CardInfoRow CardInfoRow_color").find_all("span")
            color_value = color[1].text
        except Exception:
            color_value = "information not found"

        try:
            engine = car_info.find("li", class_="CardInfoRow CardInfoRow_engine").find_all("span")
            engine_value = engine[1].text.replace(" ", " ")
        except Exception:
            engine_value = "information not found"

        try:
            transmission = car_info.find("li", class_="CardInfoRow CardInfoRow_transmission").find_all("span")
            transmission_value = transmission[1].text
        except Exception:
            transmission_value = "information not found"

        try:
            drive = car_info.find("li", class_="CardInfoRow CardInfoRow_drive").find_all("span")
            drive_value = drive[1].text
        except Exception:
            drive_value = "information not found"

        try:
            condition = car_info.find("li", class_="CardInfoRow CardInfoRow_state").find_all("span")
            condition_value = condition[1].text
        except Exception:
            condition_value = "information not found"

        try:
            price_RUB = f"{int(price):,}"
        except Exception:
            price_RUB = "information not found"

        try:
            price_BYN = f"{int(int(price) / cours_BYN):,}"
        except Exception:
            price_BYN = "information not found"

        try:
            price_USD = f"{int(int(price) / cours_USD):,}"
        except Exception:
            price_USD = "information not found"

        cars_data_list.append(
            {
                "Ссылка на авто": link,
                "Название авто": car_name,
                "Год выпуска": year_value,
                "Пробег": odometer_value,
                "Кузов": car_type_value,
                "Цвет": color_value,
                "Двигатель": engine_value,
                "Коробка": transmission_value,
                "Привод": drive_value,
                "Состояние": condition_value,
                "Цена в российских рублях": price_RUB,
                "Цена в белорусских рублях": price_BYN,
                "Цена в долларах": price_USD
            }
        )

    time.sleep(random.randrange(1, 3))

print(len(cars_data_list))

sorted_cars_data_list = sorted(cars_data_list, key=lambda x: x["Цена в долларах"])

with open("cars.json", "w", encoding="utf-8") as file:
    json.dump(sorted_cars_data_list, file, indent=4, ensure_ascii=False)

with open("cars.csv", "w", encoding="cp1251", newline="") as file2:
    keys = sorted_cars_data_list[0].keys()
    writer = csv.DictWriter(file2, keys, delimiter=";")
    writer.writeheader()
    writer.writerows(sorted_cars_data_list)
