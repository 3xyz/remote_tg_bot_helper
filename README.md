# remote_tg_bot_helper
This bot provides simple interface for remote interact with your system.

# Installation

```sh
git clone https://github.com/3xyz/remote_tg_bot_helper.git
cd remote_tg_bot_helper/
pip3 install -r requirements.txt
mv config.ini.example config.ini
ln -s $(pwd)/main.py ~/local/bin/remote_tg_bot_helper
```

Change bot token and telegram ID inside `config.ini`.

Run scipt by `remote_tg_bot_helper`.
