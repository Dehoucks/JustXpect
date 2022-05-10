import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash import dcc
from dash import Dash, html, Input, Output, callback_context
import main

app = Dash(__name__)

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Just Xpect",
    brand_href="#",
    color="primary",
    dark=True,
)


content_second_row = html.Div([
dcc.Dropdown(
    ['New York City', 'Montreal', 'San Francisco'],
    ['Montreal', 'San Francisco'],
    multi=True
)
], style={'margin-top' : '10%', 'margin-right' : '33%', 'margin-left' : '33%',  'width': '34%', 'display': 'inline-block', 'textAlign' : 'center'}
),

content_second_row = html.Div([
    html.P("D'où venez-vous ?"),
    dcc.Dropdown(['Nord (59)', 'Paris (75)', 'Bouches-du-Rhône (13)', 'Rhône (69)', 'Seine-Saint-Denis (93)', 'Hauts-de-Seine (92)', 'Gironde (33)', 'Pas-de-Calais (62)', 'Yvelines (78)', 'Seine-et-Marne (77)', 'Loire-Atlantique (44)', 'Val-de-Marne (94)', 'Haute-Garonne (31)', 'Essonne (91)', 'Isère (38)', 'Seine-Maritime (76)', "Val-d'Oise (95)", 'Hérault (34)', 'Bas-Rhin (67)', 'Alpes-Maritimes (06)', 'Ille-et-Vilaine (35)', 'Var (83)', 'Moselle (57)', 'Finistère (29)', 'Oise (60)', 'Maine-et-Loire (49)', 'Haute-Savoie (74)', 'Haut-Rhin (68)', 'Loire (42)', 'Morbihan (56)', 'Gard (30)', 'Meurthe-et-Moselle (54)', 'Calvados (14)', 'Loiret (45)', 'Pyrénées-Atlantiques (64)', 'Vendée (85)', 'Puy-de-Dôme (63)', 'Charente-Maritime (17)', 'Ain (01)', 'Indre-et-Loire (37)', 'Eure (27)', "Côtes-d'Armor (22)", 'Somme (80)', 'Marne (51)', 'Sarthe (72)', 'Vaucluse (84)', 'Saône-et-Loire (71)', 'Doubs (25)', 'Aisne (02)', "Côte-d'Or (21)", 'Drôme (26)', 'Manche (50)', 'Pyrénées-Orientales (66)', 'Vienne (86)', 'Eure-et-Loir (28)', 'Savoie (73)', 'Dordogne (24)', 'Landes (40)', 'Tarn (81)', 'Haute-Vienne (87)', 'Deux-Sèvres (79)', 'Aude (11)', 'Vosges (88)', 'Charente (16)', 'Yonne (89)', 'Allier (03)', 'Lot-et-Garonne (47)', 'Loir-et-Cher (41)', 'Ardèche (07)', 'Aube (10)', 'Mayenne (53)', 'Cher (18)', 
'Orne (61)', 'Aveyron (12)', 'Ardennes (08)', 'Jura (39)', 'Tarn-et-Garonne (82)', 'Corrèze (19)', 'Haute-Saône (70)', 'Hautes-Pyrénées (65)', 'Haute-Loire (43)', 'Indre (36)', 'Nièvre (58)', 'Gers (32)', 'Meuse (55)', 'Haute-Corse (2B)', 'Haute-Marne (52)', 'Lot (46)', 'Alpes-de-Haute-Provence (04)', 'Corse-du-Sud (2A)', 'Ariège (09)', 'Cantal (15)', 
'Territoire-de-Belfort (90)', 'Hautes-Alpes (05)', 'Creuse (23)', 'Lozère (48)'], id='demo-dropdown1', style = {'margin-top' : ' 10px'}),
    
    html.P("Quel est votre métier ?", style = {'margin-top' : ' 10px'}),
    dcc.Dropdown(['Développeur web', 'Chef de projet', 'Auditeur financer', 'Webmaster', 'Directeur Artistique', 'Ingénieur Biologie', 
'Cuisinier', 'Data Scientist', 'Designer', 'Agent de sécurité'], id='demo-dropdown2', style = {'margin-top' : ' 10px'}),
    html.P("Quel est votre niveau d'expérience ?", style = {'margin-top' : ' 10px'}),
    dcc.Dropdown(['0', '1', '2', '3', '4' , 'Senior'], id='demo-dropdown3'),
    dbc.Button("Recherche", color="primary", className="me-1", n_clicks=0, id = 'button', style = {'margin-top' : '5px'}),
], style={'margin-top' : '5%', 'margin-right' : '33%', 'margin-left' : '33%',  'width': '34%', 'display': 'inline-block', 'textAlign' : 'center'})

content_third_row = html.Div(children = [
    dbc.Card(
    dbc.CardBody(
        [
            html.H5("Voici le salaire auquel vous pouvez prétendre.", className="card-title"),
            html.P(f"Veuillez remplir vos informations ci-dessus.", id = 'salary_text1'),
            html.P(f"", id = 'salary_text2'),
            dcc.Input(id="input2", type="Email", placeholder="email", debounce=True),
            dbc.Button("Drop CV", color="primary", style = {'margin-left' : '10%'}),
        ]
    )
)
], style= {'margin-top' : '10px', 'display': 'none'}, id = 'salary_block')


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    navbar,
    content_second_row,
    content_third_row
])

@app.callback(
    Output('salary_text1', 'children'),
    Output('salary_text2', 'children'),
    Output(component_id='salary_block', component_property='style'),
    Input('button', 'n_clicks'),
    Input('demo-dropdown1', 'value'),
    Input('demo-dropdown2', 'value'),
    Input('demo-dropdown3', 'value')
)
def update_output(n_click, department, work_name, year_experience):
    print(n_click)
    if n_click != 0:
        low_salary, high_salary = main.algo(work_name, department, year_experience)
        print(low_salary, high_salary)
    return f'Fourchette basse: {low_salary}€ brut annuel.', f'Fourchette haute: {high_salary}€ brut annuel.', {'display': 'block'}



if __name__ == "__main__":
    app.run_server(debug=False)