import pandas as pd
import numpy as np
from typing import Optional, List

class Analysis:
    '''Data analysis tool
    '''

    def check_missing_values(data: pd.DataFrame, number_of_lines: int, axis_check: int) -> pd.DataFrame:
        '''Returns columns with the number of passes (descending)
    
        Args:
        data(pd.DataFrame) = data for checking
        number_of_lines(int) = the number of lines to be printed
        axis_check(int) = analyze rows(1) or columns(0)
        '''
        return data.isnull().sum(axis=axis_check).sort_values(ascending=False)[:number_of_lines]

    def get_unique_value(data: pd.DataFrame, features: Optional[List[str]]=None):
        '''Returns unique features values
    
        Args:
        data(pd.DataFrame) =  data for checking
        features(List[str]) = features that need to be checked for omissions
            Defaul value: None
        '''
        if features is None:
            features = list(data)
        
        for feature in features:
            print(feature, type(data[feature][0]), data[feature].unique())

    def get_features_with_omissions(data: pd.DataFrame) -> List[str]:
        '''Returns a list of features that have omissions
    
        Args:
        data(pd.DataFrame) =  data for checking
        '''
        return [feature for feature in list(data) if data[feature].isnull().any()]

    def get_lists_type_feature(data: pd.DataFrame, features: List[str]) -> [List[str], List[str]]:
        '''Separates features by type
        
        Args:
        data(pd.DataFrame) = data for checking
        features(List[str]) = features that need to be divided into string and numeric
        '''
        features_str = []
        features_int = []
        for feature in features:
            if type(data[feature][0]) == str:
                features_str.append(feature)
            else:
                features_int.append(feature)
        
        return features_str, features_int
            
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
