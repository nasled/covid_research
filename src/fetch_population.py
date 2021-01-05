import requests
import json


from src.config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL, POPULATION_JSON_PATH
from src.parse_dataset import DATE_RAW

# from src.normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
#                           CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
#                           POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
#                           POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
#                           POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
#                           POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
#                           POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
#                           POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
#                           POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST

# 20201103
def convert_date(date):
    month, day, year = date.split('/')
    return year + month + day

population_dict = {}
for date in DATE_RAW:
    converted_date = convert_date(date)
    response = requests.get(CENSUS_ENDPOINT_URL.format(converted_date))
    json_response = response.content.decode('utf-8')
    dict_response = json.loads(json_response)
    population_dict[date] = int(dict_response['us']['population'])

    print(converted_date, json_response)



with open(POPULATION_JSON_PATH, 'w+') as outfile:
    json.dump(population_dict, outfile)

# put in parse dataset
print(population_dict)
print('population json saved to:', POPULATION_JSON_PATH)


print('latex table')
table = []
table.append(['Date', 'Population'])
for date in DATE_RAW:
    table.append([ str(date), str(population_dict[date]) ])

latex = ''
for row in table:
    latex = latex + "\t\t&\t\t".join(row) + " \\\ \n"
print(latex)