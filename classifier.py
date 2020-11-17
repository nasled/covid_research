import statistics as st
import scipy.stats as sp
import math

from normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
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

    # print('list', data_dict)
    # print('mean', mean)
    # print('result', result_dict)

    return result_dict


print('cases classifier', classify_by_mean(CASES_BY_STATE))
print('death classifier', classify_by_mean(DEATH_BY_STATE))
print('recovery classifier', classify_by_mean(RECOVERY_BY_STATE))

'''
cases total/min/max 3678525 447491 147141
death total/min/max 92921 19392 3716.84
recovery total/min/max 3585604 437461 143424.16
cases classifier {'WY': 'MEAN', 'NYC': 'OVERMEAN', 'OH': 'OVERMEAN', 'ID': 'MEAN', 'CO': 'MEAN', 'AZ': 'OVERMEAN', 'CT': 'MEAN', 'TN': 'OVERMEAN', 'MA': 'OVERMEAN', 'AL': 'OVERMEAN', 'VA': 'OVERMEAN', 'MI': 'OVERMEAN', 'MS': 'MEAN', 'IL': 'OVERMEAN', 'WI': 'OVERMEAN', 'NC': 'OVERMEAN', 'OR': 'MEAN', 'MT': 'MEAN', 'SC': 'OVERMEAN', 'KY': 'MEAN', 'PR': 'MEAN', 'OK': 'MEAN', 'UT': 'MEAN', 'DE': 'MEAN', 'MP': 'MEAN'}
death classifier {'WY': 'MEAN', 'NYC': 'OVERMEAN', 'OH': 'OVERMEAN', 'ID': 'MEAN', 'CO': 'MEAN', 'AZ': 'OVERMEAN', 'CT': 'OVERMEAN', 'TN': 'MEAN', 'MA': 'OVERMEAN', 'AL': 'MEAN', 'VA': 'MEAN', 'MI': 'OVERMEAN', 'MS': 'MEAN', 'IL': 'OVERMEAN', 'WI': 'MEAN', 'NC': 'OVERMEAN', 'OR': 'MEAN', 'MT': 'MEAN', 'SC': 'OVERMEAN', 'KY': 'MEAN', 'PR': 'MEAN', 'OK': 'MEAN', 'UT': 'MEAN', 'DE': 'MEAN', 'MP': 'MEAN'}
recovery classifier {'WY': 'MEAN', 'NYC': 'OVERMEAN', 'OH': 'OVERMEAN', 'ID': 'MEAN', 'CO': 'MEAN', 'AZ': 'OVERMEAN', 'CT': 'MEAN', 'TN': 'OVERMEAN', 'MA': 'OVERMEAN', 'AL': 'OVERMEAN', 'VA': 'OVERMEAN', 'MI': 'OVERMEAN', 'MS': 'MEAN', 'IL': 'OVERMEAN', 'WI': 'OVERMEAN', 'NC': 'OVERMEAN', 'OR': 'MEAN', 'MT': 'MEAN', 'SC': 'OVERMEAN', 'KY': 'MEAN', 'PR': 'MEAN', 'OK': 'MEAN', 'UT': 'MEAN', 'DE': 'MEAN', 'MP': 'MEAN'}
'''



import csv
DATASET_PATH = 'd:/OneDrive/655_pr/unit0_project/datasets/csv_for_map.csv'
print('writing dataset... ', DATASET_PATH)


with open(DATASET_PATH, mode='w') as csv_file:
    fieldnames = ['state', 'cases', 'death', 'recovery']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()

    for key in RECOVERY_BY_STATE:
        writer.writerow({'state': key, 'cases': CASES_BY_STATE[key], 'death': DEATH_BY_STATE[key], 'recovery': RECOVERY_BY_STATE[key]})

