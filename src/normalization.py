import matplotlib.pyplot as plt


'''
* DIFF ALGORITHM
This algorithm is used to get rid of linear function 
'''
def set_difference(data_dict):
    difference = []
    dates = list(data_dict.keys())
    for i in range(len(data_dict)):
        # define ranges
        cur_date = dates[i]
        next_date = dates[i + 1]

        # in first day we add zero day
        if i == 0:
            difference.append(data_dict[cur_date])

        buffer = data_dict[next_date] - data_dict[cur_date]
        difference.append(buffer)

        # stop iteration
        if i + 2 == len(data_dict):
            break

    # we normalize data head if difference reach threshold
    threshold = 100000
    if difference[0] - difference[1] > threshold:
        difference[0] = difference[1]

    return difference

'''
Reduce numbers to float to store ratio
'''
def normalize_set(list):
    import math
    result = []
    for i in list:
        value = math.sqrt(i)
        result.append(value)
    # print(result)
    return result


'''
normalize_to_float using the square root of x in degree
'''
def normalize_to_degree(list, degree = 1, as_list = True):
    import math
    result = []
    for i in list:
        for j in range(0, degree):
            i = math.sqrt(i)
        if as_list:
            result.append(i)
        else:
            result.append([i])
    return result

from src.parse_dataset import CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW

POPULATION_RATE_DIFF = set_difference(POPULATION_RATE_RAW)
CASE_RATE_DIFF = set_difference(CASE_RATE_RAW)
DEATH_RATE_DIFF = set_difference(DEATH_RATE_RAW)
RECOVERY_RATE_DIFF = set_difference(RECOVERY_RATE_RAW)

POPULATION_NORM_1D = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 1)
CASE_RATE_NORM_1D = normalize_to_degree(set_difference(CASE_RATE_RAW), 1)
DEATH_RATE_NORM_1D = normalize_to_degree(set_difference(DEATH_RATE_RAW), 1)
RECOVERY_RATE_NORM_1D = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 1)

POPULATION_NORM_1D_LIST = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 1, False)
CASE_RATE_NORM_1D_LIST = normalize_to_degree(set_difference(CASE_RATE_RAW), 1, False)
DEATH_RATE_NORM_1D_LIST = normalize_to_degree(set_difference(DEATH_RATE_RAW), 1, False)
RECOVERY_RATE_NORM_1D_LIST = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 1, False)

POPULATION_NORM_3D = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 3)
CASE_RATE_NORM_3D = normalize_to_degree(set_difference(CASE_RATE_RAW), 3)
DEATH_RATE_NORM_3D = normalize_to_degree(set_difference(DEATH_RATE_RAW), 3)
RECOVERY_RATE_NORM_3D = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 3)

POPULATION_NORM_3D_LIST = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 3, False)
CASE_RATE_NORM_3D_LIST = normalize_to_degree(set_difference(CASE_RATE_RAW), 3, False)
DEATH_RATE_NORM_3D_LIST = normalize_to_degree(set_difference(DEATH_RATE_RAW), 3, False)
RECOVERY_RATE_NORM_3D_LIST = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 3, False)

POPULATION_NORM_5D = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 5)
CASE_RATE_NORM_5D = normalize_to_degree(set_difference(CASE_RATE_RAW), 5)
DEATH_RATE_NORM_5D = normalize_to_degree(set_difference(DEATH_RATE_RAW), 5)
RECOVERY_RATE_NORM_5D = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 5)

POPULATION_NORM_5D_LIST = normalize_to_degree(set_difference(POPULATION_RATE_RAW), 5, False)
CASE_RATE_NORM_5D_LIST = normalize_to_degree(set_difference(CASE_RATE_RAW), 5, False)
DEATH_RATE_NORM_5D_LIST = normalize_to_degree(set_difference(DEATH_RATE_RAW), 5, False)
RECOVERY_RATE_NORM_5D_LIST = normalize_to_degree(set_difference(RECOVERY_RATE_RAW), 5, False)


def main():
    print('generating output... ')

    # raw data

    plt.figure(figsize=(12, 12))
    plt.plot(POPULATION_RATE_RAW.keys(), POPULATION_RATE_RAW.values())
    plt.xlabel('Date')
    plt.ylabel('Population')
    plt.title('Population/Date of COVID-19')
    plt.savefig('output/population.png')

    plt.figure(figsize=(12, 12))
    plt.plot(CASE_RATE_RAW.keys(), CASE_RATE_RAW.values())
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.title('Cases/Date of COVID-19')
    plt.savefig('output/cases.png')

    plt.figure(figsize=(12, 12))
    plt.plot(DEATH_RATE_RAW.keys(), DEATH_RATE_RAW.values())
    plt.xlabel('Date')
    plt.ylabel('Death')
    plt.title('Death/Date of COVID-19')
    plt.savefig('output/death.png')

    plt.figure(figsize=(12, 12))
    plt.plot(RECOVERY_RATE_RAW.keys(), RECOVERY_RATE_RAW.values())
    plt.xlabel('Date')
    plt.ylabel('Recovery')
    plt.title('Recovery/Date of COVID-19')
    plt.savefig('output/recovery.png')


    # applied DIFF algo

    plt.figure(figsize=(12, 12))
    plt.plot(POPULATION_RATE_RAW.keys(), POPULATION_RATE_DIFF)
    plt.xlabel('Date')
    plt.ylabel('Population-Diff')
    plt.title('Population-Diff/Date of COVID-19')
    plt.savefig('output/population-diff.png')

    plt.figure(figsize=(12, 12))
    plt.plot(CASE_RATE_RAW.keys(), CASE_RATE_DIFF)
    plt.xlabel('Date')
    plt.ylabel('Cases-Diff')
    plt.title('Cases-Diff/Date of COVID-19')
    plt.savefig('output/cases-diff.png')

    plt.figure(figsize=(12, 12))
    plt.plot(DEATH_RATE_RAW.keys(), DEATH_RATE_DIFF)
    plt.xlabel('Date')
    plt.ylabel('Death-Diff')
    plt.title('Death-Diff/Date of COVID-19')
    plt.savefig('output/death-diff.png')

    plt.figure(figsize=(12, 12))
    plt.plot(RECOVERY_RATE_RAW.keys(), RECOVERY_RATE_DIFF)
    plt.xlabel('Date')
    plt.ylabel('Recovery-Diff')
    plt.title('Recovery-Diff/Date of COVID-19')
    plt.savefig('output/recovery-diff.png')


    # applied Square normalization algorithm

    plt.figure(figsize=(12, 12))
    plt.plot(POPULATION_RATE_RAW.keys(), POPULATION_NORM_1D)
    plt.xlabel('Date')
    plt.ylabel('Population-Diff-Norm')
    plt.title('Population-Diff-Norm/Date of COVID-19')
    plt.savefig('output/population-diff-sqrt-norm.png')

    plt.figure(figsize=(12, 12))
    plt.plot(CASE_RATE_RAW.keys(), CASE_RATE_NORM_1D)
    plt.xlabel('Date')
    plt.ylabel('Cases-Diff-Norm')
    plt.title('Cases-Diff-Norm/Date of COVID-19')
    plt.savefig('output/cases-diff-sqrt-norm.png')

    plt.figure(figsize=(12, 12))
    plt.plot(DEATH_RATE_RAW.keys(), DEATH_RATE_NORM_1D)
    plt.xlabel('Date')
    plt.ylabel('Death-Diff-Norm')
    plt.title('Death-Diff-Norm/Date of COVID-19')
    plt.savefig('output/death-diff-sqrt-norm.png')

    plt.figure(figsize=(12, 12))
    plt.plot(RECOVERY_RATE_RAW.keys(), RECOVERY_RATE_NORM_1D)
    plt.xlabel('Date')
    plt.ylabel('Recovery-Diff-Norm')
    plt.title('Recovery-Diff-Norm/Date of COVID-19')
    plt.savefig('output/recovery-diff-sqrt-norm.png')

    print('generated')

if __name__ == '__main__':
    main()