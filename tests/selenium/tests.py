from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clean_city():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:3000")

        # HOME ➜ SIGN UP
        home_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
        )
        home_link.click()

        sign_up_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cta-btn"))
        )
        sign_up_link.click()
        print("✅ Clicked on 'Sign Up'.")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "register-name"))
        )
        driver.find_element(By.ID, "register-name").send_keys("John Doe")
        driver.find_element(By.ID, "register-email").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "register-password").send_keys("SecurePass123")
        print("✅ Filled registration form.")

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "register-btn"))
        )
        register_button.click()
        print("✅ Clicked 'Register'.")

        time.sleep(3)
        print("🌐 Current URL after registration:", driver.current_url)

        # LOGIN
        driver.get("http://localhost:3000/login")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-email"))
        )
        driver.find_element(By.ID, "login-email").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "login-password").send_keys("SecurePass123")
        print("✅ Filled login form.")

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
        )
        login_button.click()
        print("✅ Clicked 'Login'.")

        time.sleep(3)
        print("🌐 Final URL after login:", driver.current_url)

        # EDIT PROFILE
        edit_profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Edit Profile']"))
        )
        edit_profile_button.click()
        print("📝 Clicked 'Edit Profile'.")

        # Wait for name and email inputs
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )

        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.NAME, "email")

        name_input.clear()
        name_input.send_keys("Johnathan Doe")
        time.sleep(1)  # Wait after editing name

        email_input.clear()
        email_input.send_keys("johnathan.doe@example.com")
        print("✅ Edited profile fields.")
        time.sleep(1)  # Wait after editing

        # To Save:
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))
        )
        save_button.click()
        print("✅ Clicked 'Save'.")

        # To Cancel instead (uncomment if needed):
        # cancel_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']"))
        # )
        # cancel_button.click()
        # print("❎ Clicked 'Cancel' instead of saving.")

        time.sleep(3)
                # LOGOUT
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nav-logout"))
        )
        logout_button.click()
        print("🚪 Clicked 'Logout'.")

        time.sleep(2)  # Wait after logout

    except Exception as e:
        print("❌ Error occurred:", e)
    finally:
        driver.quit()

clean_city()
