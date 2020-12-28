from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

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


case_death_tuples = []
for state in CASES_BY_STATE:
    case_death_tuples.append((DEATH_BY_STATE[state], CASES_BY_STATE[state]))

X = np.array(case_death_tuples)

n_clusters = 2
clusterer = KMeans(n_clusters=n_clusters, random_state=10)
cluster_labels = clusterer.fit_predict(X)

colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
plt.scatter(X[:, 0], X[:, 1], marker='X', s=30, lw=0, alpha=0.7, c=colors, edgecolor='k')
plt.scatter(clusterer.cluster_centers_[:, 0], clusterer.cluster_centers_[:, 1], marker='o', c="white", alpha=1, s=200, edgecolor='k')

for state in CASES_BY_STATE:
    plt.annotate(state, xy=(DEATH_BY_STATE[state], CASES_BY_STATE[state]))

for i, c in enumerate(clusterer.cluster_centers_):
    plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50, edgecolor='k')

plt.title("USA states COVID-19 Cluster")
plt.xlabel("Death")
plt.ylabel("Cases")
plt.savefig('output/cluster.png')
plt.show()

