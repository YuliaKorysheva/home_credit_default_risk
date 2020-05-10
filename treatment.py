import pandas as pd
from typing import Optional, List

class ProcessingOmissions():
    '''The class contains tools for handling omissions

    '''
    def fill_gaps(data: pd.DataFrame, features: List[str], value: any):
        '''Fill the gaps 

        Args:
        data(pd.DataFrame) = data for processing
        features(List[str]) = features to be filled
        value(any) = value to be filled
        '''
        for feature in features:
            data[feature].fillna(value, inplace=True)

    def get_obj_to_drop(data: pd.DataFrame, number_of_missing_values: int, axis_check: int) -> List[any]:
        '''Returns the objects with the most omissions

        Args:
        data(pd.DataFrame) = data for checking
        number_of_missing_values(int) = maximum permissible omissions value
        axis_check(int) = analyze rows(1) or columns(0)
        '''
        omissions = data.isnull().sum(axis=axis_check).sort_values(ascending=False)
        return [idx for idx in omissions.index if (omissions[idx] >= number_of_missing_values) and (omissions[idx] != 0)]
