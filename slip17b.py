import datetime
#Write Python program that has a class Person storing name and date of
#birth(DOB) of a person. Subtract the DOB from today’s date to find out
#whether a person is eligible to vote or not.

class Person:
	def __init__(self, name, dob):
		self.name = name
		self.dob = dob

	def is_eligible_to_vote(self):
		today = datetime.date.today()
		age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
		return age >= 18

# Example usage
name=input('Enter your name: ')
year=int(input('Enter your year of birth: '))
month=int(input('Enter your month of birth: '))
day=int(input('Enter your day of birth: '))
dob=datetime.date(year, month, day)
person=Person(name, dob)
if person.is_eligible_to_vote():
	print('You are eligible to vote')
else:
	print('You are not eligible to vote')
