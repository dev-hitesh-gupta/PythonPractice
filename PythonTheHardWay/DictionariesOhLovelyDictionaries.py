states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco', 'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)

print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)

print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)

print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)

for key, value in list(cities.items()):
    print(f"{key} has the city {value}")

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)

state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('CA', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")