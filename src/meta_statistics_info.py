import statistics as st
import scipy.stats as sp
import math

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



def print_metrics_info(title='', x=[]):
    x = list(x)
    print('------------------------')
    if title != '':
        print(title)
    print('set', x)
    print('mean', st.mean(x))
    print('median', st.median(x))
    # print('mode', st.mode(x))
    print('variance', st.variance(x))
    print('stdev', st.stdev(x))
    # print('quantiles', st.quantiles(x))
    print('iqr', sp.iqr(x))
    print('skew', sp.skew(x))
    print('kurtosis', sp.kurtosis(x))
    print('entropy', sp.entropy(x))

# raw
print_metrics_info('raw population', POPULATION_RATE_RAW.values())
print_metrics_info('raw cases', CASE_RATE_RAW.values())
print_metrics_info('raw death', DEATH_RATE_RAW.values())
print_metrics_info('raw recovery', RECOVERY_RATE_RAW.values())

print('-')
#
# applied diff
print_metrics_info('diff population', POPULATION_RATE_DIFF)
print_metrics_info('diff cases', CASE_RATE_DIFF)
print_metrics_info('diff death', DEATH_RATE_DIFF)
print_metrics_info('diff recovery', RECOVERY_RATE_DIFF)

print('-')

# applied Square normalization algorithm

print_metrics_info('diff norm population', POPULATION_NORM_1D)
print_metrics_info('diff norm cases', CASE_RATE_NORM_1D)
print_metrics_info('diff norm death', DEATH_RATE_NORM_1D)
print_metrics_info('diff norm recovery', RECOVERY_RATE_NORM_1D)


# pearson

print('---')
print('pearson')
# print('raw', sp.pearsonr(CASE_RATE_RAW.values(), DEATH_RATE_RAW.values()))
print('diff', sp.pearsonr(CASE_RATE_DIFF, DEATH_RATE_DIFF))
print('norm diff', sp.pearsonr(CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D))