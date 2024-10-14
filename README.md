
![Logo](https://i.imgur.com/ke6U3pb.png)


# EPIC RPG Macro

A proof of concept macro for `EPIC RPG`. 

Note: Crazymagicians assumes no responsibility for any consequences arising from the use of the Epic RPG Macro. Additionally, they disclaim any liability for any damage caused by its use. The Epic RPG Macro is a proof of concept developed for educational purposes, and its usage is at the discretion of the user.

## Features

- Does hunts, adventures, training, work commands, farming, daily, weekly, heal and random events

- Runs completly in the background without requiring to open the discord window/tab

- Alerts you during epic guard(captcha) events

- Shows stats of every session


## Installation

**Python 3.9 or higher is required**

* Install the dependencies
```bash
# Linux/macOS
python3 -m pip install -U discord.py-self
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
py -3 -m pip install -U discord.py-self
```

* Complete `options.ini`
replace the text withing [] (including '[' and ']') with the appropriate options. Make sure there is no space in either sides of '='

for example : [carrot or potato or bread or none] -----> carrot

* Reminder bot setup
Invite the Navi Lite bot to you server.
[Invite Link](https://discord.com/application-directory/1213487623688167494)

Use the `navi sm` command and set all reminder messages to their simplest form. i.e 

hunt

adventrue

daily

weekly

lootbox

training

quest

farm

work

Use the `navi sh` command and make sure Heal warning, Ruby counter, Training helper are all enabled, change ruby counter style to `Text`, Trainer helper style to `Text` and Ping mode to `Before`

Use the `navi srm` command and make sure all reminders are `Enabled` and DND mode `Disabled`. Change Slash commands in reminders to `Disabled`

* Run the script
    
## Contact

For concerns, feedback, or requests, contact  crazymagicians420@proton.me


## Links
[Discord-self.py](https://github.com/dolfies/discord.py-self)

[Discord.py](https://github.com/Rapptz/discord.py)

## License

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache_2.0-green)](https://choosealicense.com/licenses/apache-2.0/)

