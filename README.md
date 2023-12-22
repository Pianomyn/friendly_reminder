A Selenium script that will send one (or more than one) "friendly reminder(s)" to a Facebook group.

Made one night as a joke, cleaned and now stored on Github for reference.

# WSL Setup (Assumes Python is already installed)
- Install google-chrome binary file (Linux) and save it to `usr/bin`.
    - [Link](https://chromedriver.chromium.org/downloads)
    - Can check by running `google-chrome --version`
- Download the chromedriver binary file (Linux) and save it to `usr/bin/`.
    - Can check by running `chromedriver --version`
- Install `selenium` with pip.
- Make sure `usr/bin` is in PATH.

As of 23/12/23, these instructions worked for me.
[Guide](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)
[WebDriver Download](https://chromedriver.chromium.org/downloads)

# Usage
1. Create a config.json in the root directory.
This config.json should be in the format
``` json
{
    "username": ""
    "password": ""
    "char_url": ""
}
```
2. Create a reminder.txt file with the reminder you want to send.
3. Run python3 [n]
    - Where n is the number of reminders to send

# TODO
- Standardise setup with docker images?
