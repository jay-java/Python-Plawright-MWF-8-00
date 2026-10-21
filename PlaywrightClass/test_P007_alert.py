from playwright.sync_api import Page,expect

def test_handleAlert(page:Page):
  
   #1.alert
#    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
#    page.wait_for_timeout(3000)
#    page.once("dialog",lambda dialog:dialog.accept())
#    page.wait_for_timeout(3000)
#    page.get_by_text("Click for JS Alert").click()
#    page.wait_for_timeout(3000)
#    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")


   #2.alert
#    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
#    page.wait_for_timeout(3000)
#    page.once("dialog",lambda dialog:dialog.dismiss())
#    page.wait_for_timeout(3000)
#    page.get_by_text("Click for JS Confirm").click()
#    page.wait_for_timeout(3000)
#    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

   #3.alert
#    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
#    page.wait_for_timeout(3000)
#    page.once("dialog",lambda dialog:dialog.accept("Playwrigth Python Demo"))
#    page.wait_for_timeout(3000)
#    page.get_by_text("Click for JS Prompt").click()
#    page.wait_for_timeout(3000)
#    expect(page.locator("#result")).to_have_text("You entered: Playwrigth Python Demo")
