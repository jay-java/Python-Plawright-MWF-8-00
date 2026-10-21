from playwright.sync_api import Page,expect

def test_handleIframes(page:Page):
   page.goto("https://practice-automation.com/iframes/")
   page.wait_for_timeout(3000)

   top_frame = page.frame_locator("#iframe-1")
   page.wait_for_timeout(3000)

   expect(top_frame.locator("body")).to_contain_text("Playwright")
   page.wait_for_timeout(3000)

   bottom_page = page.frame_locator("#iframe-2")
   page.wait_for_timeout(3000)
   expect(bottom_page.locator("body")).to_contain_text("Selenium")
   page.wait_for_timeout(3000)
