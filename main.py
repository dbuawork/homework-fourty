string = input("Введіть рядок за домогою літер та цифр: ")

letter_count = 0
digit_count = 0

for char in string:
    if char.isalpha():
        letter_count += 1