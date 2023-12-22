import json
import sys
import time

from selenium.webdriver import ActionChains, Chrome
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


def login_to_facebook(driver: Chrome, config: dict) -> None:
    username = config["username"]
    password = config["password"]

    driver.get("https://www.facebook.com/")

    login_username = driver.find_element(By.ID, "email")
    login_password = driver.find_element(By.ID, "pass")
    login_username.send_keys(username)
    login_password.send_keys(password)

    login_password.send_keys(Keys.ENTER)
    time.sleep(TIMEOUT_SHORT)


def go_to_chat(driver: Chrome, config: dict) -> None:
    chat_url = config["chat_url"]
    driver.get(chat_url)
    time.sleep(TIMEOUT_SHORT)


def get_friendly_reminder(
    reminder_file_path: str = "./reminder.txt",
) -> list[str]:
    with open(reminder_file_path) as fp:
        return [line.strip("\n") for line in fp]


def send_friendly_reminders(
    driver: Chrome,
    n: int,
    reminder_file_path: str = "./reminder.txt",
) -> None:
    reminder = get_friendly_reminder(reminder_file_path)
    chat_box = driver.find_element(
        By.CSS_SELECTOR, "div[aria-label='Message']"
    )
    for _ in range(n):
        for index, line in enumerate(reminder):
            chat_box.send_keys(line)
            if index == len(reminder) - 1:
                chat_box.send_keys(Keys.ENTER)
                """
                driver.find_element(
                    By.CSS_SELECTOR, "div[aria-label='Press enter to send']"
                ).click()
                """
            else:
                ActionChains(driver).key_down(Keys.SHIFT).key_down(
                    Keys.ENTER
                ).perform()
            # Might not need to sleep, depending on PC specs.
            time.sleep(TIMEOUT_SHORT)


if __name__ == "__main__":
    if len(sys.argv) != 2 and not sys.argv[1].isnumeric():
        print("Usage: python3 friendly_reminder.py [n]")
        exit(1)

    chrome_options = create_options()

    driver = Chrome(options=chrome_options)

    config = get_config()

    login_to_facebook(driver, config)

    go_to_chat(driver, config)

    send_friendly_reminders(driver, int(sys.argv[1]))
