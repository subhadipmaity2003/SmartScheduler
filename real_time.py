# File: analytics/real_time.py
import time
import random

def generate_task_performance():
    while True:
        task_id = random.randint(1, 10)
        performance = random.uniform(0, 100)
        print(f"Task ID: {task_id}, Performance: {performance:.2f}%")
        time.sleep(5)

if __name__ == "__main__":
    generate_task_performance()

