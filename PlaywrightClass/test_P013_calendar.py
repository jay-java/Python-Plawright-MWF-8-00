from playwright.sync_api import Page,expect

def test_webtable(page:Page):
    expected_year = "2024"
    expected_day="20"
    expected_hour ="9"
    expected_minute ="30"
    expected_AMPM = "PM"
    page.goto("https://www.automationtesting.co.uk/datepicker.html/")
    page.wait_for_timeout(3000)
    date_picker = page.locator("#basicDate")
    date_picker.click()
    page.wait_for_timeout(3000)
    next_month = page.locator(".flatpickr-next-month")
    next_month.click()
    year_input = page.locator(".numInput.cur-year").first
    year_input.click()
    year_input.type(expected_year)
    page.wait_for_timeout(3000)
    page.locator(
        f"//span[contains(@class,'flatpickr-day') and text()= '{expected_day}']"
    ).first.click()
    page.wait_for_timeout(3000)
    hour_input = page.locator(".flatpickr-hour").first
    hour_input.click()
    hour_input.press("Control+A")
    hour_input.type(expected_hour)
    page.wait_for_timeout(3000)

    minute_input = page.locator(".flatpickr-minute").first
    minute_input.click()
    minute_input.press("Control+A")
    minute_input.type(expected_minute)
    page.wait_for_timeout(3000)

    am_pm  = page.locator(".flatpickr-am-pm").first
    current_value = am_pm.text_content()

    if current_value != expected_AMPM:
        am_pm.click()

    page.wait_for_timeout(3000)

    selected_value = date_picker.input_value()
    print("selected date time : ",selected_value)
    assert expected_year in selected_value
    assert expected_day in selected_value
    assert "9:30" in selected_value
    expect(date_picker).not_to_be_empty()

