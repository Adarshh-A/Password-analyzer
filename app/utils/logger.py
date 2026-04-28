import datetime

def log_event(password, result):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | {password} | {result}\n")
