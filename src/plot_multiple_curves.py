from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

from src.normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST



def main():
    x = np.arange(len(DATE_RAW.values()))


    y1 = np.array(POPULATION_RATE_DIFF)
    y2 = np.array(DEATH_RATE_DIFF)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y1, label='population')
    plt.plot(x, y2, 'r', label='death')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Rate')
    plt.title('Population and Death Rate of COVID-19')
    plt.savefig('output/population_and_death_diff.png')
    # plt.show()


    y1 = np.array(CASE_RATE_DIFF)
    y2 = np.array(DEATH_RATE_DIFF)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y1, label='case')
    plt.plot(x, y2, 'r', label='death')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Rate')
    plt.title('Cases and Death Rate of COVID-19')
    plt.savefig('output/cases_and_death_diff.png')
    # plt.show()


if __name__ == '__main__':
    main()