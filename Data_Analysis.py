

import pandas as pd

# Read the text file into a pandas dataframe
df = pd.read_csv('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/Amazon_Process2_Output/part-00000', sep='\t', header=None)

# Display the first five rows of the dataframe
header = ['Product Id', 'Number of Issue Reviews']

df.columns = header
# print(df.head())
df[['Product', 'Issue']] = df['Product Id'].str.split('-', expand=True)
df.drop('Product Id', axis=1, inplace=True)
df = df.reindex(columns=['Product', 'Issue', 'Number of Issue Reviews'])
# Print the updated dataframe



df_negative = pd.read_csv('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/negative_data.csv')


grouped_df = df_negative.groupby('asin').size().reset_index(name='Total Number of Reviews')
# print(grouped_df)
merged_df = pd.merge(grouped_df, df, left_on='asin', right_on='Product', how='inner')
df_sorted = merged_df.sort_values(['asin'],ascending=False)

# display the merged dataframe


df_sorted['Percentage of Issue review'] = 100 * df_sorted['Number of Issue Reviews'] / df_sorted['Total Number of Reviews']
# print the updated DataFrame
df_sorted.drop('Product', axis=1, inplace=True)
df_sorted = df_sorted.reindex(columns=['asin', 'Issue','Total Number of Reviews', 'Number of Issue Reviews','Percentage of Issue review'])
print(df_sorted.head())
