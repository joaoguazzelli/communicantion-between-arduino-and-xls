import pandas as pd
import webbrowser


def export_to_html():
    wb = pd.read_excel('dados_ard.xlsx')
    wb.to_html('teste.html')
    webbrowser.open('teste.html')
