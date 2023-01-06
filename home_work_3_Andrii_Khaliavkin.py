# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".


while True:
    word = input("Enter a word with letter 'o': ")
    if "o" in word.lower():
        break
    else:
        print("There is no letter 'o' in your word. Try again.")


# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for item in lst1:
    if type(item) == str:
        lst2.append(item)

print(lst2)


# Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі).


text = input("Enter a text: ")
words = text.split()
count = 0

for word in words:
    if word[-1].lower() == "o":
        count += 1

print(count)

