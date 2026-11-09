def input_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Введите целое число")