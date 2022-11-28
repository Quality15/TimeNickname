import requests
from colorama import Back, Fore, Style, init
import datetime
import time
import sys

init()

def changeNickname(token, guild_id, delay, name):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/members/@me' # 487226897487364097 <- Qual
    headers = {'Authorization': f'{token}'}

    while True:
        time_ = datetime.datetime.now().strftime("%H:%M")
        data = {
            "nick": f"[{time_}] {name}"
        }

        r = requests.patch(url, headers=headers, json=data)
        r_name = requests.get(url, headers=headers)

        if r.status_code == 200:
            print(f'{Fore.GREEN} Change nickname - {r.status_code}\n\t{data}\n')
        else:
            print(f'{Fore.RED} Change nickname - {r.status_code}\n{r.text}\n')

        time.sleep(delay)

if __name__ == '__main__':
    TOKEN = open("token.txt", 'r').read()
    if len(TOKEN) < 2:
        TOKEN = input("Enter account token: ")
    guild = open("guild.txt", 'r').read()
    if len(guild) < 2:
        guild = input("Enter guild id: ")
    delay = int(input("Enter delay (seconds) between nick change: "))
    # if delay < 30:
    #     sys.exit("Delay must be greater than 30 seconds")
    name = input("Enter name (optional): ")
    if name == '':
        g_url = f'https://discord.com/api/v9/users/@me'
        headers = {'Authorization': f'{TOKEN}'}
        r_name = requests.get(g_url, headers=headers)
        name = r_name.json()["username"]
        changeNickname(TOKEN, guild, delay, name)
    else:
        changeNickname(TOKEN, guild, delay, name)