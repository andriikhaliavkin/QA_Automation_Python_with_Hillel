# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну функцію гри з попередньої дз.
# Після закінчення гри декоратор має сповістити, скільки тривала гра.
import time


def time_check(func):
    """This function checks time of execution of function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Виконання функції тривало {end_time - start_time} секунд")
    return wrapper


def age_check(age):
    """This function checks age of user and returns answer"""
    if age < 7:
        return f"Тобі ж {age} {get_year(age)}! Де твої батьки?"
    elif age < 16:
        return f"Тобі лише {age}, а це е фільм для дорослих!"
    elif age > 65:
        return f"Вам {age} {get_year(age)}? Покажіть пенсійне посвідчення!"
    elif age % 11 == 0:
        return f"О, вам {age} {get_year(age)}! Який цікавий вік!"
    else:
        return f"Незважаючи на те, що вам {age} {get_year(age)}, білетів всеодно нема!"


def get_year(age):
    """Take age as arg, return string"""
    if age % 10 == 1 and age != 11:
        return "рік"
    elif age % 10 in (2, 3, 4) and age not in (12, 13, 14):
        return "роки"
    else:
        return "років"


@time_check
def main():
    """Main function"""
    while True:
        user_age = int(input("Скільки вам років? "))
        print(age_check(user_age))
        user_answer = input("Хочете повторити виконання? (Yes/No) ")
        if user_answer == "Yes":
            continue
        elif user_answer == "No":
            break
        else:
            print("Неправильна відповідь!")
            break


