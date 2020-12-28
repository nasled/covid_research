import requests

from src.config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL, POPULATION_JSON_PATH

response = requests.get(CDC_ENDPOINT_URL)
content = response.content.decode("utf-8-sig")
print('len', len(content))

print('saving dataset... ', MAIN_DATASET_PATH)
file = open(MAIN_DATASET_PATH, 'w')
file.write(content)
file.close()


