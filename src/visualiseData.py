
import pandas as pd

path_to_csv = "../cmake-build-release/results_final.csv"
df = pd.read_csv(path_to_csv)
print(df)