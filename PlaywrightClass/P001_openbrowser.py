from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())
    input('press enter')
    
    # browser.close()

# with sync_playwright() as p:
#     browser = p.chromium.launch(channel="msedge",headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     print(page.title())
#     # input('press enter')
    # browser.close()


# with sync_playwright() as p:
#     browser = p.firefox.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     print(page.title())
#     browser.close()


#This one is for safari browser
# with sync_playwright() as p:
#     browser = p.webkit.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     print(page.title())
#     browser.close()






