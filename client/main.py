import asyncio
import os
import random
import requests

import aiofiles
from fastapi import FastAPI
from fastapi import BackgroundTasks

app = FastAPI()


def generate_log_entry():
    ip_addresses = [
        '127.0.0.1',
        '0.0.0.0',
        'localhost'
    ]
    methods = [
        'GET', 'POST',
        'PUT', 'DELETE',
        'PATCH', 'TRACE',
        'OPTIONS', 'PUT'
    ]
    uri_data = ['example', 'test']
    status_codes = [
        200, 404, 500,
        202, 100, 202, 201
    ]

    ip = random.choice(ip_addresses)
    uri = random.choice(uri_data)
    method = random.choice(methods)
    status_code = random.choice(status_codes)

    log_entry = f"{ip} {method} {uri} {status_code}"
    return log_entry


def send_log_entry(log_entry):
    url = 'http://127.0.0.1:8001/api/data/'
    requests.post(url, json={'log': log_entry})


async def write_log_entry(log_entry: str):
    log_file_path = 'client/logs/server_logs.txt'
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    async with aiofiles.open(log_file_path, mode='a') as log_file:
        await log_file.write(log_entry)


@app.post("/generate-logs/")
async def generate_logs(background_tasks: BackgroundTasks):
    n = int(os.getenv('LOG_GENERATOR_N', 2))
    m = int(os.getenv('LOG_GENERATOR_M', 10))
    for _ in range(n):
        log_entry = generate_log_entry()
        background_tasks.add_task(send_log_entry, log_entry)
        background_tasks.add_task(write_log_entry, log_entry)
        await asyncio.sleep(random.randint(0, m) / 1000)

    return {"message": f"Generated {n} log entries."}