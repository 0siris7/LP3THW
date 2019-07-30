states = {
    'Oregon' : 'OR',
    'Florida':  'FL',
    'California': 'CA',
    'New York'  :   'NY',
    'Michigan' : 'MI'
}

cities = {
    "CA" : "San Fransisco",
    'MI' :  "Detroit",
    'FL' :  "Jacksonville"
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbr is: ", states['Michigan'])
print("Florida's abbr is: ", states['Florida'])

print('-' * 10)
print("michigan has : ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has city {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

for state, abbrev in list(states.items()):
    print(f"{states} state is abbteviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("No texas")

city = cities.get('TX', 'Doesnt exist')
print(f"The city for state TX is : {city}")
