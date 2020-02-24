# import pyowm
# TASK ONE
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(input('ВВедіть місто яке вас цікавить: '))
# w = observation.get_weather()
# # print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# tempo = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
# print('У Ващому місті швидкість вітру - {} км/год'.format(w.get_wind()['speed']))
# print('Кут вітру - {} км/год'.format(w.get_wind()['deg']))
# print('Вологість - {}'.format(w.get_humidity()))
# print(f"Max - {tempo['temp_max']}\nMid - {tempo['temp']}\nMin - {tempo['temp_min']}")

#TASK TWO

# import random

# random_num = random.randint(1, 100)
# try:
#     player_input = int(input('Enter your number: '))
# except:
#     print('Wrong input, please enter a number!')
#     player_input = int(input('Enter your number: '))
# tries = 0
# while random_num != player_input:
#     tries += 1
#     if random_num > player_input:
#         print("Your number is smaller than random")
#         player_input = int(input('Enter number once again: '))
#     else:
#         print("Your number is bigger than random")
#         player_input = int(input('Enter number once again: '))
# print(f"Congratulations! computer`s number was: {random_num}, it took {tries} tries to get it!")

#TASK THREE ?
# 404 can`t find what to do

#TASK FOUR ?
# 404 can`t find this one too

#TASK FIVE
#Написати функцію, яка обчислює суму цифр введеного числа


# def sum_up_all_nums(nums):
#     sum = 0
#     while nums != 0:
#         sum += nums % 10
#         nums = nums // 10
#     return sum
#
#
# print(sum_up_all_nums(1594))
