#------------------------------------------#
# Developed by: Arjan
# Adapted by: Thiago Piovesan
# Video link: https://youtu.be/XOFrvzWFM7Y
#------------------------------------------#
# Library importation:
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout

def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Medal dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
