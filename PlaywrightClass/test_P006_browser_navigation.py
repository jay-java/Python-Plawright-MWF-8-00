from playwright.sync_api import sync_playwright

def test_locator_filtering():

   with sync_playwright() as p:
        browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
        )     
        context = browser.new_context(no_viewport=True)  # or viewport=None
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
        page.go_back()
        page.wait_for_timeout(2000)
        page.go_forward()
        page.wait_for_timeout(2000)
        page.reload()
        page.wait_for_timeout(2000)
        page.pause()

    #    browser.close()

