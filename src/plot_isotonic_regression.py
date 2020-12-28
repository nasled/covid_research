import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state


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



y = RECOVERY_RATE_DIFF
n = len(y)
x = np.arange(n)

ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0, colors='green')
fig = plt.figure()

plt.plot(x, y, 'b.', markersize=5)
plt.plot(x, y_, 'g-', markersize=5)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'r')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('COVID-19 Trend')
plt.xlabel('Timeline')
plt.ylabel('Rate')
plt.savefig('output/recovery_isotonic_regression.png')
# plt.show()


y = DEATH_RATE_DIFF
n = len(y)
x = np.arange(n)

ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0, colors='green')
fig = plt.figure()

plt.plot(x, y, 'b.', markersize=5)
plt.plot(x, y_, 'g-', markersize=5)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'r')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('COVID-19 Trend')
plt.xlabel('Timeline')
plt.ylabel('Rate')
plt.savefig('output/death_isotonic_regression.png')
# plt.show()


y = CASE_RATE_DIFF
n = len(y)
x = np.arange(n)

ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0, colors='green')
fig = plt.figure()

plt.plot(x, y, 'b.', markersize=5)
plt.plot(x, y_, 'g-', markersize=5)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'r')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('COVID-19 Trend')
plt.xlabel('Timeline')
plt.ylabel('Rate')
plt.savefig('output/case_isotonic_regression.png')
# plt.show()