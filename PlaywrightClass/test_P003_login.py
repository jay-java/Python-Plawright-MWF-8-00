import re
import time
from playwright.sync_api import Page,expect

def test_locators(page : Page):
   # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   # page.wait_for_timeout(3000)

   # page.get_by_placeholder("Username").fill("Admin")
   # page.get_by_placeholder("Password").fill("admin123")
   # page.wait_for_timeout(5000)
   # page.get_by_role("button",name=" Login ").click()


   page.goto("https://www.saucedemo.com/")
   page.wait_for_timeout(3000)
   
   page.get_by_placeholder("Username").fill("standard_user")
   page.get_by_placeholder("Password").fill("secret_sauce")
   page.wait_for_timeout(5000)
   page.get_by_role("button",name="Login").click()
   page.wait_for_timeout(5000)

