from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Opening browser')
def open_browser(context):
    context.driver =  webdriver.Chrome()


@when("Providing url in browser")
def provide_url(context):
    context.driver.get("https://www.google.com")


@then("Verify title of the Google page")
def verify_title(context):
    assert context.driver.title == "Google"