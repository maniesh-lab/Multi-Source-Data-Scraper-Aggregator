import pandas as pd

def merge_datasets(*dfs):
    
    combined_df = pd.concat(dfs,ignore_index=True)

    return combined_df
