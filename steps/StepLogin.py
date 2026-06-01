from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import *
from dotenv import load_dotenv
import os

load_dotenv()

WEBSITE_URL = "https://banco-site-rpa-test.vercel.app/"


@given("user is on the login page")
def login_page(context):
    context.driver= webdriver.Chrome()
    context.driver.get(WEBSITE_URL)



@when("user enters valid username and password")
def valid_login(context, username, password):
    

    username = os.getenv("USERNAME_BANK")
    password = os.getenv("PASSWORD_BANK")

    username_field= context.driver.find_element(By.ID, "username")
    password_field= context.driver.find_element(By.ID, "password")

    wait = WebDriverWait(context.driver, 10)
    
    try:
        wait.until(lambda driver: username_field.is_displayed())
        username_field.send_keys(username)

        wait.until(lambda driver: password_field.is_displayed())
        password_field.send_keys(password)
    except Exception as e:
        print(f"Error occurred: {e}")

    btn_enter= context.driver.find_element(By.ID, "btn-login")
    btn_enter.click()


@then("user should be redirected to the dashboard")
def verify_dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        assert context.driver.find_element(By.TAG_NAME, "h2").text== "Lançamento de Transações"
        print(  "Login successful, user is on the dashboard.")
    except Exception as e:
        print(f"Error occurred: {e}")