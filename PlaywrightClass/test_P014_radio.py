from playwright.sync_api import Page,expect

def test_webtable(page:Page):
    page.goto("https://practice-automation.com/form-fields/")
    page.locator("#drink1").check()
    page.locator("#drink2").check()
    page.wait_for_timeout(3000)
    page.locator("#color2").check()

    # page.locator("#picture").fill("C:\Users\topst\Downloads\m1.jpg")
    page.pause()