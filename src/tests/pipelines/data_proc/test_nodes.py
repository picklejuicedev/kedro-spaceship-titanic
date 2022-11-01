
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from  spaceship_titanic.pipelines.data_proc.nodes \
    import create_alone_col, split_cabin, remove_Nan_values, split_name



def test_proc_PassengerId():
    data = {'PassengerId': ['0001_01', '0002_01', '0002_02', '0003_01'],
        'Age': [20, 21, 19, 18]}
    df = pd.DataFrame(data)

    data_result = {'PassengerId': ['0001_01', '0002_01', '0002_02', '0003_01'],
        'Age': [20, 21, 19, 18],
        'Alone': [True, False, False, True]}

    df_result = pd.DataFrame(data_result)

    df_proc = create_alone_col(df)

    assert_frame_equal(df_proc, df_result)


def test_proc_split_cabin():
    data = {'Cabin': ['B/1/P', 'F/2/S', 'A/3/S', pd.NA]}
    df = pd.DataFrame(data)

    data_result = {'Deck': ['B', 'F', 'A', pd.NA],
                    'Room': [1, 2, 3, 0],
                    'Side': ["P","S","S", pd.NA]}
    df_result = pd.DataFrame(data_result)

    df_proc = split_cabin(df)

    assert_frame_equal(df_proc, df_result)


def test_remove_Nan():
    data = {
        'RoomService': [12.3, 21.3, 11.30, pd.NA],
        'FoodCourt': [12.3, 21.3, 11.30, pd.NA],
        'ShoppingMall': [12.3, 21.3, 11.30, pd.NA],
        'Spa': [12.3, 21.3, 11.30, pd.NA],
        'VRDeck': [12.3, 21.3, 11.30, pd.NA],
        'Age': [21,34,56, pd.NA],
        'Name': ["A A", "b b","C C", pd.NA],
        'Room': [1, 2, 3, pd.NA]}
    df = pd.DataFrame(data)

    data_result = {
        'RoomService': [12.3, 21.3, 11.30, 0.0],
        'FoodCourt': [12.3, 21.3, 11.30, 0.0],
        'ShoppingMall': [12.3, 21.3, 11.30, 0.0],
        'Spa': [12.3, 21.3, 11.30, 0.0],
        'VRDeck': [12.3, 21.3, 11.30,0.0],
        'Age': [21,34,56, 27],
        'Name': ["A A", "b b","C C", "No Name"],
        'Room': [1, 2, 3, 0]}
    df_result = pd.DataFrame(data_result)

    df_proc = remove_Nan_values(df)

    assert_frame_equal(df_proc, df_result)
    

def test_split_name():
    data = {'Name': ["A A", "b b","C C", "No Name"]}
    df = pd.DataFrame(data)

    data_result = {
        'Firstname': ["A", "b","C", "No"],
        'Lastname': ["A", "b","C", "Name"]}
    df_result = pd.DataFrame(data_result)

    df_proc = split_name(df)

    assert_frame_equal(df_proc, df_result)