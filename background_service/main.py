import json
import time
from pathlib import Path

import requests

api_url = 'http://127.0.0.1:8000/api/data/'


def fetch_logs(api_url):
    """Функция для отправки GET запроса"""
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def save_to_file(logs, file_path):
    """ Функция для сохранения результатов в файл"""
    with open(file_path, 'a') as file:
        for log in logs:
            file.write(json.dumps(log) + '\n')


def main(api_url, file_path, interval_seconds=60):
    while True:
        try:
            logs = fetch_logs(api_url)
            save_to_file(logs, file_path)
            print(f"Logs saved at {file_path}")
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(interval_seconds)


if __name__ == "__main__":
    file_path = Path("logs/logs.txt")
    main(api_url, file_path)
