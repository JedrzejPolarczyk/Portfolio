from datetime import datetime, timedelta
import yfinance as yf
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


# Funkcja do pobierania danych z serwisu Yahoo Finance
def download_data(symbol, start_date, end_date, interval="1h"):
    data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    return data


# Klasa do tworzenia interaktywnej aplikacji Dash
class FinancialApp:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.start_date = datetime.today() - timedelta(days=5)
        self.end_date = datetime.today()
        self.selected_interval = "1h"  # Domyślny interwał

        self.symbols = {
            'usdpln': "USDPLN=X",
            'eurpln': "EURPLN=X",
            'chfpln': "CHFPLN=X",
            'ethbtc': "ETH-BTC",
            'bz': "BZ=F",
            'cl': "CL=F"
        }
#Funkcja do zmieniania interwałów w wykresach na wybrany przez użytkownika
    def download_all_data(self):
        data = {}
        for key, symbol in self.symbols.items():
            if self.selected_interval == '1d':
                data[key] = download_data(symbol, self.start_date - timedelta(days=90), self.end_date, interval="1d")
            elif self.selected_interval == '1wk':
                data[key] = download_data(symbol, self.start_date - timedelta(days=180), self.end_date,
                                          interval="1wk")
            elif self.selected_interval == '1mo':
                data[key] = download_data(symbol, self.start_date - timedelta(days=5 * 365), self.end_date,
                                          interval="1mo")
            else:
                data[key] = download_data(symbol, self.start_date, self.end_date, interval=self.selected_interval)
        return data

    # Funkcja do wybierania przez użytkownika interwałów w wykresach
    def create_layout(self):
        return html.Div([
            html.Div(children=[
                html.H1("Kursy wymiany z interwałami do wyboru Jędrzej Polarczyk",
                        style={'textAlign': 'center'}),
                dcc.RadioItems(
                    id='interval-selector',
                    options=[
                        {'label': '1 godzina', 'value': '1h'},
                        {'label': '1 dzień', 'value': '1d'},
                        {'label': '1 tydzień', 'value': '1wk'},
                        {'label': '1 miesiąc', 'value': '1mo'},
                    ],
                    value=self.selected_interval,
                    labelStyle={'display': 'block'}
                )
            ], style={'backgroundColor': '#3bf76d', 'padding': '20px'}),

            dcc.Graph(
                id='plnx-graph',
                figure=self.create_plnx_figure()
            ),

            dcc.Graph(
                id='eth-btc-graph',
                figure=self.create_ethbtc_figure()
            ),

            dcc.Graph(
                id='bz-graph',
                figure=self.create_bz_figure()
            )
        ], style={'backgroundColor': '#3bf76d', 'padding': '20px'})
#Tworzenie wykresu dla cen USD, EUR, CHF w PLN
    def create_plnx_figure(self):
        usdpln_data = self.downloaded_data['usdpln']
        eurpln_data = self.downloaded_data['eurpln']
        chfpln_data = self.downloaded_data['chfpln']

        return {
            'data': [
                {'x': usdpln_data.index, 'y': usdpln_data['Open'], 'type': 'line', 'name': 'USD do PLN'},
                {'x': eurpln_data.index, 'y': eurpln_data['Open'], 'type': 'line', 'name': 'EUR do PLN'},
                {'x': chfpln_data.index, 'y': chfpln_data['Open'], 'type': 'line', 'name': 'CHF do PLN'}
            ],
            'layout': {
                'title': 'Kurs wymiany USD, EUR i CHF do PLN',
                'xaxis': {'title': 'Data'},
                'yaxis': {'title': 'Kurs wymiany'},
                'plot_bgcolor': '#f2f2f2'
            }
        }

    # Tworzenie wykresu dla ETH do BTC
    def create_ethbtc_figure(self):
        ethbtc_data = self.downloaded_data['ethbtc']

        return {
            'data': [
                {'x': ethbtc_data.index, 'y': ethbtc_data['Open'], 'type': 'line', 'name': 'ETH do BTC'}
            ],
            'layout': {
                'title': 'Kurs wymiany ETH do BTC',
                'xaxis': {'title': 'Data'},
                'yaxis': {'title': 'Kurs wymiany'},
                'plot_bgcolor': '#f2f2f2'
            }
        }

    # Tworzenie wykresu dla cen ropy naftowej
    def create_bz_figure(self):
        bz_data = self.downloaded_data['bz']
        cl_data = self.downloaded_data['cl']

        return {
            'data': [
                {'x': bz_data.index, 'y': bz_data['Open'], 'type': 'line', 'name': 'Brent Crude Oil'},
                {'x': cl_data.index, 'y': cl_data['Open'], 'type': 'line', 'name': 'WTI Crude Oil'}
            ],
            'layout': {
                'title': 'Porównanie Brent Crude Oil oraz West Texas Intermediate Crude Oil',
                'xaxis': {'title': 'Data'},
                'yaxis': {'title': 'Cena USD'},
                'plot_bgcolor': '#f2f2f2'
            }
        }
#Funkcja aktualizująca interwały
    def update_interval(self, selected_interval):
        self.selected_interval = selected_interval
        self.downloaded_data = self.download_all_data()
#Funkcja włączająca aplikacje
    def run_app(self):
        self.downloaded_data = self.download_all_data()
        self.app.layout = self.create_layout()

        # Obsługa interwału
        @self.app.callback(
            Output('plnx-graph', 'figure'),
            Output('eth-btc-graph', 'figure'),
            Output('bz-graph', 'figure'),
            Input('interval-selector', 'value')
        )
        def update_graphs(selected_interval):
            self.update_interval(selected_interval)
            return self.create_plnx_figure(), self.create_ethbtc_figure(), self.create_bz_figure()

        self.app.run_server(debug=True)


if __name__ == '__main__':
    financial_app = FinancialApp()
    financial_app.run_app()
