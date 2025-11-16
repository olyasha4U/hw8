import logging

# logging.basicConfig(level=logging.INFO, filename="year.log", filemode="w", format="Year-Month-Day :  %(message)s")
# logging.info("2025:11:Saturday")

# 3
# def login(username, password):
#     correct_username = "Olga"
#     correct_password = "12345"
#     try:
#
#         assert username == correct_username and password == correct_password
#         print("Вхід виконано успішно")
#     except :
#         print("Невірне ім'я користувача або пароль")
#
# login("Olga", "12345")
# login("user", "54321")
# 4
# def check_age(age):
#     age_ok =18
#     try:
#         assert age >= age_ok
#         print("Ви можете використовувати цей сервіс")
#     except:
#         print("Вам має бути 18 років або більше")
#
# check_age(13)
# check_age(19)
5
def process_list (input_list):

    try:
        assert len(input_list) >= 3
        print(f"Список містить {len(input_list)}  елементів")
    except:
        print("Список повинен містити принаймні 3 елементи")

process_list(["a"])
process_list(["abc", "a","b", 3])
process_list(["abc", "a","b"])