import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=options)
driver.get('https://adac.theorie24.de/2022-08-v360/')

iframe = driver.find_element(By.CSS_SELECTOR, "body > div > iframe")
driver.switch_to.frame(iframe)

actions = ActionChains(driver)


elem = driver.find_element(By.XPATH, '//*[@id="t24displayAdContainer"]/a')
elem.click()
elem.click()
elem.click()

time.sleep(1)

elem = driver.find_element(By.XPATH, '/html/body/div/div[8]/div[11]/div[2]/div/div[4]/button[1]')
elem.click()

time.sleep(1)

elem.find_element(By.XPATH, '/html/body/div/div[8]/div[14]/div[2]/div[2]/label[1]/input')

actions.send_keys('Fadel')
actions.perform()

actions.send_keys(Keys.TAB)
actions.perform()

actions.send_keys('Hassan')
actions.perform()

actions.send_keys(Keys.TAB)
actions.perform()

actions.send_keys('206624841')
actions.perform()

elem.find_element(By.XPATH, '/html/body/div/div[8]/div[14]/div[2]/div[2]/button[1]').click()

time.sleep(1)

elem.find_element(By.XPATH, '//*[@id="app_SettingsPage_PageFooter_buttonapply"]').click()

time.sleep(1)

elem.find_element(By.XPATH, '//*[@id="app_SettingsPage_PageFooter_buttonapply"]').click()

time.sleep(1)

elem.find_element(By.XPATH, '//*[@id="app_SettingsPage_PageFooter_buttonapply"]').click()

time.sleep(1)

elem.find_element(By.XPATH, '//*[@id="MainMenuContainer_button26"]').click()

cont = False

while not cont:
    print('Select questions to learn and start!')
    answ = input('Type "y" to continue: ')
    if answ == 'y':
        cont = True


result = elem.find_element(By.XPATH, '/html/body/div[1]/div[8]/div[7]/div/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]').text
questionCount = int(re.search(r'\d+', result).group())

print(questionCount)

for x in range(questionCount):
    elem.find_element(By.XPATH,
                      '/html/body/div[1]/div[8]/div[7]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]').click()

    time.sleep(.5)

    elem.find_element(By.XPATH, '//*[@id="app_TestingPage_CoreTestingDisplay_t24btnnext"]').click()

    result = elem.find_element(By.XPATH,
                               '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[3]/div[1]/div[4]/div[2]/span/u').text

    ansList = [False, False, False]

    if result == 'falsch':
        elem1 = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[2]')
        correct1 = str(elem1.value_of_css_property('background'))
        if correct1.__contains__('optquestion_2'):
            print('correct')
            ansList[0] = True
        elif correct1.__contains__('optquestion_1'):
            print('false')
            ansList[0] = False
        elem2 = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/table/tbody/tr/td[2]/div[2]')
        correct2 = str(elem2.value_of_css_property('background'))
        if correct2.__contains__('optquestion_2'):
            print('correct')
            ansList[1] = True
        elif correct2.__contains__('optquestion_1'):
            print('false')
            ansList[1] = False
        elem3 = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[4]/table/tbody/tr/td[2]/div[2]')
        correct3 = str(elem3.value_of_css_property('background'))
        if correct3.__contains__('optquestion_2'):
            print('correct')
            ansList[2] = True
        elif correct3.__contains__('optquestion_1'):
            print('false')
            ansList[2] = False

    elem.find_element(By.XPATH, '//*[@id="app_TestingPage_CoreTestingDisplay_t24btnnext"]').click()

    time.sleep(.5)

    elem.find_element(By.XPATH,
                      '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div[1]/img').click()

    print(ansList)

    if ansList[0] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]').click()
    if ansList[1] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/table/tbody/tr/td[2]/div[1]').click()
    if ansList[2] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[4]/table/tbody/tr/td[2]/div[1]').click()

    elem.find_element(By.XPATH, '//*[@id="app_TestingPage_CoreTestingDisplay_t24btnnext"]').click()

    time.sleep(.5)

    elem.find_element(By.XPATH,
                      '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div[1]/img').click()

    time.sleep(.5)

    if ansList[0] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]').click()
    if ansList[1] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/table/tbody/tr/td[2]/div[1]').click()
    if ansList[2] is True:
        elem.find_element(By.XPATH,
                          '/html/body/div[1]/div[8]/div[7]/div/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[4]/table/tbody/tr/td[2]/div[1]').click()

    elem.find_element(By.XPATH, '//*[@id="app_TestingPage_CoreTestingDisplay_t24btnnext"]').click()

    time.sleep(.5)




