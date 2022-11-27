import requests
import datetime
import time
import sys

def changeNickname(token, guild_id, delay):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/members/@me' # 487226897487364097 <- Qual
    headers = {'Authorization': f'{token}'}

    g_url = f'https://discord.com/api/v9/users/@me'
    r_name = requests.get(g_url, headers=headers)
    name = r_name.json()["username"]

    while True:
        time_ = datetime.datetime.now().strftime("%H:%M")
        data = {
            "nick": f"[{time_}] {name}"
        }

        r = requests.patch(url, headers=headers, json=data)
        r_name = requests.get(url, headers=headers)

        print(f'Change nickname - {r.status_code}\n{r.text}\n\t{data}\n')

        time.sleep(delay)

if __name__ == '__main__':
    TOKEN = open("token.txt", 'r').read()
    if len(TOKEN) < 2:
        TOKEN = input("Enter account token: ")
    guild = open("guild.txt", 'r').read()
    if len(guild) < 2:
        guild = input("Enter guild id: ")
    delay = int(input("Enter delay (seconds) between nick change: "))
    if delay < 60:
        sys.exit("Delay must be greater than 60 seconds")
    else:
        changeNickname(TOKEN, guild, delay)