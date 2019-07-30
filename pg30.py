#Creating a mapping of state to abbreviation

states = { #Create a dict for states
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states and some cities in them

cities = { #create a dict for cities
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is : ",states['Florida'])

#do it by using the state then cities dict
print('-' * 10) 
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for abbrev, city in list(cities.items()): # cities.items() return key and value as a list #list funct not necessary
	print(f"{states} state is abbreviated {abbrev}")
	print(f"and has cuty {cities[abbrev]}")

print("-" * 10)

#safely get a abbreviation by state that might nit be in there

state = states.get('Texas') 

if not state:
	print("Sorry, no Texas.")

# get a citty with a deafdault value

city = cities.get('TX', 'Does not exist')
print(f"The cuty for state 'TX' is: {city}")
