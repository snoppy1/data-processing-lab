import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
is_german = list(filter(lambda city: city["country"] == "Germany", cities))
print(is_german)
    

'''
Your code here

'''

# Print all cities in Spain with a temperature above 12°C
spain_warm = list(filter(lambda city: city["country"] == "Spain" and float(city["temperature"]) > 12, cities))
print(spain_warm)

'''
Your code here

'''
count = 0 
unique =[]
for city in cities:
    if city["country"] not in unique :
        unique.append(city["country"])
        count +=1 
print(count)
# Count the number of unique countries

'''
Your code here

'''

sum_temp = 0
count_temp = 0
for city in cities:
    sum_temp  = sum_temp + float(city["temperature"])
    count_temp += 1
print(sum_temp/count_temp)


# Print the average temperature for all the cities in Germany
is_germany_tem = list(filter(lambda city : city["country"] == "Germany" , cities ))
germany_temp = 0
for i in is_germany_tem:
    germany_temp += float(i["temperature"])
print(germany_temp / len(is_germany_tem))


# Print the max temperature for all the cities in Italy
is_italy= list(filter(lambda city : city["country"] == "Italy" , cities ))
italy_list_temp = [float(city["temperature"]) for city in is_italy]
print(max(italy_list_temp))



'''
Your code here

'''
