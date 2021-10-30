from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import elements_2
import time
import calendar
import os

# for Windows users:
# PATH = '/Users/your_user/chromedriver_folder/chromedriver'
# driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())
form_page = elements_2
wait = WebDriverWait(driver, 10)
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdiZ8JjRcmk49ehcimGXQY2ULaK7wPM5IwU4vWRsCw3M2EQvA/viewform'
service_type_other = 'Other'
INVOICE_DATE = datetime.now().strftime("%d/%m/%Y")
SERVICE_START_DATE = datetime.now().replace(day=1).strftime("%d/%m/%Y")
NAME = 'PE LAST_NAME FIRST_NAME'
ADDRESS = 'Country, c. City, st. Street, build. Number, fl. Number'
EMAIL = 'example@email.com'
SERVICE_TYPE = 'Choose your service type'
SALARY_AMOUNT = '1000000'
TRANSFER_FEE_AMOUNT = '20'
TRANSFER_FEE_TEXT = 'Transfer fee'

def get_end_of_current_month():
    year = int(datetime.now().strftime('%Y'))
    month = int(datetime.now().strftime('%m'))
    days_in_current_month = calendar.monthrange(year, month)
    end_of_current_month = datetime.now().replace(day=days_in_current_month[1]).strftime("%d/%m/%Y")
    return end_of_current_month

SERVICE_END_DATE = get_end_of_current_month()

def submit_invoice(add_transfer_fee: bool = True):
    driver.get(url)
    driver.fullscreen_window()
    invoice_date = driver.find_element_by_xpath(form_page.invoice_date)
    invoice_date.send_keys(INVOICE_DATE)
    entity_name = driver.find_element_by_xpath(form_page.entity_name)
    entity_name.send_keys(NAME)
    address = driver.find_element_by_xpath(form_page.address)
    address.send_keys(ADDRESS)
    email_field = driver.find_element_by_xpath(form_page.email_field)
    email_field.send_keys(EMAIL)
    next_button = driver.find_element_by_xpath(form_page.next_button)
    next_button.click()
    driver.fullscreen_window()

    # 1st invoice item
    wait.until(EC.element_to_be_clickable((By.XPATH, form_page.next_button_2)))
    start_date_field = driver.find_element_by_xpath(form_page.start_date_field)
    start_date_field.send_keys(SERVICE_START_DATE)
    end_date_field = driver.find_element_by_xpath(form_page.end_date_field)
    end_date_field.send_keys(SERVICE_END_DATE)
    select_services_type = driver.find_element_by_xpath(form_page.select_services_type)
    select_services_type.send_keys(SERVICE_TYPE)
    salary_input = driver.find_element_by_xpath(form_page.salary_input)
    add_more_items_yes = driver.find_element_by_xpath(form_page.add_more_items_yes)
    next_button_2 = driver.find_element_by_xpath(form_page.next_button_2)
    actions = ActionChains(driver)
    actions.move_to_element(next_button_2).perform()
    salary_input.send_keys(SALARY_AMOUNT)
    add_more_items_yes.click()
    next_button_2.click()
    driver.fullscreen_window()
    if add_transfer_fee:
        # 2nd invoice item - transfer fee
        wait.until(EC.element_to_be_clickable((By.XPATH, form_page.next_button_2)))
        start_date_field = driver.find_element_by_xpath(form_page.start_date_field)
        start_date_field.send_keys(SERVICE_START_DATE)
        end_date_field = driver.find_element_by_xpath(form_page.end_date_field)
        end_date_field.send_keys(SERVICE_END_DATE)
        select_services_type = driver.find_element_by_xpath(form_page.select_services_type)
        select_services_type.send_keys(service_type_other)
        additional_info = driver.find_element_by_xpath(form_page.additional_info)
        additional_info.send_keys(TRANSFER_FEE_TEXT)
        salary_input = driver.find_element_by_xpath(form_page.salary_input)
        add_more_items_no = driver.find_element_by_xpath(form_page.add_more_items_no)
        next_button_2 = driver.find_element_by_xpath(form_page.next_button_2)
        actions = ActionChains(driver)
        actions.move_to_element(next_button_2).perform()
        salary_input.send_keys(TRANSFER_FEE_AMOUNT)
        add_more_items_no.click()
        time.sleep(2)
        next_button_2.click()
        driver.fullscreen_window()
        breakpoint()

submit_invoice()
