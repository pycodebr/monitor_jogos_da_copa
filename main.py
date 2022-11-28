import sys
import requests
from time import sleep
from datetime import datetime


def get_match_data():
    return requests.get(
        url='https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-28-11-2022-brasilxsuica.json'
    ).json()


def show_history():
    match_data = get_match_data()
    narrations = match_data['match']['narrations']
    narrations.pop()
    for narration in narrations:
        last_narration_moment = narration['moment']
        last_narration_text = narration['text']
        message = '.\n.\n.\n'
        message += f'{last_narration_moment} minutos - ' if last_narration_moment else ''
        message += last_narration_text
        print(message)


if sys.argv[1] == 'history':
    show_history()

last_update = None
while True:
    match_data = get_match_data()

    narrations = match_data['match']['narrations']
    last_narration = narrations[len(narrations)-1]
    last_narration_time = datetime.strptime(last_narration['created_at'], '%Y-%m-%dT%H:%M:%S.000000Z')

    if (not last_update) or (last_narration_time > last_update):
        last_update = last_narration_time
        last_narration_moment = narrations[len(narrations)-1]['moment']
        last_narration_text = narrations[len(narrations)-1]['text']
        message = '.\n.\n.\n'
        message += f'{last_narration_moment} minutos - ' if last_narration_moment else ''
        message += last_narration_text
        print(message)

    sleep(15)
