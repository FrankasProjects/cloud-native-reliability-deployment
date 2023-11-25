import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# descriptive statistics
df_res = pd.read_csv('QuantitativeAnalysis/resultset/resultset.csv')
df_stacked = pd.read_csv('QuantitativeAnalysis/stacked/stacked.csv')

max_year =df_res['Year'].max()
min_year =df_res['Year'].min()

# normal barplot

val, cnt = np.unique(df_res['Year'], return_counts=True)
plt.bar(val, cnt)
plt.show()

# stacked barplot

# group based on publication types
jour_counts = df_stacked[df_stacked['Publication Type'] == 'Journal'].groupby('Year').size().reset_index(name='Journal Count')
# fill in not counted years with 0
all_years = pd.DataFrame({'Year': range(df_stacked['Year'].min(), df_stacked['Year'].max() + 1)})
journal_counts = pd.merge(all_years, jour_counts, on='Year', how='left').fillna(0)

conf_counts = df_stacked[df_stacked['Publication Type'] == 'Conference'].groupby('Year').size().reset_index(name='Conference Count')
all_years = pd.DataFrame({'Year': range(df_stacked['Year'].min(), df_stacked['Year'].max() + 1)})
conference_counts = pd.merge(all_years, conf_counts, on='Year', how='left').fillna(0)


# plot bars in stack manner
plt.bar(all_years['Year'], conference_counts['Conference Count'], color='tab:orange', label="Conferences")
plt.bar(all_years['Year'], journal_counts['Journal Count'], bottom=conference_counts['Conference Count'], color='tab:blue', label="Journals")
plt.legend(loc='upper right')
plt.show()