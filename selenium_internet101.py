import time
from selenium import webdriver
from seleniumwire import webdriver
import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")

phone = '1111111111'
name = 'Автотест'
street = 'Тестовая линия'
dom = '1'


def test_search_example():
    driver.get('https://piter-online.net')

    time.sleep(1)

    search_input = driver.find_element(By.XPATH,
                                       "//input[contains(@datatest, 'main_input_street_home_new')]")

    search_input.clear()
    search_input.send_keys(street)
    time.sleep(5)
    search_input.send_keys("\n")
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "//input[contains(@class, 'app141 app148 app147 app143 app160')]")
    search_input.clear()
    search_input.send_keys(dom)
    time.sleep(5)
    search_input.send_keys("\n")
    time.sleep(5)

    search_input = driver.find_element(By.XPATH, "/html/body/div/div/div[8]/div[1]/div/div/div/ul/li[1]")
    time.sleep(5)
    search_input.click()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "//div[contains(@data-test, 'find_tohome_button')]")
    time.sleep(5)
    search_input.click()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div/div/div/div/div/span")
    time.sleep(5)
    search_input.click()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "/html/body/div/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[2]/div[6]/div/div/div[2]/div[2]/a")
    time.sleep(5)
    search_input.click()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "//input[contains(@name, 'name')]")
    search_input.clear()
    search_input.send_keys(name)
    time.sleep(5)
    search_input.send_keys("\n")
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "//input[contains(@datatest, 'providers_provider_order_input_tel')]")
    search_input.clear()
    search_input.send_keys(phone)
    time.sleep(5)

    search_input = driver.find_element(By.XPATH,
                                       "//div[contains(@data-test, 'order_form_input_connect_button')]")
    search_input.click()
    # search_input.send_keys("\n")
    time.sleep(1)

    driver.save_screenshot('result.png')

    time.sleep(5)

    # params = {"fio": "Автотест", "phone_connection": "71111111111", "need_convergent": "false",
    #           "convergent_tariff_id": "0", "uuid": "c995eb05-d340-4b96-89b6-33de849d41d5", "tariff_id": "102134003"}

    # params = {'convergent_tariff_id': '0', "fio": "Автотест", 'house_id': "4270758",
    #               "lead_form_type": '{"lead_form_type":"click_send_order_with_tariff","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","screenWidth":1280,"screenHeight":1024,"url":"https://piter-online.net/leningradskaya-oblast/orders/home?tariff_id=102134003","from":"TC"}',
    #               "need_convergent": "false", "phone_connection": "71111111111", "region_id": "47", "street_id": "380434",
    #               "tariff_id": "102134003", "uuid": "c995eb05-d340-4b96-89b6-33de849d41d5"}

    # params = {
    #   "fio": "Автотест",
    #   "phone_connection": "71111111111",
    #   "need_convergent": "false",
    #   "convergent_tariff_id": 0,
    #   "region_id": 47,
    #   "lead_form_type": "{\"lead_form_type\":\"click_send_order_with_tariff\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36\",\"screenWidth\":1280,\"screenHeight\":1024,\"url\":\"https://piter-online.net/leningradskaya-oblast/orders/home?tariff_id=102134003\",\"from\":\"TC\"}",
    #   "tariff_id": "102134003",
    #   "uuid": "c995eb05-d340-4b96-89b6-33de849d41d5"
    # }
    #
    # headers = {'authority': 'orders.101internet.ru', "method": "POST", "path": "/api_external/sites/webhook?type=site101-order-home", "scheme": "https"}
    #
    # # forma = requests.get(driver.current_url)
    # # forma = requests.get('https://piter-online.net/leningradskaya-oblast/rates?house_id=4270758')
    #
    # forma = requests.post('https://piter-online.net/leningradskaya-oblast/orders/home?tariff_id=105236004', headers=headers, data=params)
    #
    # print(forma.text)
    # print(forma.status_code)

    # for request in driver.requests[-1]:
    #     if request.response:
    #         print(driver.requests[-1]
    # request.url,
    # request.response.status_code,
    # # request.response.headers['Content-Type']
    # )

    # status = driver.requests[-1].response.status_code
    # assert driver.requests[-1].response.status_code == 200
    print("Status code:")
    print(driver.requests[-1].response.status_code)

    def steps23():
        driver.execute_script("window.history.go(-1)")
        search_input = driver.find_element(By.XPATH,
                                           "/html/body/div/div/div[1]/div[4]/div[4]/div[1]/div/div/div[2]/div[2]/div[6]/div/div/div[2]/div[2]/a")
        time.sleep(5)
        search_input.click()
        time.sleep(5)

        search_input = driver.find_element(By.XPATH,
                                           "//input[contains(@name, 'name')]")
        search_input.clear()
        search_input.send_keys(name)
        time.sleep(5)
        search_input.send_keys("\n")
        time.sleep(5)

        search_input = driver.find_element(By.XPATH,
                                           "//input[contains(@datatest, 'providers_provider_order_input_tel')]")
        search_input.clear()
        search_input.send_keys(phone)
        time.sleep(5)

        search_input = driver.find_element(By.XPATH,
                                           "//div[contains(@data-test, 'order_form_input_connect_button')]")
        search_input.click()
        # search_input.send_keys("\n")
        time.sleep(1)

        driver.save_screenshot('result.png')
        time.sleep(1)
        print("Status code:")
        print(driver.requests[-1].response.status_code)
    steps23()
    steps23()
    steps23()
    steps23()

        # assert driver.requests[-1].response.status_code == 201

    driver.quit()
