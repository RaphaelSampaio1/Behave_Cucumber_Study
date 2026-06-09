from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from behave import *
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

WEBSITE_URL = "https://banco-site-rpa-test.vercel.app/"


@given("user is on the login page")
def login_page(context):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get(WEBSITE_URL)



@when("user enters valid username and password")
def valid_login(context):
    wait = WebDriverWait(context.driver, 10)

    username = os.getenv("USERNAME_BANK")
    password = os.getenv("PASSWORD_BANK")

    username_field = wait.until(lambda driver: driver.find_element(By.ID, "username"))
    password_field = wait.until(lambda driver: driver.find_element(By.ID, "password"))

    username_field.send_keys(username)
    password_field.send_keys(password)

    btn_enter = context.driver.find_element(By.ID, "btn-login")
    btn_enter.click()


@then("user should be redirected to the dashboard")
def verify_dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        assert context.driver.find_element(By.TAG_NAME, "h2").text== "Lançamento de Transações"
        print(  "Login successful, user is on the dashboard.")
    except Exception as e:
        print(f"Error occurred: {e}")



@when(u'user enters "{username}" and "{password}"')
def invalid_login(context, username, password):
    try:
        wait = WebDriverWait(context.driver, 10)

        username_field = wait.until(lambda driver: driver.find_element(By.ID, "username"))
        password_field = wait.until(lambda driver: driver.find_element(By.ID, "password"))

        username_field.send_keys(username)
        password_field.send_keys(password)

        btn_enter = context.driver.find_element(By.ID, "btn-login")
        btn_enter.click()
    except Exception as e:
        print(f"Error occurred: {e}")


@then("user should see an error message")
def verify_error_message(context):
    wait = WebDriverWait(context.driver, 10)
    message = wait.until(lambda driver: driver.find_element(By.ID, "login-error"))
    wait.until(lambda driver: driver.find_element(By.ID, "login-error").is_displayed())
    assert message.text == "Senha inválida."
    
