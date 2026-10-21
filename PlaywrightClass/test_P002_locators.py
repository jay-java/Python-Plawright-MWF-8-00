import re
import time
from playwright.sync_api import Page,expect

def test_locators(page : Page):
   page.goto("https://demo.nopcommerce.com/")
   page.wait_for_timeout(3000)

   # get_by_alt_text()
   logo = page.get_by_alt_text("nopCommerce demo store")
   expect(logo).to_be_visible()

   # get_by_text()
   expect(page.get_by_text("Welcome to our store")).to_be_visible() #full text
   expect(page.get_by_text("Welcome to ")).to_be_visible() # partial text
   expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() #regular expresssion


   #get_by_Role()
   page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
   expect(page.get_by_role("heading",name="Register")).to_be_visible()


   #get_by_ label()
   page.get_by_label("First name:").fill("python")
   page.get_by_label("Last name:").fill("playwright")
   page.get_by_label("Email:").fill("python@gmail.com")
   page.wait_for_timeout(5000)

   #get_by_placeholder()
   page.get_by_placeholder("Search store").fill("mobile phones")
   page.wait_for_timeout(5000)


   #get_by_title()
   #https://testautomationpractice.blogspot.com/p/playwrightpractice.html
   page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
   expect(page.get_by_title("Home page link")).to_have_text("Home")
   expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
   page.wait_for_timeout(5000)


   #get_by_test_Id()
   expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
   expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")





   # expect(page.get_by_alt_text("nopCommerce demo store")).to_be_visible()
