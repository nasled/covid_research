# import pandas
import json

from src.config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL, POPULATION_JSON_PATH

print('parsing dataset... ', MAIN_DATASET_PATH)

# convert csv to list
def parse_csv(csvfile):
    import csv
    dataset = []
    with open(MAIN_DATASET_PATH, newline='') as csvfile:
        # csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csvreader = csv.reader(csvfile, quotechar='"', delimiter=',')
        '''
        0 - submission_date
        1 - state
        3 - conf_cases
        8 - conf_death
        13 - consent_cases
        14 - consent_death
        '''
        for row in csvreader:
            # 10/21/2020,MN,"126,591",,,"1,060",13,"2,334","2,269",65,35,1,10/22/2020 01:34:46 PM,N/A,Agree
            if row[0] != 'submission_date' and row[3] != '' and row[8] != '' and \
                row[13] == 'Agree' and row[14] == 'Agree' and \
                row[3] != '0' and row[8] != '0':
                    # consent_cases,consent_deaths:
                if row[0].split('/')[1] in ['01','05', '10', '15', '20', '25']:
                    # dataset was updated
                    dataset.append([row[0], row[1], row[3].replace(',',''), row[8].replace(',','')])
    return dataset

dataset = parse_csv(MAIN_DATASET_PATH)

print('dataset 0:', dataset[0])

# group by date = state/case/death
group_storage = {}
for row in dataset:
    '''
    ['05/01/2020', 'CO', '14078', '693']
    '''
    line = (row[1], row[2], row[3])
    if row[0] not in group_storage.keys():
        group_storage[row[0]] = [line]
    else:
        group_storage[row[0]].append(line)

# group by date/state = case/death
date_storage = {}
for date in group_storage:
    title = ''
    case = 0
    death = 0
    for state in group_storage[date]:
        # title = state[0]
        case = case + int(state[1])
        death = death + int(state[2])
    date_storage[date] = [case,death,case-death]
sorted_dates = sorted(date_storage)


# generate state data
cases_by_states_dict = {}
death_by_states_dict = {}
recovery_by_states_dict = {}
for date in sorted_dates:
    for row in group_storage[date]:
        state, case, death = row
        if state == 'NYC':
            state = 'NY'
        if state == 'MP':
            continue
        if state not in cases_by_states_dict:
            cases_by_states_dict[state] = 0
            death_by_states_dict[state] = 0
            recovery_by_states_dict[state] = 0
        cases_by_states_dict[state] = int(case)
        death_by_states_dict[state] = int(death)
        recovery_by_states_dict[state] = int(case) - int(death)
CASES_BY_STATE = cases_by_states_dict
DEATH_BY_STATE = death_by_states_dict
RECOVERY_BY_STATE = recovery_by_states_dict


# generate cases points
counter = 0
date_dict = {}
case_dict = {}
death_dict = {}
recovery_dict = {}
for date in sorted_dates:
    case, death, recovery = date_storage[date]
    date_dict[date] = counter + 1
    case_dict[date] = case
    death_dict[date] = death
    recovery_dict[date] = recovery
# calculate differences between periods
DATE_RAW = date_dict
CASE_RATE_RAW = case_dict
DEATH_RATE_RAW = death_dict
RECOVERY_RATE_RAW = recovery_dict
print('parsed points', len(CASE_RATE_RAW))
