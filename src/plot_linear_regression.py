from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math


# # slope, intercept = custom_devised_regression(x,y)
# def custom_devised_regression(x,y):
#     n = np.size(x)
#     m_x, m_y = np.median(x), np.median(y)
#     SS_xy = np.sum(y**2 * x**2) - n * m_y * m_x
#     SS_xx = np.sum(x**4) - n * m_x * m_x
#     b_1 = SS_xy / SS_xx
#     b_0 = m_y - b_1 * m_x
#     return (b_1,b_0)


from normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST


def main():
    x = np.array(list(range(0, len(DATE_RAW))))  # timeline

    y = np.array(POPULATION_NORM_1D)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    curve = intercept + slope * x
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='instances')
    plt.plot(x, curve, 'r', label='forecast')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Population')
    plt.title('Population during COVID-19')
    plt.savefig('output/forecast-population-diff-sqrt-norm.png')

    y = np.array(CASE_RATE_NORM_1D)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    curve = intercept + slope * x
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='instances')
    plt.plot(x, curve, 'r', label='forecast')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Cases')
    plt.title('Cases of COVID-19')
    plt.savefig('output/forecast-cases-diff-sqrt-norm.png')

    y = np.array(DEATH_RATE_NORM_1D)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    curve = intercept + slope * x
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='instances')
    plt.plot(x, curve, 'r', label='forecast')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Death')
    plt.title('Death of COVID-19')
    plt.savefig('output/forecast-death-diff-sqrt-norm.png')

    y = np.array(RECOVERY_RATE_NORM_1D)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    curve = intercept + slope * x
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='instances')
    plt.plot(x, curve, 'r', label='forecast')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Recovery')
    plt.title('Recovery of COVID-19')
    plt.savefig('output/forecast-recovery-diff-sqrt-norm.png')

    y = np.array(RECOVERY_RATE_DIFF)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    curve = intercept + slope * x
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='instances')
    plt.plot(x, curve, 'r', label='forecast')
    plt.legend()
    plt.xlabel('Timeline')
    plt.ylabel('Recovery')
    plt.title('Recovery of COVID-19')
    plt.savefig('output/recovery-linear-regression.png')

if __name__ == '__main__':
    main()