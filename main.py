# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Incorporate data
df = pd.read_csv("Dash-Example/Spotify_Youtube.csv")
df_views = df.query("Views < 5000000 and Stream < 5000000")
df_views_opposite = df.query("Views > 500000000 and Stream > 500000000")

fig1 = px.density_heatmap(df, x="Danceability", y="Energy")
fig2 = px.parallel_categories(
    df[["Album_type", "Licensed", "official_video", "Stream"]],
    labels={"Album_type": "Type of Album", "official_video": "Official Video"},
)
fig3 = px.histogram(df_views, x="Views", color_discrete_sequence=["red"])
fig4 = px.histogram(
    df_views,
    x="Stream",
    labels={"Stream": "Streams"},
    color_discrete_sequence=["green"],
)
fig5 = px.density_heatmap(
    df_views,
    x="Views",
    y="Stream",
    labels={"Stream": "Streams"},
    color_continuous_scale="blugrn",
)
fig6 = px.scatter(
    df_views_opposite,
    x="Views",
    y="Stream",
    labels={"Stream": "Streams", "official_video": "Official Video"},
    color="official_video",
    hover_data=["Title"],
)


# Initialize the app and style
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div(
    [
        html.Div(
            children="Examining Popular Artist's Hit Songs on YouTube vs Spotify",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 35,
                "font-weight": "bold",
                "margin-bottom": "3%",
            },
        ),
        html.Div(
            children=[
                html.Div(
                    children="View counts of YouTube videos under 5M views",
                    style={
                        "textAlign": "auto",
                        "margin": "0px",
                        "color": "black",
                        "fontSize": 20,
                        "display": "inline-block",
                        "width": "50%",
                        "height": "50%",
                        "text-align": "center",
                    },
                ),
                html.Div(
                    children="Spotify streams for songs under 5M plays",
                    style={
                        "textAlign": "auto",
                        "margin": "0px",
                        "color": "black",
                        "fontSize": 20,
                        "display": "inline-block",
                        "width": "50%",
                        "height": "50%",
                        "text-align": "center",
                    },
                ),
                dcc.Graph(
                    figure=fig3,
                    style={"width": "50%", "height": "50%", "display": "inline-block"},
                    responsive=True,
                ),
                dcc.Graph(
                    figure=fig4,
                    style={"width": "50%", "height": "50%", "display": "inline-block"},
                    responsive=True,
                ),
            ]
        ),
        html.Div(
            children="YouTube view counts vs Spotify streams for songs with less than 5M plays",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 20,
                "margin": "0px",
            },
        ),
        dcc.Graph(figure=fig5),
        html.Div(
            children="YouTube view counts vs Spotify streams for songs with more than 500M plays",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 20,
                "margin": "0px",
            },
        ),
        dcc.Graph(figure=fig6),
        html.Div(
            children="Danceability vs Energy: Is there any correlation?",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 20,
                "margin": "0px",
            },
        ),
        dcc.Graph(figure=fig1),
        html.Div(
            children="Exploring Categorical Variables",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 20,
                "margin": "0px",
            },
        ),
        dcc.Graph(figure=fig2),
        html.Div(
            children="But what does all of this data mean?",
            style={
                "textAlign": "center",
                "color": "black",
                "fontSize": 35,
                "font-weight": "bold",
                "margin-bottom": "3%",
            },
        ),
        html.Div(
            children="It appears that YouTube videos are far more likely than Spotify streams to have less views about the same content. In other words, the same song uploaded to YouTube and Spotify is more likely to recieve greater attention on Spotify as opposed to YouTube.  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tempus ante magna. Curabitur vel neque sapien. Etiam sodales tincidunt turpis, a rutrum sem suscipit vel. Integer non sodales justo, in tempus risus. Integer varius egestas lectus vel semper. Morbi vitae convallis elit. Nullam finibus risus ut sapien egestas, feugiat tristique odio vehicula. Vivamus ultrices purus vitae orci laoreet, id euismod neque viverra. Maecenas in ullamcorper magna. Vivamus eu felis faucibus tortor semper finibus a vitae turpis. Nullam viverra velit quis bibendum luctus. Ut in odio euismod, congue mauris id, aliquet odio. Aenean a urna consectetur felis euismod lobortis vitae ac libero. Morbi vel nulla bibendum, vehicula sem id, varius ante. Nam condimentum eros volutpat posuere luctus. Curabitur a sapien consectetur, elementum nulla vitae, cursus lorem. Mauris nec aliquam mi. Phasellus nec tempus elit, quis efficitur diam. Donec sit amet urna quis dolor lobortis tincidunt vitae eget odio. Praesent aliquam molestie elit, eu dictum massa faucibus a. Ut in dictum justo, vel efficitur magna. Donec lacus turpis, tincidunt quis sodales et, consequat sit amet erat. Duis tincidunt erat ac urna tincidunt rhoncus. Quisque condimentum velit ut commodo semper. Fusce nec efficitur tortor. Nullam auctor mi vitae dui euismod, sit amet dignissim metus tincidunt. Fusce ac porta ligula. Vivamus id euismod ante. Donec vel metus vel risus faucibus ultrices. Sed pulvinar molestie erat eu feugiat. Cras aliquam ante eros, sed placerat lorem lobortis quis. Aliquam vel neque scelerisque, feugiat magna at, feugiat diam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas molestie erat felis, in elementum nibh viverra sed. Nullam commodo eleifend lobortis. Pellentesque lacinia vehicula elementum. Nunc dignissim maximus iaculis. Fusce aliquam feugiat urna vitae suscipit. In hac habitasse platea dictumst. Nam condimentum volutpat feugiat. Maecenas at elit eu odio lacinia dignissim vitae vel massa. Sed et luctus nisl. Integer dictum est tortor, eget faucibus nisl volutpat ac. In elementum ornare turpis in bibendum. Donec sodales mi quis mauris posuere malesuada. Morbi dictum risus ante. ",
            style={
                "color": "dark gray",
                "font-family": "Source Sans Pro",
                "font-size": "18px",
                "line-height": "32px",
                "margin-left": "12%",
                "margin-right": "12%",
            },
        ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
