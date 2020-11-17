import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('/home/art/datasets/csv_for_map.csv')

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