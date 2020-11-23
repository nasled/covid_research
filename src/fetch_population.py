import requests
import json

ENDPOINT_URL = 'https://www.census.gov/popclock/data/population.php/us?date={0}'


from src.parse_dataset import DATE_RAW


# 20201103
def convert_date(date):
    month, day, year = date.split('/')
    return year + month + day

population_dict = {}
for date in DATE_RAW:
    converted_date = convert_date(date)
    response = requests.get(ENDPOINT_URL.format(converted_date))
    json_response = response.content.decode('utf-8')
    dict_response = json.loads(json_response)
    population_dict[date] = int(dict_response['us']['population'])

    print(converted_date, json_response)

# put in parse dataset
print(population_dict)



