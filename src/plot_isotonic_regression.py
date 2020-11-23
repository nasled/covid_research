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

from src.normalization import CASE_RATE_RAW

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
