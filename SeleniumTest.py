import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

FORM_URL = "file:///D:/programmingcodes/vspython/U&I/kickstarter25-26/actual.html"

CENTERS = [
    "Devnar", "SG", "Rehmath", "SBG", "Nightingale",
    "Manchikalalu", "Aadarna", "Aman vedika", "DJ", "NA"
]

def fill_form(driver, name, phone, center):
    wait = WebDriverWait(driver, 10)
    driver.get(FORM_URL)  # Load form fresh

    # --- Fill Name ---
    name_input = wait.until(EC.presence_of_element_located((By.ID, "agent")))
    name_input.clear()
    name_input.send_keys(name)

    # --- Fill Phone ---
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.clear()
    phone_input.send_keys(phone)

    # --- Select Center ---
    select_element = Select(driver.find_element(By.ID, "center"))
    select_element.select_by_visible_text(center)

    # --- Submit Button ---
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(0.5)  # small pause
    submit_button.click()

    print(f"Submitted: {name}, {phone}, {center}")


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        for i in range(1, 26):  # 25 people
            # Reload form page each time before filling
            driver.get(FORM_URL)

            name = f"Agent_{i:03d}"
            phone = f"9{random.randint(100000000,999999999)}"
            center = random.choice(CENTERS)

            fill_form(driver, name, phone, center)

            print("⏳ Waiting 10 seconds before next entry...")
            time.sleep(15)

    finally:
        driver.quit()



if __name__ == "__main__":
    main()
