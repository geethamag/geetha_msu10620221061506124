enteryear=int(input("Enter the year you want to check:")) 
if(enteryear%4==0 and enteryear%100!=0 or enteryear%400==0):
  print("The year you've entered is a leap year!")
else:
  print("The year you've entered isn't a leap year!")