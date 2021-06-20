import pandas as pd
from datetime import datetime


def format_alltweets_db_as_general_info_df(df):

    df['tweets'] = 1

    last_tweet_list = []
    first_tweet_list = []
    for target in df['username'].unique():
        df_filtered = df.query(f'username == "{target}"')
        last_tweet = df_filtered['date'].max()
        first_tweet = df_filtered['date'].min()
        last_tweet_list.append(last_tweet)
        first_tweet_list.append(first_tweet)

    df_grouped = df.groupby('username').sum('tweets')[['tweets', 'nlikes', 'nreplies', 'nretweets']]
    df_grouped = df_grouped.astype(int)
    df_grouped['first_tweet'] = first_tweet_list
    df_grouped['last_tweet'] = last_tweet_list
    df_grouped = df_grouped.reset_index()
    return df_grouped


def json_to_df(json):
    df = pd.DataFrame.from_dict(json, orient='index')
    return df


def format_date(dt_string):
    format = "%Y-%m-%d %H:%M:%S"
    dt_object = datetime.strptime(dt_string, format)
    date_formated = dt_object.strftime("%m/%d/%Y %H:%M")
    return date_formated


def format_df_dates(df_dates_column):
    date_list_formated = []
    for dt_string in list(df_dates_column):
        date_formated = format_date(dt_string)
        date_list_formated.append(date_formated)
    return date_list_formated


if __name__ == '__main__':
    pass

