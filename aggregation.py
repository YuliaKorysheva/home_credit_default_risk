import pandas as pd
from typing import Optional, List

def create_empty_data(data: pd.DataFrame) -> pd.DataFrame:
    '''Creates an empty file for further filling

    Args:
    data(pd.DataFrame) = data for creating indexes
    '''
    return pd.DataFrame({'SK_ID_CURR': data['SK_ID_CURR'].unique()}).set_index('SK_ID_CURR')

def aggregate_category_entries(data: pd.DataFrame, feature_for_aggregation: List[str]) -> pd.DataFrame:
    '''Aggregates characteristics by counting occurrences of individual categories
    Creates tags for each unique value for all categories. For each client, counts the number of each category.

    Args:
    data(pd.DataFrame) = aggregation data
    feature_for_aggregation(List[str]) = features to be aggregated
    '''
    d = create_empty_data(data)
    for feature in feature_for_aggregation:
        d = d.reindex(columns = d.columns.tolist() + list(data[feature].unique()))
        group = data.groupby(['SK_ID_CURR', feature]).count()
        for idx, idx_feature in group.index:
            d.loc[idx, idx_feature] = group['SK_ID_BUREAU'].loc[(idx, idx_feature)]

    return d

def aggregate_max_value(data: pd.DataFrame, feature_for_aggregation: List[str]) -> pd.DataFrame:
    '''Creates new characteristics based on the maximum values ​​of each characteristic

    Args:        
    data(pd.DataFrame) = aggregation data
    feature_for_aggregation(List[str]) = features to be aggregated
    '''
    d = create_empty_data(data)
    for feature in feature_for_aggregation:
        d = d.reindex(columns = d.columns.tolist() + [feature])
        group = data.groupby(['SK_ID_CURR'])[feature].max()
        for idx in group.index:
            d.loc[idx, feature] = group.loc[idx]
            
    return d.rename(columns=lambda x: x + '_MAX')

def aggregate_min_value(data: pd.DataFrame, feature_for_aggregation: List[str]) -> pd.DataFrame:
    '''Creates new characteristics based on the minimum values ​​of each characteristic

    Args:        
    data(pd.DataFrame) = aggregation data
    feature_for_aggregation(List[str]) = features to be aggregated
    '''
    d = create_empty_data(data)
    for feature in feature_for_aggregation:
        d = d.reindex(columns = d.columns.tolist() + [feature])
        group = data.groupby(['SK_ID_CURR'])[feature].min()
        for idx in group.index:
            d.loc[idx, feature] = group.loc[idx]
            
    return d.rename(columns=lambda x: x + '_MIN')

def aggregate_mean_value(data: pd.DataFrame, feature_for_aggregation: List[str]) -> pd.DataFrame:
    '''Creates new characteristics based on the mean values ​​of each characteristic

    Args:        
    data(pd.DataFrame) = aggregation data
    feature_for_aggregation(List[str]) = features to be aggregated
    '''
    d = create_empty_data(data)
    for feature in feature_for_aggregation:
        d = d.reindex(columns = d.columns.tolist() + [feature])
        group = data.groupby(['SK_ID_CURR'])[feature].mean()
        for idx in group.index:
            d.loc[idx, feature] = group.loc[idx]
            
    return d.rename(columns=lambda x: x + '_MEAN')
    