# string = input("Введіть рядок за домогою літер та цифр: ")
#
# letter_count = 0
# digit_count = 0
#
# for char in string:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1
# print("Кількість літер у рядку: ", letter_count)
# print("Кількість цифр у рядку: ", digit_count)
#
# ################################################################

# numwords = list(map(int,input("Введіть ряд чисел для пошуку: ").split()))
# numdigits = int(input("Введіть число для пошуку: "))
#
# num = 0
#
# for i in numwords:
#     if i == numdigits:
#         num += 1
# print(f"Число {numdigits} зустрічається {num} разів")

#
# string = input("Введіть з клавіатури рядок: ")
# search_word = input("Введіть слово яке потрібно знайти: ")
# replace_word = input("Введіть слово яким потрібно замінить: ")
#
# words = string.split()
# modified_words = []
#
# for word in words:
#    if word == search_word:
#        modified_words.append(replace_word)
#    else:
#        modified_words.append(word)
# modified_string = " ".join(modified_words)
# print(modified_string)

river = "Dmytro"
print(river[:])
print(river[2:3])
print(river[4:5])
print(river[:5])
print(river[:4])
#print(river[:])
#print(river[1:])
print(river[::-1])
print(river[::-2])
print(len("Dmytro"))


