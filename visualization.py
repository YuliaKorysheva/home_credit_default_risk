import pandas as pd
from typing import Optional, List
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def get_stat_category_features(data: pd.DataFrame, feature: str, colour: sns.palettes._ColorPalette, horizontal_located: bool):
    '''Returns three histograms for one categorical attribute
    Illustrates statistics on the number of observations for each category, in what percentage the data is shared with customers who did not repay the loan (by category), 
    how many people did not repay the loan in each category

    Args:
    data(pd.DataFrame) =  data for checking
    features(List[str]) = feature for visualization
    colour(sns.palettes._ColorPalette) = colour for graphs
    horizontal_located(bool) = should the graphs be horizontal
    '''
    if horizontal_located:
        fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(16, 6))
        plt.subplots_adjust(wspace=0.5)
    else:
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(10, 16))
        plt.subplots_adjust(hspace=0.9)
    
    
    s1 = sns.countplot(ax=ax1, x=feature, data=data, palette=colour)
    s1.set(xlabel='Значения категориального признака', ylabel='Количество объектов в категории')
    s1.set_xticklabels(s1.get_xticklabels(),rotation=90)
    
    group = data.groupby(['TARGET', feature], as_index=False).count()
    group = group[group.TARGET == 1]
    non_returnees = group.sum().SK_ID_CURR 
    group['persent_non_returnees'] = group.SK_ID_CURR / (non_returnees / 100)

    s2 = sns.barplot(ax=ax2, x=feature, y='persent_non_returnees', data=group, palette=colour)
    s2.set(xlabel='Значения категориального признака', 
           ylabel='Разбиение на категории из тех, кто не вернул кредит (%)')
    s2.set_xticklabels(s2.get_xticklabels(),rotation=90)
    
    group = data.groupby([feature], as_index=False).count()
    group_target = data.groupby(['TARGET',feature], as_index=False).count()
    group_target = group_target[group_target.TARGET == 1]
    group = group.loc[group[feature].isin(list(group_target[feature].unique()))]
    group_target.index = np.arange(len(group_target))
    group.index = np.arange(len(group))
    group_target['persent'] = (group_target.SK_ID_CURR / (group.SK_ID_CURR / 100))
    
    s3 = sns.barplot(ax=ax3, x=feature, y='persent', data=group_target, palette=colour)
    s3.set(xlabel='Значения категориального признака', 
           ylabel='Процент тех, кто не вернул кредит в отдельной категории')
    s3.set_xticklabels(s3.get_xticklabels(),rotation=90)
        
    plt.show()

def compare_numerical_and_categorical_features(data: pd.DataFrame, str_feature: str, int_feature: str, colour: sns.palettes._ColorPalette, separation_by_target: bool):
    '''Illustrates the bond between numerical and categorical

    Args:
    data(pd.DataFrame) =  data for checking
    str_features(str) = categorical features for visualization
    int_features(int) = numerical features for visualization
    colour(sns.palettes._ColorPalette) = colour for graphs
    separation_by_target(bool) = whether to show the target value separately
    '''
    fig, ax1 = plt.subplots(ncols=1, figsize=(16, 6))
    s = sns.stripplot(ax=ax1, x=str_feature, y=int_feature, data=data,
                      hue='TARGET', palette=colour, dodge=separation_by_target)
    
    plt.show()

def compare_numerical_features(data: pd.DataFrame, features: List[str], colour: sns.palettes._ColorPalette):
    '''Returns feature distributions and their dependency

    Args:
    data(pd.DataFrame) = data for checking
    features(List[str]) = featurws for comparison
    colour(sns.palettes._ColorPalette) = colour for graphs
    '''
    sns.pairplot(data[features], hue='TARGET', palette=colour)

def get_heatmap(data: pd.DataFrame, features: List[str], colour: sns.palettes._ColorPalette):
    '''Returns a correlation map

    Args:
    data(pd.DataFrame) = data for checking
    features(Lisr[str]) = features for counting correlation
    '''
    f, ax = plt.subplots(ncols=1, figsize=(11,9))
    sns.heatmap(data[features].corr(), cmap=colour, annot=True)