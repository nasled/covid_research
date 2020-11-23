import matplotlib.pyplot as plt
import numpy as np

from src.normalization import DATE_RAW, POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF


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
    plt.show()


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
    plt.show()


if __name__ == '__main__':
    main()