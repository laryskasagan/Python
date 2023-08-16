#!/usr/bin/env python3

print("Welcome to the age calculator.")
answer = input("Would you like to know how old you will be in a particular years? (y/n) ")

while not (answer == 'y' or answer == 'n'):
	print('The value of answer is', answer)
	print("I'm sorry, I didn't understand. Please try again.")
	answer = input("Wolud you like to know how old you will be in a particular years? (y/n) ")

if answer == 'n':
	print("I'm sorry you're not intrested. Goodbye!")
else:
	dates = []	
	
	print("Valid formats for dates: '1/1/2000' or 'jan 1, 2000'")
	dob = input("What's your birthday? ")
	dates.append(dob)
	
	
	future =input("What date did you want to know about? ")
	dates.append(future)
	
	month = ['','']
	day = ['','']
	year = ['','']
	counter = 0
	for date in dates:
		d = 0
		y = 0
		if dates[counter][0].isdigit() is True:
			tempDate = date.split('/')
			month[counter] = tempDate[0]
			day[counter] = tempDate[1]
			year[counter] = tempDate[2]
		else:
			tempDate = date.split()
			month[counter] = tempDate[0]
			year[counter] = tempDate[2]
			for i in tempDate[1]:
				if i != ',':
					day[counter] = day[counter] + i
		counter += 1
			
			
	
	myDict = {'jan': 1,'Jan': 1,'january': 1,'January': 1,'feb': 2,'Feb': 2,'february': 2,'February': 2,'mar': 3,'Mar': 3,'march': 3,'March': 3,'apr': 4,'Apr': 4,'april': 4,'April': 4,'may': 5,'May': 5,'jun': 6,'Jun': 6,'june': 6,'June': 6,'jul': 7,'Jul': 7,'july': 7,'July': 7,'aug': 8,'Aug': 8,'august': 8, 'August': 8,'sep': 9,'Sep': 9,'september': 9,'September': 9,'oct': 10,'Oct': 10,'october': 10,'October': 10,'nov': 11,'Nov': 11,'november': 11,'November': 11,'dec' : 12,'Dec': 12,'december': 12,'December': 12}
	
	if month[0] in myDict:
		month[0] = myDict[month[0]]
	if month[1] in myDict:
		month[1] = myDict[month[1]]
	
	month[0] = int(month[0])
	month[1] = int(month[1])
	
	
	age = int(year[1]) - int(year[0])
	day[0] = int(day[0])
	day[1] = int(day[1])
	if month[1] <= month[0]:
		age = age - 1
		if month[1] == month[0]:
			if day[1] >= day[0]:
				age = age + 1
		
	print('On ' + dates[1] + ' you will be ' + str(age) + ' years old.')
	print('Goodbye!')
