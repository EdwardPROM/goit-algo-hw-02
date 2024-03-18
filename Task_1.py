from queue import Queue
import time

# Створення черги заявок
queue = Queue()

# Функція для генерації нової заявки та додавання її до черги
def generate_request():
    new_request = "New request"  # Можна створити нову заявку
    queue.put(new_request)  # Додати заявку до черги
    print("New request generated:", new_request)

# Функція для обробки заявок з черги
def process_request():
    if not queue.empty():  # Перевірка, чи черга не пуста
        request = queue.get()  # Видалення заявки з черги
        print("Processing request:", request)  # Імітація обробки заявки
    else:
        print("Queue is empty. No requests to process.")

try:
    while True:
        generate_request()
        time.sleep(1)
        process_request()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted by user")