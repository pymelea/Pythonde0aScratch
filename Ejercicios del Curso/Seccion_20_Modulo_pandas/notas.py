import pandas as pd

import webbrowser

website = 'https://es.wikipedia.org/wiki/National_Basketball_Association'
webbrowser.open(website)

dataframe_nba = pd.read_clipboard()
print(dataframe_nba) 
