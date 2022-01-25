#import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())
df_goals = pd.read_csv('goals.csv')
df['Total Goals'] = df['Home Team Goals']  + df['Away Team Goals']
print(df.head())

sns.set_style("whitegrid")
sns.set_context('notebook', font_scale=1.25)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(x= df['Year'], y= df['Total Goals'])
ax.set_title("Bar plot of goals in World Cup")
plt.show()

f, ax2 = plt.subplots(figsize =(12, 7))
ax2 = sns.boxplot(x='year', y='goals', data=df_goals, palette = 'Spectral')
ax2.set_title('Box Plot Of Goals.')
plt.show()
print(df_goals.head())