import pandas as pd
from datetime import datetime


def json_to_df(json):
    df = pd.DataFrame.from_dict(json, orient='index')
    return df


def format_date(dt_string):
    format = "%Y-%m-%d %H:%M:%S"
    dt_object = datetime.strptime(dt_string, format)
    date_formated = dt_object.strftime("%d/%m/%Y %H:%M")
    return date_formated


def format_df_dates(df_dates_column):
    date_list_formated = []
    for dt_string in list(df_dates_column):
        date_formated = format_date(dt_string)
        date_list_formated.append(date_formated)
    return date_list_formated


if __name__ == '__main__':
    pass

