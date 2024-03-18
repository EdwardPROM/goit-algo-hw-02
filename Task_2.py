from collections import deque

def is_palindrome(input_string):
    # Ініціалізуємо двосторонню чергу
    queue = deque()
    input_string = input_string.lower().replace(" ", "")
    
    # Додаємо всі символи рядка до двосторонньої черги
    for char in input_string:
        queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False  # Якщо символи не співпадають
    return True  # Якщо всі символи співпадають

input_str = "Was it a car or a cat I saw"
print(is_palindrome(input_str)) 