# Description
A Selenium script that will send one (or more than one) "friendly reminder(s)" to a Facebook group chat.

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
<br/>
[WebDriver Download](https://chromedriver.chromium.org/downloads)

# Usage
1. Create a config.json in the root directory.
This config.json should be in the format
``` json
{
    "username": ""
    "password": ""
    "chat_url": ""
}
```
Eg
``` json
{
    "username": "fakeemail@gmail.com"
    "password": "fJvy28a33M"
    "chat_url": "https://www.facebook.com/messages/t/1"
}
```

2. Create a reminder.txt file with the reminder you want to send.
3. Run `python3 friendly_reminder.py [n]`
    - Where n is the number of reminders to send

# TODO
- Standardise setup with docker images?
- Sequence actions in Selenium programatically.
