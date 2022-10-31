#------------------------------------------#
# Developed by: Arjan
# Adapted by: Thiago Piovesan
# Video link: https://youtu.be/GlRauKqI08Y
#------------------------------------------#
# Library importation:
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from src.data.loader import load_transaction_data

from src.components.layout import create_layout

DATA_PATH = "./data/transactions.csv"

def main() -> None:
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
