import os
import dash
from dash import dcc, html
import requests

# Use the correct backend URL
BACKEND_URL = os.getenv("BACKEND_URL", "https://backend-axfy.onrender.com")

app = dash.Dash(__name__)

def get_cohorts():
    response = requests.get(f"{BACKEND_URL}/cohorts")
    return response.json() if response.status_code == 200 else []

app.layout = html.Div([
    html.H1("Cohort Knowledgebase"),
    html.Ul(id="cohort-list")
])

@app.callback(
    dash.Output("cohort-list", "children"),
    dash.Input("cohort-list", "id")
)
def update_list(_):
    cohorts = get_cohorts()
    return [html.Li(cohort["name"]) for cohort in cohorts]

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
