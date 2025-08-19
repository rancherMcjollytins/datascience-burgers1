import matplotlib.pyplot as plt
import pandas as pd

#Read in the big_mac_update dataset to big_mac_df DataFrame
big_mac_df = pd.read_csv("data/big_mac_aud.csv",header=None)

#Create the plot using big_mac_df
big_mac_df.plot(kind='scatter',x='0',y='1',color='blue',alpha=0.3,title='test')

#Show the plot
plt.show()