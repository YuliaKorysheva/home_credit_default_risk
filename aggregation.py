import pandas as pd
from typing import Optional, List

class AggregationData():
    '''Data Aggregation Tools
    '''
    def aggregate_category_entries(data: pd.DataFrame, feature_for_aggregation: List[str]) -> pd.DataFrame:
        '''Aggregates characteristics by counting occurrences of individual categories
        Creates tags for each unique value for all categories. For each client, counts the number of each category.

        Args:
        data(pd.DataFrame) = aggregation data
        feature_for_aggregation(List[str]) = features to be aggregated
        '''
        column_name = 'SK_ID_CURR'
        d = pd.DataFrame({column_name: data[column_name].unique()}).set_index(column_name)
        for feature in feature_for_aggregation:
            d = d.reindex(columns = d.columns.tolist() + list(data[feature].unique()))
            group = data.groupby([column_name, feature]).count()
            for idx, idx_feature in group.index:
                d.loc[idx, idx_feature] = group['SK_ID_BUREAU'].loc[(idx, idx_feature)]

        return d