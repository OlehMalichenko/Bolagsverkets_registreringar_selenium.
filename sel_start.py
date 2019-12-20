from selenium import webdriver
from time import sleep


def main(date_1, date_2):
    driver = start_driver()
    if driver is None:
        return

    sleep(1)

    if click_sok_kungorelse(driver=driver) is False:
        return

    sleep(2)

    if click_avancerad_sokning(driver=driver) is False:
        return

    sleep(2)

    if write_in_avancerad_sokning(driver=driver, date_1=date_1, date_2=date_2) is False:
        return

    sleep(1.4)

    if click_sok(driver) is False:
        return

    


def start_driver():
    try:
        driver = webdriver.Firefox()
        url = 'https://poit.bolagsverket.se/poit/PublikPoitIn.do'
        driver.get(url)
    except:
        print('Not start driver')
        return None
    else:
        return driver



def click_sok_kungorelse(driver):
    try:
        element = driver.find_element_by_xpath('//a[@id="nav1-2"]')
    except:
        print('Not find element: Sok kungorelse')
        return False
    else:
        element.click()
        return True



def click_avancerad_sokning(driver):
    try:
        element_2 = driver.find_element_by_xpath('//form[@name="SokKungorelseForm"]/div[@style="float: right;"]/a')
    except:
        print('Not find element: Avancerad Sokning')
        return False
    else:
        element_2.click()
        return True



def write_in_avancerad_sokning(driver, date_1, date_2):
    if set_annan_period(driver) is False:
        return False

    if set_date(driver,date_1, date_2) is False:
        return False

    sleep(1)

    if set_amnesomrade(driver) is False:
        return False

    sleep(1.4)

    if set_kungorelserubrik(driver) is False:
        return False

    sleep(1.2)

    if set_underrubrik(driver) is False:
        return False

    return True




def set_annan_period(driver):
    try:
        period = driver.find_element_by_xpath('//select[@id="tidsperiod"]/option[@value="6"]')
    except:
        print('Not find element: Period')
        return False
    else:
        period.click()
        return True



def set_date(driver: webdriver, date_1: str, date_2: str):
    try:
        element_1 = driver.find_element_by_xpath('//input[@id="from"]')
        element_2 = driver.find_element_by_xpath('//input[@id="tom"]')
    except:
        print('Not find element: dates')
        return False
    else:
        element_1.send_keys(date_1)
        sleep(1.5)
        element_2.send_keys(date_2)
        return True



def set_amnesomrade(driver: webdriver):
    try:
        element = driver.find_element_by_xpath('//select[@id="amnesomrade"]/option[contains(text(),"Bolagsverkets registreringar")]')
    except:
        print('Not find element: Bolagsverkets registreringar')
        return False
    else:
        element.click()
        return True


def set_kungorelserubrik(driver: webdriver):
    try:
        element = driver.find_element_by_xpath('//select[@id="kungorelserubrik"]/option[contains(text(),"Aktiebolagsregistret")]')
    except:
        print('Not find element: Aktiebolagsregistret')
        return False
    else:
        element.click()
        return True



def set_underrubrik(driver: webdriver):
    try:
        element = driver.find_element_by_xpath('//select[@id="underrubrik"]/option[contains(text(),"Nyregistreringar")]')
    except:
        print('Not find element: Nyregistreringar')
        return False
    else:
        element.click()
        return True


def click_sok(driver: webdriver):
    try:
        element = driver.find_element_by_xpath('//input[@id="SokKungorelse"]')
    except:
        print('Not find element: SokKungorelse')
        return False
    else:
        element.click()
        return True


if __name__ == '__main__':
    date_1 = '2019-12-02'
    date_2 = '2019-12-10'
    main(date_1=date_1, date_2=date_2)