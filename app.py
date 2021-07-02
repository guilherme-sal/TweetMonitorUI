from flask import Flask, redirect, render_template, request, url_for, flash
from uicore.ui_functions import json_to_df, format_df_dates, format_date
from uicore.ui_requests import request_post_new_target, \
    request_targets_list, request_tweets_from_target, request_collect_now, request_delete_target, request_log, \
    request_aggregated_db

app = Flask(__name__)
app.secret_key = 'FFF3B51'


@app.route('/', methods=['GET'])
def index():

    log = request_log()
    log = log.split(';')[1].split('#')[1]
    log = format_date(log.split('.')[0])

    targets_list = request_targets_list()
    targets_list.sort(key=lambda i: i.lower())

    json = request_aggregated_db()
    df = json_to_df(json)
    df['first_tweet'] = format_df_dates(df['first_tweet'])
    df['last_tweet'] = format_df_dates(df['last_tweet'])
    df_formated = df.sort_values('username', key=lambda col: col.str.lower())

    return render_template('index.html', targets_list=targets_list, df_formated=df_formated, log=log)


@app.route(f'/<target>', methods=['GET', 'POST'])
def target(target):

    targets_list = request_targets_list()

    json = request_tweets_from_target(target)

    if json:
        df = json_to_df(json)
        df = df[['id', 'date', 'tweet', 'nlikes', 'nretweets', 'nreplies', 'hashtags', 'urls', 'photos', 'thumbnail',
                 'language']]
        df['date'] = format_df_dates(df['date'])
        columns = df.columns

        return render_template('target_table.html', targets_list=targets_list, table_columns=columns, df=df,
                               target=target)
    else:
        return(f'Ainda não há tweets para {target}.')


@app.route('/add', methods=['POST'])
def add():
    add_target = request.form['add']
    if (len(add_target) > 16) or (len(add_target) < 1):
        flash('Target name should have 1 to 16 characters.', 'danger')
        return redirect(url_for('index'))
    else:
        add_target = str(add_target)
        targets_list = request_targets_list()
        if add_target not in targets_list:
            success = request_post_new_target(add_target)
            if success:
                flash('Conta adicionada com sucesso.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Conta não pôde ser adicionada.', 'danger')
                return redirect(url_for('index'))
        else:
            flash(f'{add_target} is already on list.', 'danger')
            return redirect(url_for('index'))


@app.route('/update', methods=['GET'])
def update():
    code = request_collect_now()
    if code == 200:
        flash(f'Database updated!', 'success')
        return redirect(url_for('index'))
    else:
        flash(f'Some error occurred during updating collection', 'danger')
        return redirect(url_for('index'))


@app.route(f'/remove/<target>', methods=['GET'])
def remover(target):
    code = request_delete_target(target)
    if code == 200:
        flash('Success - Target removed.', 'success')
        return redirect(url_for('index'))
    else:
        flash('Error - Some error occurred during removal.', 'danger')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
