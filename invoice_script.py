from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import invoice_page
import time

form_page = invoice_page
driver = form_page.driver
today_date = datetime.now().strftime("%d/%m/%Y")
SERVICE_TYPE_OTHER = 'Other'
INVOICE_DATE = today_date
SERVICE_START_DATE = form_page.get_first_day_of_current_month()
SERVICE_END_DATE = form_page.get_last_day_of_current_month()
NAME = 'PE LAST_NAME FIRST_NAME'
ADDRESS = 'Country, c. City, st. Street, build. Number, fl. Number'
EMAIL = 'example@email.com'
SERVICE_TYPE = 'Choose your service type'
SALARY_AMOUNT = '1000000'
TRANSFER_FEE_AMOUNT = '20'
TRANSFER_FEE_TEXT = 'Transfer fee'

def submit_invoice(add_transfer_fee: bool = True) -> None:
    driver.get(form_page.url)
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
    form_page.wait_for_clickable(form_page.next_button_2)
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
        form_page.wait_for_clickable(form_page.next_button_2)
        start_date_field = driver.find_element_by_xpath(form_page.start_date_field)
        start_date_field.send_keys(SERVICE_START_DATE)
        end_date_field = driver.find_element_by_xpath(form_page.end_date_field)
        end_date_field.send_keys(SERVICE_END_DATE)
        select_services_type = driver.find_element_by_xpath(form_page.select_services_type)
        select_services_type.send_keys(SERVICE_TYPE_OTHER)
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
        # this script doesn't hit the [Submit] button
        # for you to verify the data
        breakpoint()

submit_invoice()
