from playwright.sync_api import sync_playwright

def test_locator_filtering():

   with sync_playwright() as p:
       browser = p.chromium.launch(
       headless=False,
       args=["--start-maximized"]
       )     
       context = browser.new_context(no_viewport=True)  # or viewport=None
       page = context.new_page()

       page.goto("https://www.saucedemo.com/")
       page.wait_for_timeout(5000)
       page.locator("#user-name").fill("standard_user")
       page.locator("#password").fill("secret_sauce")
       page.locator("#login-button").click()

      #  p1 = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
      #  p1.locator("button:has-text('Add to cart')").click()

       p1 = page.locator(".inventory_item").filter(has=page.locator("button.btn_inventory"))
       p1.first.locator("button").click()

       page.pause()

    #    browser.close()

