from flask import Flask, render_template, redirect, session, request
import random
import os
import datetime

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index():
    try:
        session['gold_total']==session['gold_total']
    except KeyError:
         session['gold_total']=0
         print 'Starting gold count is 0'
    return render_template('ninja.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print request.form
    now = datetime.datetime.now()
    print 'datetime is ', now
    try:
        session['outcome']==session['outcome']
    except KeyError:
         session['outcome']=[]
         print 'No outcome yet'

    if request.form['building'] == 'farm':
        print 'farm'
        # session['gold_count'] = 20
        farm_gold=random.randint(10,20)
        session['outcome'].insert(0, 'Earned '+ str(farm_gold)+ ' from the farm! '+ str(now))
        session['gold_total']+=farm_gold
        print 'farm gold earned is ', farm_gold

    elif request.form['building'] == 'casino':
        print 'casino'
        casino_gold=random.randint(-50,50)
        if casino_gold >= 0:
            session['outcome'].insert(0, 'Earned '+ str(casino_gold)+ ' from the casino! '+ str(now))
            session['gold_total']+=casino_gold
            print 'Casino gold earned is ', casino_gold
        else:
            session['outcome'].insert(0, 'Lost '+ str(casino_gold)+ ' from the casino...Ouch! '+ str(now))
            session['gold_total']+=casino_gold
            print 'Casino gold lost is ', casino_gold


    for key, value in session.items():
        print key,':',value
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    for key, value in session.items():
        print key,':',value
    return redirect ('/')
app.run(debug=True)
