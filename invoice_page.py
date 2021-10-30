import os
import calendar
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, datetime

driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())
# for Windows users:
# PATH = '/Users/your_user/chromedriver_folder/chromedriver'
# driver = webdriver.Chrome(PATH)
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdiZ8JjRcmk49ehcimGXQY2ULaK7wPM5IwU4vWRsCw3M2EQvA/viewform'
invoice_date = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
address = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
entity_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
address = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
email_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
next_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
start_date_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
end_date_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
select_services_type = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]'
salary_input = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
add_more_items_yes = '//*[@id="i35"]/div[3]/div'
add_more_items_no = '//*[@id="i38"]/div[3]'
next_button_2 = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span'
additional_info = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'

def wait_for_clickable(element) -> None:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, element)))

def get_first_day_of_current_month() -> datetime:
    first_day_of_current_month = datetime.now().replace(day=1).strftime("%d/%m/%Y")
    return first_day_of_current_month

def get_last_day_of_current_month() -> datetime:
    year = int(datetime.now().strftime('%Y'))
    month = int(datetime.now().strftime('%m'))
    days_in_current_month = calendar.monthrange(year, month)
    end_of_current_month = datetime.now().replace(day=days_in_current_month[1]).strftime("%d/%m/%Y")
    return end_of_current_month
