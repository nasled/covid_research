import requests

response = requests.get('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD&bom=true&format=true')
content = str(response.content.decode('utf-8'))
print('len', len(content))

DATASET_PATH = '/tmp/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time_last.csv'
print('parsing dataset... ', DATASET_PATH)

file = open(DATASET_PATH, 'w')
file.write(content)
file.close()