# import pandas

DATASET_PATH = '/home/art/datasets/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time_Nov_7.csv'
print('parsing dataset... ', DATASET_PATH)

# convert csv to list
def parse_csv(csvfile):
    import csv
    dataset = []
    with open(DATASET_PATH, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        '''
        0 - submission_date
        1 - state
        3 - conf_cases
        8 - conf_death
        13 - consent_cases
        14 - consent_death
        '''
        for row in csvreader:
            if row[0] != 'submission_date' and row[3] != '' and row[8] != '' and \
                row[13] == 'Agree' and row[14] == 'Agree' and \
                row[3] != '0' and row[8] != '0':
                    # consent_cases,consent_deaths:
                if row[0].split('/')[1] in ['01','05', '10', '15', '20', '25']:
                    dataset.append([row[0], row[1], row[3], row[8]])
    return dataset

dataset = parse_csv(DATASET_PATH)

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


POPULATION_RATE_RAW = {
    '04/15/2020': 329519667,
    '04/20/2020': 329541155,
    '04/25/2020': 329562644,
    '05/01/2020': 329588430,
    '05/05/2020': 329606219,
    '05/10/2020': 329628455,
    '05/15/2020': 329650692,
    '05/20/2020': 329672928,
    '05/25/2020': 329695164,
    '06/01/2020': 329726295,
    '06/05/2020': 329746456,
    '06/10/2020': 329771658,
    '06/15/2020': 329796860,
    '06/20/2020': 329822061,
    '06/25/2020': 329847263,
    '07/01/2020': 329877505,
    '07/05/2020': 329899443,
    '07/10/2020': 329926866,
    '07/15/2020': 329954289,
    '07/20/2020': 329981711,
    '07/25/2020': 330009134,
    '08/01/2020': 330047526,
    '08/05/2020': 330069263,
    '08/10/2020': 330096434,
    '08/15/2020': 330123605,
    '08/20/2020': 330150776,
    '08/25/2020': 330177947,
    '09/01/2020': 330215986,
    '09/05/2020': 330238125,
    '09/10/2020': 330265798,
    '09/15/2020': 330293471,
    '09/20/2020': 330321145,
    '09/25/2020': 330348818,
    '10/01/2020': 330382026,
    '10/05/2020': 330400989,
    '10/10/2020': 330424693,
    '10/15/2020': 330448397,
    '10/20/2020': 330472101,
    '10/25/2020': 330495805,
    '11/01/2020': 330528990,
    '11/05/2020': 330546051
}
