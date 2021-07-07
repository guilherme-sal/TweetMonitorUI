import requests

### Endpoints ###
APIURL = 'http://50.116.36.123:5000'

LOG_ENDPOINT = APIURL + '/log'

COLLECTNOW = APIURL + '/collectnow'

ALLTWEETS_ENDPOINT = APIURL + '/tweets'
AGGREGATEDDB_ENDPOINT = APIURL + '/tweets/aggregate/all'

TARGETS = APIURL + '/targets'
TARGET_ENDPOINT = APIURL + '/target'


def request_collect_now():
    r = requests.get(COLLECTNOW).json()
    code = r['Code']
    return code


def request_alltweets_as_json():
    r = requests.get(ALLTWEETS_ENDPOINT).json()
    json = r['Dataframe']
    return json


def request_targets_list():
    r = requests.get(TARGETS).json()
    targets_list = r['Targets']
    return targets_list


def request_target_info(target):
    r = requests.get(f'{TARGET_ENDPOINT}/{target}').json()
    json = r[f'{target}']
    return json


def request_post_new_target(target):
    r = requests.post(f'{TARGET_ENDPOINT}/{target}').json()
    code = r['Code']
    return code


def request_tweets_from_target(target):
    r = requests.get(f'{ALLTWEETS_ENDPOINT}/{target}').json()
    json = r['Dataframe']
    return json


def request_delete_target(target):
    r = requests.delete(f'{TARGET_ENDPOINT}/{target}').json()
    code = r['Code']
    return code


def request_log():
    r = requests.get(f'{LOG_ENDPOINT}').json()
    log = r['Log']
    return log


def request_aggregated_db():
    r = requests.get(AGGREGATEDDB_ENDPOINT).json()
    json = r['Dataframe']
    return json

