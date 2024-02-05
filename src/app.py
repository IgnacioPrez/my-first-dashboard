import pandas as pd
import plotly.express as px
from dash import Dash, dash_table, dcc, callback, Output, Input
import dash_mantine_components as dmc

df = pd.read_csv("./files/student-mat.csv", delimiter=";")

app = Dash(__name__)

app.layout = dmc.Container(
    [
        dmc.Title(
            "Student achievement in secondary education of two Portuguese schools",
            order=1,
            color="#191E27",
            mb=15,
        ),
        dmc.Container(
            style={"width": "60vw", "overflow-x": "scroll", "marginBottom": 15},
            children=[
                dash_table.DataTable(
                    id="data-table",
                    columns=[{"name": col, "id": col} for col in df.columns],
                    data=df.to_dict("records"),
                    page_size=10,
                ),
            ],
        ),
        dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ["sex", "reason","internet","paid"]],
            id="my-dmc-radio-item",
            value="sex",
            size="sm",
            style={"marginBottom": 15, "marginTop": 10},
        ),
        dcc.Graph(figure={}, id="graph-placeholder"),
    ]
)


@callback(
    Output(component_id="graph-placeholder", component_property="figure"),
    Input(component_id="my-dmc-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    print(col_chosen)
    fig = px.histogram(
        df, x="age", y=col_chosen, color="age", text_auto=True, opacity=0.75
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
