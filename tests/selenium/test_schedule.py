from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date

def test_schedule_waste_pickup():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/home")
    wait = WebDriverWait(driver, 10)

    # Fill in Full Name
    name_input = wait.until(EC.presence_of_element_located((By.ID, "home-name")))
    name_input.send_keys("John Doe")
    time.sleep(1)

    # Fill in Email
    email_input = driver.find_element(By.ID, "home-email")
    email_input.send_keys("john.doe@example.com")
    time.sleep(1)

    # Select Location
    location_select = Select(driver.find_element(By.ID, "home-location"))
    location_select.select_by_visible_text("Nairobi")
    time.sleep(1)

    # Select Waste Type
    waste_select = Select(driver.find_element(By.ID, "home-waste"))
    waste_select.select_by_visible_text("General Waste")
    time.sleep(1)

    # Pick a Date (today for example)
    date_input = driver.find_element(By.ID, "home-date")
    today = date.today().isoformat()  # format: YYYY-MM-DD
    date_input.send_keys(today)
    time.sleep(1)

    # Add Additional Details
    desc_area = driver.find_element(By.ID, "home-desc")
    desc_area.send_keys("Please pick it up before 10 AM.")
    time.sleep(1)

    # Submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "home-btn")
    submit_button.click()
    time.sleep(2)

    # Assert success message or check expected result
    assert "thank you" in driver.page_source.lower() or "request submitted" in driver.page_source.lower()

    driver.quit()

if __name__ == "__main__":
    test_schedule_waste_pickup()
