import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


CHECK_INTERVAL = 10* 60  

# university login page
LOGIN_URL = "https://access.um.ac.ir/login?34de4b52789e3c93"

# A website used only to test whether real Internet access exists
CHECK_URL = "https://www.coursera.org/"

USERNAME = os.environ.get("UM_USERNAME")
PASSWORD = os.environ.get("UM_PASSWORD")


# ============================================================
# INTERNET CHECK
# ============================================================

def internet_is_available():
    """
    Returns True if we have normal Internet access.
    Returns False if the university captive portal intercepts
    the request or there is no Internet.
    """

    try:
        response = requests.get(
            CHECK_URL,
            timeout=8,
            allow_redirects=True
        )

        final_url = response.url.lower()

        # If we were redirected to the university login page,
        # we are not authenticated.
        if "access.um.ac.ir" in final_url:
            return False

        # Normal HTTP response means Internet is available.
        if response.status_code == 200:
            return True

        return False

    except requests.RequestException:
        return False



def create_browser():

    options = webdriver.ChromeOptions()

    # Run Chrome in background
    options.add_argument("--headless=new")

    # Recommended for stable background execution
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Optional: reduce unnecessary browser output
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    return driver



def login(driver):

    print("\nOpening university login page...")

    try:
        driver.get(LOGIN_URL)

        time.sleep(2)

    except WebDriverException as e:

        print("Could not open login page.")
        print(e)

        return False



    inputs = driver.find_elements(By.TAG_NAME, "input")

    username_box = None
    password_box = None

    for element in inputs:

        input_type = element.get_attribute("type")

        if input_type == "password":
            password_box = element

        elif input_type in ["text", "number"]:

            if username_box is None:
                username_box = element


    if username_box is None:

        print("Could not find username field.")

        return False


    if password_box is None:

        print("Could not find password field.")

        return False


    print("Entering username...")

    username_box.clear()
    username_box.send_keys(USERNAME)

    print("Entering password...")

    password_box.clear()
    password_box.send_keys(PASSWORD)


    print("Submitting login...")

    password_box.send_keys(Keys.ENTER)

    # Give university server time to authenticate.
    time.sleep(5)



    print("Checking connection after login...")

    if internet_is_available():

        print("✓ Successfully authenticated.")

        return True

    else:

        print("✗ Authentication appears to have failed.")

        return False

def main():

    if not USERNAME or not PASSWORD:

        print("ERROR:")
        print("UM_USERNAME and UM_PASSWORD are not configured.")
        print()
        print("Set them before running the program.")

        return


    print("======================================")
    print(" University Internet Auto Login")
    print(" Ferdowsi University")
    print("======================================")
    print()
    print("Checking Internet every 10 minutes.")
    print()


    driver = create_browser()


    try:

        while True:

            print("--------------------------------------")

            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{current_time}] Checking Internet...")

            if internet_is_available():

                print("✓ Internet is working.")

            else:

                print("✗ Internet is unavailable.")
                print("→ Attempting to authenticate...")

                success = login(driver)

                if success:

                    print("✓ Re-authentication successful.")

                else:

                    print("✗ Re-authentication failed.")
                    print("Will try again in 10 minutes.")

            print("Next check in 10 minutes.")

            time.sleep(CHECK_INTERVAL)


    except KeyboardInterrupt:

        print("\nProgram stopped by user.")


    finally:

        driver.quit()

if __name__ == "__main__":
    main()