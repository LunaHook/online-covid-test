from termcolor import colored
IW = True
Nextp = "yes"
Hos = 0
Tested = 0
import subprocess as sp
while IW == True:
  print(colored("Welcome, today I will test you and anyone else for", "white"), colored("COVID-19", "red"), colored("symptoms and then offer suggestions", "white"))
  
  Feeling = input("How are you feeling today? (Please type in either 'good' or 'bad'): \n ")
#if user feeling good
  if Feeling == "good":
    Tested = Tested + 1
    Nextp = input("Ok, great. Is there a next person? (Please type in either 'yes' or 'no'): \n ")
    if Nextp == "yes":
#to clear the screen so no one sees other's answers 
      sp.call('clear', shell=True)
      print("Ok, please bring them in ")
    if Nextp == "no":
      print("Ok, bye! \nTested: \n %r \nNeed to go to the hospital: \n %r " % (Tested, Hos))
      IW = False
#if usr feeling bad
  if Feeling == "bad":
    Tested = Tested + 1
#Question 1, temp.bad
    
# regularly 98.6
    Q1 = float(input("Please check your temperature. Type the temperature up to 1 decimal place: \n "))
    var1 = 2
    if Q1 >= 100.4:
      var1 = 1
#Question 2, Oximeter
# regulerly
    Q2 = int(input("Please check your Pulse Oximeter level. Type it here: \n "))
    var2 = 2
    if Q2 <= 90:
      var2 = 1
#1 = bad
#2 = good
    if var1 == 2 and var2 == 2:
      Nextp = input("Don't worry, You are totaly fine. Is there a next person? (Please type in either 'yes' or 'no'): \n ")
    if var1 == 1 and var2 == 1:
      print(colored("I recomend going to get COVID-19 tested.", "red"), colored("Is there a next person? (Please type in either 'yes' or 'no'):"))
      Nextp = input("\n")
      Hos = Hos + 1
    if var1 == 2 and var2 == 1:
      Nextp = input("Your oxygen level is low, please monitor this for the next few days. Is there another person for screening? (Please type in either 'yes' or 'no'): \n ")
    if var1 == 1 and var2 == 2:
      Nextp = input("You have a fever, please monitor this for the next few days. Is there a next person? (Please type in either 'yes' or 'no'): \n ")
    #to clear the screen so no one sees other's answers 
    sp.call('clear', shell=True)
    if Nextp == "no":
      sp.call('clear', shell=True)
      print("Ok, bye! \nTested: \n %r \nNeed to go to the hospital: \n %r " % (Tested, Hos))
      IW = False
    if Nextp == "yes":
      #to clear the screen so no one sees other's answers
      sp.call('clear', shell=True)
      print("Ok, bring them in.")

