import reflex as rx


data01 = [
    {"name": "Group A", "value": 400},
    {"name": "Group B", "value": 300, "fill": "#AC0E08FF"},
    {"name": "Group C", "value": 300, "fill": "rgb(80,40, 190)"},
    {"name": "Group D", "value": 200, "fill": rx.color("yellow", 10)},
    {"name": "Group E", "value": 278, "fill": "purple"},
    {"name": "Group F", "value": 189, "fill": "orange"},
]


def pie_simple():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            label=True,
        ),
        width="100%",
        height=300,
    )
