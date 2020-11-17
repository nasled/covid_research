"""
===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.

"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state



from normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST


y = CASE_RATE_RAW
n = len(y)
x = np.arange(n)



# #############################################################################
# Fit IsotonicRegression and LinearRegression models
ir = IsotonicRegression()
y_ = ir.fit_transform(x, y)
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression

# #############################################################################
# Plot result
segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0, colors='green')
# lc.set_array(np.ones(len(y)))
# lc.set_linewidths(np.full(n, 0.5))

fig = plt.figure()
plt.plot(x, y, 'b.', markersize=5)
plt.plot(x, y_, 'g-', markersize=5)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'r')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('COVID-19 Trend')
plt.xlabel('Timeline')
plt.ylabel('Rate')
plt.savefig('output/isotonic_regression.png')
plt.show()
