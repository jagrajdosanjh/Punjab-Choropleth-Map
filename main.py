import pandas as pd
import json
import plotly.express as px
punjab_districts = json.load(open("punjabHigh.json", "r"))  # r as in read
state_id_map = {}
for feature in punjab_districts['features']:
    feature['id'] = feature['properties']['id']
    state_id_map[feature['properties']['name']] = feature['id']
state_id_map
punjab_districts['features'][2]['properties']
df = pd.read_excel("data/data.xlsx")
df['id'] = df['District'].map(state_id_map)
df.head()
fig = px.choropleth(df, locations='id', geojson="punjabHigh.json",
                    color="Extrajudicial Executions", scope="asia")
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
