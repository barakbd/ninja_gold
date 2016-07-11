from flask import Flask, render_template, redirect, session, request
import random

app=Flask(__name__)
app.secret_key='ninja_gold'

@app.route('/')
def index():
    try:
        session['gold_count']==session['gold_count']
    except KeyError:
         session['gold_count']=0
         print 'Starting gold count is 0'
    return render_template('ninja.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['farm'] == 'farm':
        print 'hi'
        # session['gold_count'] = 20
        session['farm_gold']=random.randint(10,20)
        session['gold_count']+=session['farm_gold']
    for key, value in session.items():
        print key,':',value
    return redirect('/')

app.run(debug=True)
