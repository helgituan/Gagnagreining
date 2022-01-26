import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import pandas as pd
import requests
import seaborn as sns
#from mpl_toolkits.basemap import Basemap
from wordcloud import WordCloud
import json

df = pd.read_json('earthquake.json')
df.info()