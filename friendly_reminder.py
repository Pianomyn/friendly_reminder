import json
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Customise accordingly
# TODO: Look into progamatically sequencing actions
TIMEOUT_SHORT = 1
TIMEOUT_LONG = 2


def create_options() -> Options:
    chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")  # Much faster without UI
    return chrome_options


def get_config(config_path: str = "./config.json") -> dict:
    try:
        with open(config_path) as fp:
            config = json.load(fp)
        return config
    except IOError:
        raise IOError(f"{config_path} does not exist")


def login_to_facebook(driver: webdriver.Chrome, config: dict) -> None:
    username = config["username"]
    password = config["password"]

    driver.get("https://www.facebook.com/")

    login_username = driver.find_element(By.ID, "email")
    login_password = driver.find_element(By.ID, "pass")
    login_username.send_keys(username)
    login_password.send_keys(password)

    login_password.send_keys(Keys.ENTER)
    time.sleep(TIMEOUT_SHORT)


def go_to_chat(driver: webdriver.Chrome, config: dict) -> None:
    chat_url = config["chat_url"]
    driver.get(chat_url)
    time.sleep(TIMEOUT_SHORT)


def get_friendly_reminder(
    reminder_file_path: str = "./reminder.txt",
):
    with open(reminder_file_path) as fp:
        return fp.read().replace("\n", "")


def send_friendly_reminders(
    driver: webdriver.Chrome,
    n: int,
    reminder_file_path: str = "./reminder.txt",
):
    reminder = get_friendly_reminder(reminder_file_path)
    chat_box = driver.find_element(
        By.CSS_SELECTOR, "div[aria-label='Message']"
    )
    for _ in range(n):
        chat_box.send_keys(reminder)
        chat_box.send_keys(Keys.ENTER)
        """
        driver.find_element(
            By.CSS_SELECTOR, "div[aria-label='Press enter to send']"
        ).click()
        """
        # time.sleep(TIMEOUT_SHORT)
        # Might not need to sleep, depending on PC specs.


if __name__ == "__main__":
    if len(sys.argv) != 2 and not sys.argv[1].isnumeric():
        print("Usage: python3 friendly_reminder.py [n]")
        exit(1)

    chrome_options = create_options()

    driver = webdriver.Chrome(options=chrome_options)

    config = get_config()

    login_to_facebook(driver, config)

    go_to_chat(driver, config)

    send_friendly_reminders(driver, int(sys.argv[1]))
