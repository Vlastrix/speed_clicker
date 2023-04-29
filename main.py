from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep

GAME_URL = "https://www.arealme.com/click-speed-test/es/"
seconds = 10

chrome_driver_path = "C:/Chrome WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.get(GAME_URL)

start_button = driver.find_element(By.CLASS_NAME, "progress-button")

sleep(4)

start_button.click()

click_arena = driver.find_element(By.ID, "clickarena")

sleep(2)

while True:
    try:
        click_arena.click()
    except UnexpectedAlertPresentException:
        pass
