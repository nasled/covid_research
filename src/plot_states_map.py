import plotly.graph_objects as go
import pandas as pd

from src.config import MAIN_DATASET_PATH, STATES_DATASET_PATH, GEOCODES_DATASET_PATH, \
                   CDC_ENDPOINT_URL, CENSUS_ENDPOINT_URL
from src.normalization import DATE_RAW, CASE_RATE_RAW, DEATH_RATE_RAW, RECOVERY_RATE_RAW, POPULATION_RATE_RAW,\
                          CASES_BY_STATE, DEATH_BY_STATE, RECOVERY_BY_STATE,\
                          POPULATION_RATE_DIFF, CASE_RATE_DIFF, DEATH_RATE_DIFF, RECOVERY_RATE_DIFF,\
                          POPULATION_NORM_1D, CASE_RATE_NORM_1D, DEATH_RATE_NORM_1D, RECOVERY_RATE_NORM_1D,\
                          POPULATION_NORM_1D_LIST, CASE_RATE_NORM_1D_LIST, DEATH_RATE_NORM_1D_LIST, RECOVERY_RATE_NORM_1D_LIST,\
                          POPULATION_NORM_3D, CASE_RATE_NORM_3D, DEATH_RATE_NORM_3D, RECOVERY_RATE_NORM_3D,\
                          POPULATION_NORM_3D_LIST, CASE_RATE_NORM_3D_LIST, DEATH_RATE_NORM_3D_LIST, RECOVERY_RATE_NORM_3D_LIST, \
                          POPULATION_NORM_5D, CASE_RATE_NORM_5D, DEATH_RATE_NORM_5D, RECOVERY_RATE_NORM_5D, \
                          POPULATION_NORM_5D_LIST, CASE_RATE_NORM_5D_LIST, DEATH_RATE_NORM_5D_LIST, RECOVERY_RATE_NORM_5D_LIST

df = pd.read_csv(STATES_DATASET_PATH)

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['recovery'].astype(float),
    locationmode='USA-states',
    colorscale='haline',
    colorbar_title='Rate',
))

fig.update_layout(
    title_text='COVID-19 States by Recovery',
    geo_scope='usa',
)

fig.show()