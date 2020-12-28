import statistics as st
import scipy.stats as sp
import math
import csv


from src.config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL, POPULATION_JSON_PATH

from src.normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST


cases_total = sum(CASES_BY_STATE.values())
cases_max = max(CASES_BY_STATE.values())
cases_mean = st.mean(CASES_BY_STATE.values())
death_total = sum(DEATH_BY_STATE.values())
death_max = max(DEATH_BY_STATE.values())
death_mean = st.mean(DEATH_BY_STATE.values())
recovery_total = sum(RECOVERY_BY_STATE.values())
recovery_max = max(RECOVERY_BY_STATE.values())
recovery_mean = st.mean(RECOVERY_BY_STATE.values())

print('cases total/min/max', cases_total, cases_max, cases_mean)
print('death total/min/max', death_total, death_max, death_mean)
print('recovery total/min/max', recovery_total, recovery_max, recovery_mean)

import operator

def classify_by_mean(data_dict):
    classes = ['OVERMEAN', 'MEAN']
    total = sum(data_dict.values())
    mean = st.mean(data_dict.values())

    result_dict = {}
    for state in data_dict:
        if data_dict[state] > mean:
            result_dict[state] = classes[0]
        else:
            result_dict[state] = classes[1]


    sort_dict = dict(sorted(result_dict.items(), key=operator.itemgetter(1)))

    return sort_dict


print('cases classifier', classify_by_mean(CASES_BY_STATE))
print('death classifier', classify_by_mean(DEATH_BY_STATE))
print('recovery classifier', classify_by_mean(RECOVERY_BY_STATE))

print('writing dataset... ', STATES_DATASET_PATH)
with open(STATES_DATASET_PATH, mode='w') as csv_file:
    fieldnames = ['state', 'cases', 'death', 'recovery']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()

    for key in RECOVERY_BY_STATE:
        writer.writerow({'state': key, 'cases': CASES_BY_STATE[key], 'death': DEATH_BY_STATE[key], 'recovery': RECOVERY_BY_STATE[key]})

