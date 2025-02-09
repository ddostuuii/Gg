import os
import sys
import time
import json
import random
import threading
import requests
import uuid
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

try:
    from websocket import create_connection
except ImportError:
    os.system("pip install websocket-client")
    from websocket import create_connection

# Open the Telegram Channel
import webbrowser
webbrowser.open("https://t.me/Plya_Team")

# Initialize rich console
console = Console()

# Account counters
success = 0
failed = 0
retry = 0
accounts = []

# Function to display the animated box
def display_box():
    while success < 50:
        os.system("clear" if os.name == "posix" else "cls")  # Clear screen

        box_text = """[bold cyan]
╭──────────────────────────── SAFEUM TOOL ────────────────────────────╮
│                                                                     │
│            [bold red]Multi-Account Generator[/bold red]             │
│                                                                     │
│             [bold cyan]Owner: @seedhe maut[/bold cyan]              │
│       [bold green]Generating Safeum Accounts...[/bold green]        │
╰─────────────────────────────────────────────────────────────────────╯
[/bold cyan]"""

        console.print(Text(box_text, justify="center"))
        time.sleep(1)

# Function to create Safeum accounts
def work():
    global failed, success, retry

    username = choice("qwertyuiooasdfghjklzxcvpbnm") + "".join(
        choices(list("qwertyuioasdfghjklzxcvbnpm1234567890"), k=16)
    )

    try:
        con = create_connection(
            "wss://195.13.182.213/Auth",
            header={
                "app": "com.safeum.android",
                "host": None,
                "remoteIp": "195.13.182.213",
                "remotePort": str(8080),
                "sessionId": str(uuid.uuid4()),
                "time": "2024-04-11 11:00:00",
                "url": "wss://51.79.208.190/Auth",
            },
            sslopt={"cert_reqs": CERT_NONE},
        )

        con.send(
            dumps(
                {
                    "action": "Register",
                    "subaction": "Desktop",
                    "locale": "en_LV",
                    "gmt": "+03",
                    "password": {
                        "m1x": "5284472cbfadaf07932442855c56c53eefa7a3ba3e5df71908c299edc1141649",
                        "m1y": "bd36a298d03c9d8f637895bc4595d7fffb445ebde10226b5f4f7e8b5ba0bd853",
                        "m2": "b387c7efe18b119459a00c055bd87405d833e4a804ee10495a5f1535d42b5c29",
                        "iv": "3205f0d29dd638d12f8ab293c2fd46ac",
                        "message": "2b177cd8cafc75d2fb0735a11190c6b893a681ec188120fba2323d22a58d3d374440f6b84985d1787639103521d0ad8fc1c94b9e398b227caec4634d20aa8dbd9d38ded1289a0b01db1fc8e2f0292617",
                    },
                    "magicword": {
                        "m1x": "370c2ed52f368efb131857b7132d78cdf687a88210fd91f9d24455d30de15256",
                        "m1y": "b081644eaad191729fec40d8ec401ec49d0a38c488f3de10d374f2e9f6257679",
                        "m2": "090e58d2cabe8bc66c7ca3afa48b032545e8aca522431881cf0c8643b7c4fbcc",
                        "iv": "b706987a9c3bd72369b135bbd0421a75",
                        "message": "b2da38580a855ed6592b6b95a50e712e",
                    },
                    "magicwordhint": "0000",
                    "login": str(username),
                    "devicename": "Xiaomi 23106RN0DA",
                    "softwareversion": "1.1.0.2300",
                    "nickname": "safeum_user",
                    "os": "AND",
                    "deviceuid": str(uuid.uuid4()),
                    "devicepushuid": "*djLCF_YCTyKYwPG2sfCouM:APA91bF414Dk4qM3A9R7zaK6qQr_LKS8VkXs9zkgUAdNQJnLoQM4rpZwzv6kTI5U0Ud5SitNNXRYdL53FjHzfKgl_g19gyxqZWkZhFptvoJ3GNqM7IesIzzCh8p8HIM7nRTRnsivlV9v",
                    "osversion": "and_13.0.0",
                    "id": str(random.randint(1000000000, 9999999999)),
                }
            )
        )

        gzip = decompress(con.recv()).decode("utf-8")

        if '"status":"Success"' in gzip:
            success += 1
            accounts.append(username + ":rrrr")
            with open("maur.txt", "a") as f:
                f.write(username + ":rrrr\n")
        else:
            failed += 1
    except:
        retry += 1

# Function to update UI with progress
def update_progress():
    global success, failed, retry

    with Progress(
        TextColumn("[bold green]Success: {task.fields[success]}[/bold green]"),
        BarColumn(),
        TextColumn("[bold red]Failed: {task.fields[failed]}[/bold red]"),
        BarColumn(),
        TextColumn("[bold yellow]Retry: {task.fields[retry]}[/bold yellow]"),
        console=console,
    ) as progress:
        task = progress.add_task(
            "[bold magenta]Processing Accounts...",
            total=100,
            success=success,
            failed=failed,
            retry=retry,
        )

        while success < 50:  # Stop when 50 successful accounts are created
            time.sleep(0.5)  # Simulate work
            progress.update(
                task,
                advance=random.randint(0, 2),
                success=success,
                failed=failed,
                retry=retry,
            )

# Run UI and Safeum account creation in parallel
if __name__ == "__main__":
    thread1 = threading.Thread(target=display_box)
    thread2 = threading.Thread(target=update_progress)
    thread3 = ThreadPoolExecutor(max_workers=10000)

    thread1.start()
    thread2.start()

    while success < 50:
        thread3.submit(work)

    thread1.join()
    thread2.join()
