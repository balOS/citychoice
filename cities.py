#! python3
#This project is a city selection tool that allows you to find the ideal city based on 4 criteria: winter weather, population, cost, and Whole Foods access...I know.

#FUTURE TODO: (ideally) update with a front end interface of some sort before you publish. that could be kind of cool. (i mean, would that be like the lamest easy first product? does a product need that?)

import re
import pandas as pd
import random

def start():
    
  print("Hey, what's happening? We're going to find you a new place to live.")
  print("\n")
  name = input("What's your name? ")
  print('\n')
  city = input("Where do you currently live? ")
  print('\n')


  percentile = input("""Let's talk about the weather in winter. What are you willing to put up with?
  a - only the best
  b - it's gotta be good
  c - alright
  d - eh, I don't care
  """)
  
  winterWeather = int()

  if 'a' in  percentile:
    winterWeather = 15
  elif 'b' in percentile:
    winterWeather = 30
  elif 'c' in percentile:
    winterWeather = 50
  else:
    winterWeather = 100


  df = pd.read_csv('citiesCSV/CitiesWeather.csv')
  #to remove row lengths and see everything printed - pd.set_option("max_rows", None)
  goodSpot = df.loc[df["Winter"] <= winterWeather, ['Overall', 'City', 'Winter']]

  weather = goodSpot['City'].str.split(',', n = 1, expand = True) 
  weatherCity = weather[0]

  print('\n')
  population = input("""How big of a city do you want to live in? \n
  a - small (<100,000 people)
  b - medium (<300,000 people)
  c - big (<1,000,000 people)
  d - real big, bubba (>1,000,000 people)
  """)
  popChoice = int()


  if 'a' in  population:
    popChoice = 100000
  elif 'b' in population:
    popChoice = 300000
  elif 'c' in population:
    popChoice = 1000000
  else:
    popChoice = 10000000

  df3 = pd.read_csv('citiesCSV/CitiesPopulation.csv')
  goldilocks = df3.loc[df3['2019'] <= popChoice, ['City', '2019']]

  size = goldilocks['City'].str.split(' city', n = 1, expand = True) 
  sizedCity = size[0]

  #In future, you could make this a question that builds on your last answer. What's your current city's Cost of Living? If none in the system, use default numbers.
  print('\n')
  df4 = pd.read_csv('citiesCSV/CitiesCostOfLiving.csv')
  cost = input("""What kind of price range are you looking for? \n
  a - dirt cheap ("I ain't payin shit.")
  b - cheap ("Keep it reasonable...we're kinda broke.")
  c - average - ("We'll be fine and can still afford Whole Foods.")
  d - don't care - "I'm rich biiiiatch!"
  """)

  livingCost = ()
  if 'a' in  cost:
    livingCost = 45
  elif 'b' in cost:
    livingCost = 60
  elif 'c' in cost:
    livingCost = 80
  else:
    livingCost = 150


  money = df4.loc[df4['Cost of Living Plus Rent Index'] < livingCost, ['City', 'Cost of Living Plus Rent Index']]

  affordable = money['City'].str.split(',', n = 1, expand = True)
  affordableCity = affordable[0]
  print('\n')
  #TODO: Need to test this whole process. Not a must for v1, so can be pulled.
  compCity = input("Do you want this to be less expensive than " + city + "? ")
  moneyComp = ()
  if compCity == 'yes':
    for place in affordableCity:
      if city in place:
        moneyComp = money[city, :1]

  print(moneyComp)

  df2 = pd.read_csv('citiesCSV/CitiesWholeFoods.csv', usecols=['City'])
  wholeFoodsCity = (df2['City'].str.strip())
  wholeFoods = input("Do you need a local Whole Foods? ")

  best_city = set(weatherCity) & set(wholeFoodsCity) & set(sizedCity) & set(affordableCity)
  alt_best_city = set(weatherCity) & set(sizedCity) & set(affordableCity)

  print("""Alright, your new home is coming in...
  3
  2
  1
  ...
  """)

  input("You ready? ")

  mainCity = random.choice(tuple(best_city))
  altCity = random.choice(tuple(alt_best_city))

  #TODO: Then, have a premium add on to make people pay $.99 to see all potential listings. Ha! This is going to require you to turn the set into a proper dictionary, I guess?

  #premium - need to write a $.99 feature in here. 

  if wholeFoods == 'yes' or 'Yes' or 'YES' or 'Y':
    print(mainCity)
    allCities = input("Want to see the full list of cities that fit your criteria? ")
    if allCities == 'yes' or 'Yes' or 'YES' or 'Y':
      print (best_city)
    else:
      print("Well I bet you have a ton of fun there. Peace!")
  else:
    print(altCity)
    allCities = input("Want to see the full list of cities that fit your criteria? ")
    if allCities == 'yes' or 'Yes' or 'YES' or 'Y':
      print (alt_best_city)
    else:
      print("Well I bet you have a ton of fun there. Peace!")



  if wholeFoods == 'yes' or 'Yes' or 'YES' or 'Y':
    print("Thanks for playing. If you want to learn more about your future home in " + mainCity + ", I have a few friends there.")
    print("\n")
    print("Leave me your email, and I'll get you set up.")
    email = input()
  else:
    print("Thanks for playing. If you want to learn more about your future home in " + altCity + ", I can share some hot info.")
    print("\n")
    print("Leave me your email, and I'll get you set up.")
    email = input()

  #Could use a question to ask what kind of information they want on that city (w/ a few options: culture, food, music, weather, cost, crime, walkability)
  #TODO: Need to write system to hold their email and send them a follow up. Google API takes a lot of work, although I am headed that way. Just need to:
  #  authorize some stuff and understand that process better
  # input API here (good training for spotify and O*NET work)

  print("Awesome, I'll shoot you a note shortly. Cheers " + name + "!")
  print("\n")
  print("TM balOS 2020")

while True:
    start()
    if input("Want to play again? (Y/N) ").strip().upper() != 'Y':
        break

#Future TODO: print a list of all the criteria that matches their choices. What categories do the cities share? 