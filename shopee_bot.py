"""
Script Autor By p4mbud1
"""
import datetime
from os import error
import selenium
import undetected_chromedriver as UC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

## URL PIN And LINK and Options
global url, pin, link
url_shopee      = "https://shopee.co.id/"
pin             = "245690"
url_product     = "https://shopee.co.id/PUFF-SPONS-SILIKON-WARNA-WARNI-SPON-SILIKON-GAMBAR-SPONS-SILIKON-VARIASI-i.4226907.954955909?__hybrid_pc__=1&stm_referrer="
cookie          = "dE9PTkRMQkMweEJkTUwxVlSWav4IUUX09gsX5uII7Oyu6CRDnx2ViOt6cEMyw5UWhO7UbYwXb0jStCGw0yKa5+bh7qXUaTONNspKo3bWjawE0uAtuxp5tLHyOxsqN2M6CGbX0tq/QetcngG91ptgNA=="

## Seting 
UC.TARGET_VERSION = 92
options     = UC.ChromeOptions()
options.headless = True
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,'plugins': 2, 'popups': 2, 'geolocation': 2,'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,'durable_storage': 2}}
options.add_experimental_option("prefs", prefs)
browser = UC.Chrome(options=options)

def buy_product():
    try:
        print ("-> Request To Buy")
        buy     = WebDriverWait(browser, 0.5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", buy)
        print ("-> -> Product added to cart")

        #checkout    = EC.element_to_be_clickable((By.XPATH, ''))

    except NoSuchElementException as error:
        print ("Error While Buy")

def main():
    # # Setting Cookies
    browser.get(url_shopee)
    browser.add_cookie({'name': 'SPC_EC', 'value':cookie})
    browser.get_cookies()

    # # Seting Link 
    browser.get(url_product)
    print ("Seting is Complate")

    # Seting Time
    flas_sale_time      = datetime.datetime(2021, 7, 21, 20,30,00,)
    time_now            = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    """
    while str(time_now) != str(flas_sale_time) :
        #print ("Belum Sama")
        time_now            = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if time_now != flas_sale_time:
            print(str(flas_sale_time) + " " + str(time_now))
        else:
            exit
    """
    buy_product()

if __name__ == '__main__':
    main()





