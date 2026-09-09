from playwright.sync_api import Page,expect
def test_css_xpath(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #css seletor
    # page.locator("input[placeholder='Username']").fill("Admin")
    # page.locator("input[placeholder='Password']").fill("admin123")
    # page.locator("button[type='submit']").click()
    #xpath
    page.locator("//input[@placeholder='Username']").fill("Admin")
    page.locator("//input[@placeholder='Password']").fill("admin123")
    page.locator("//button[normalize-space()='Login']").click()
    page.pause()
