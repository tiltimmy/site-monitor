import requests   #запросы к сайтам
import datetime   #текущее время   

sites = [
    "https://google.com",
    "https://github.com",
    "https://hvdhvfjfjf.com"
]
def save_result(now, site, status, code):
    with open("log.txt", "a") as f:
        f.write(f"{now} | {site} | {status} | {code}\n")

def check_sites(sites):
    for site in sites:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            response = requests.get(site, timeout=5)
            if response.status_code == 200:
                print(f"{site} доступен.")
                save_result(now, site,"ОК" , "200")
            else:
                print(f"{site} недоступен. Код ответа: {response.status_code}")
                save_result(now, site, "ОШИБКА", response.status_code)
        except requests.RequestException as e:
            print(f"{site} недоступен. Ошибка: {e}")
            save_result(now, site, "Ошибка", "Недоступен")


if __name__ == "__main__":
    print(f"Проверка сайтов началась...")
    check_sites(sites)