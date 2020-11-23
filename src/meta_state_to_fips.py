
STATE_TO_FIPS_CODE = {
    'AK': '02',
    'AL': '01',
    'AR': '05',
    'AS': '60',
    'AZ': '04',
    'CA': '06',
    'CO': '08',
    'CT': '09',
    'DC': '11',
    'DE': '10',
    'FL': '12',
    'GA': '13',
    'GU': '66',
    'HI': '15',
    'IA': '19',
    'ID': '16',
    'IL': '17',
    'IN': '18',
    'KS': '20',
    'KY': '21',
    'LA': '22',
    'MA': '25',
    'MD': '24',
    'ME': '23',
    'MI': '26',
    'MN': '27',
    'MO': '29',
    'MS': '28',
    'MT': '30',
    'NC': '37',
    'ND': '38',
    'NE': '31',
    'NH': '33',
    'NJ': '34',
    'NM': '35',
    'NV': '32',
    'NYC': '36',
    'OH': '39',
    'OK': '40',
    'OR': '41',
    'PA': '42',
    'PR': '72',
    'RI': '44',
    'SC': '45',
    'SD': '46',
    'TN': '47',
    'TX': '48',
    'UT': '49',
    'VA': '51',
    'VI': '78',
    'VT': '50',
    'WA': '53',
    'WI': '55',
    'WV': '54',
    'WY': '56'
}



from config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL, POPULATION_JSON_PATH

from normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST

print('parsing dataset... ', GEOCODES_DATASET_PATH)

# convert csv to dict
def parse_csv_to_dict(csvfile):
    import csv
    dataset = {}
    with open(GEOCODES_DATASET_PATH, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            # print(row)
            if row[0] not in dataset.keys():
                dataset[row[0]] = [row[0] + row[1]]
            else:
                dataset[row[0]].append(row[0] + row[1])
    return dataset

STATE_CODE_TO_FIPS_CODE = parse_csv_to_dict(GEOCODES_DATASET_PATH)

# INPUT_DATA = {'WY': 'MEAN', 'NYC': 'OVERMEAN', 'OH': 'OVERMEAN', 'ID': 'MEAN', 'CO': 'MEAN', 'AZ': 'OVERMEAN', 'CT': 'MEAN', 'TN': 'OVERMEAN', 'MA': 'OVERMEAN', 'AL': 'OVERMEAN', 'VA': 'OVERMEAN', 'MI': 'OVERMEAN', 'MS': 'MEAN', 'IL': 'OVERMEAN', 'WI': 'OVERMEAN', 'NC': 'OVERMEAN', 'OR': 'MEAN', 'MT': 'MEAN', 'SC': 'OVERMEAN', 'KY': 'MEAN', 'PR': 'MEAN', 'OK': 'MEAN', 'UT': 'MEAN', 'DE': 'MEAN', 'MP': 'MEAN'}
# for state in INPUT_DATA:
#     if state in STATE_TO_FIPS_CODE.keys():
#         state_code = STATE_TO_FIPS_CODE[state]
#         fips_code = STATE_CODE_TO_FIPS_CODE[state_code]
#         print(state, fips_code)