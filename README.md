# covid_research
Research of COVID-19 impact and trend in USA using statistical approach

The repository contains code source, paper source and presentation files of the COVID-19 research across USA and states based on public data from https://cdc.gov.

#### Source Code Execution

The source code described in start execution priority.
 
```
fetch_covid_dataset.py
```
Downloads the dataset and saves result to local path.

```
parse_dataset.py
```
Parses downloaded dataset and creates data structures.

```
fetch_population.py
```
Parses population from endpoint and saves result to local path.

```
normalization.py
```
Applies date difference algorithm, performs square root normalization and generates image plots for result values. 

```
meta_statistics_info.py
```
Saves statistical information form data structures' values.

```
classifier.py
```
Classifies states based on mean-feature and saves result to local path.

```
plot_linear_regression.py
```
Generates trend results of linear model for population, cases, death and recovery metrics. 

```
plot_isotonic_regression.py   
```
Generates isotonic model visualization for cases, death and recovery metrics.

```
plot_multiple_curves.py
```
Generates impact plots between population/death and cases/death metrics.

```
plot_states_map.py
```
Generates density recovery figure of US states. 

```
plot_kmeans_cluster.py
```
Generates cluster of US states based on k-means algorithm.  

```
meta_state_to_fips.py
```
Maps state to fips codes.


#### Paper Build
```
make
```
Builds paper and saves to output folder. 

[CDC](https://cdc.gov)