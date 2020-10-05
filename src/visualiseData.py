
import pandas as pd
import seaborn as sns
from IPython.display import display

path_to_csv1 = "../results_1.csv"
df1 = pd.read_csv(path_to_csv1)


path_to_csv2 = "../results_2.csv"
df2 = pd.read_csv(path_to_csv2)
df_ = pd.DataFrame()
df = pd.concat([df1, df_ ,df2])

cm = sns.light_palette("green", as_cmap=True)
th_props = [
    ('font-size', '11px'),
    ('text-align', 'center'),
    ('font-weight', 'bold'),
    ('color', '#6d6d6d'),
    ('background-color', '#f7f7f9')
]

td_props = [
    ('font-size', '11px')
]
styles = [
    dict(selector="th", props=th_props),
    dict(selector="td", props=td_props)
]

# df.style.background_gradient(cmap=cm, subset=['Average matched points','Average distance', 'Average process time(μs)'])\
#     .highlight_max(subset=['Average matched points','Average distance', 'Average process time(μs)'])\
#     .set_caption('This is a custom caption.')\
#     .set_table_styles(styles)
display(df)