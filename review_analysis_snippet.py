from flask import Flask,render_template,request
import pandas as pd

import csv,datetime
app=Flask(__name__)

from textblob import TextBlob as tb


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/tables', methods=['POST','GET'])
def table():
    df2 = pd.read_csv("link/Dataset2.csv")
    df2 = df2.dropna()
    list_apps = sorted(set(df2["App"]))
    if request.method == "POST":
        app_name = request.form['app_name']
        dictionary = {
            "postitive" : [],
            "negative" : [],
            "neutral" : []
        }
        df = df2.loc[df2["App"]== app_name]

        df_pos = df[df["Sentiment"] == "Positive"]
        df_neg = df[df["Sentiment"] == "Negative"]
        df_neu = df[df["Sentiment"] == "Neutral"]

        dictionary['positive'] = list(df_pos["Translated_Review"])
        dictionary['negative'] = list(df_neg["Translated_Review"])
        dictionary['neutral'] = list(df_neu["Translated_Review"])

        total = len(df)
        per_pos = len(dictionary['positive'])/total * 100
        per_neg = len(dictionary['negative'])/total * 100
        per_neut = len(dictionary['neutral'])/total * 100
        
        return render_template('tables.html',ppos=per_pos,pneg=per_neg,pneu=per_neut,app_name=app_name,list_apps=list_apps,
                           pos=dictionary['positive'],neg=dictionary['negative'],neu=dictionary['neutral'])
    
    return render_template('tables.html',list_apps=list_apps)


@app.route('/add_data',methods=['GET','POST'])
def data_1():
    money=0
    message='Data Added'
    df=pd.read_csv('updated_proj_new.csv')
    app = request.form['App_name']
    cat = request.form['Category']
    rating = request.form['Rating']
    review = request.form['Review']
    size = request.form['Size']
    Installs = request.form.get('Installs')
    Type = request.form.get('Type')
    if Type == 'Paid':
        money= '$'+str(request.form['price'])
    content = request.form.get('content_rating')
    Genre = request.form.get('Genre')
    Last = datetime.datetime.strptime(request.form['Last'], '%Y-%m-%d')
    Last=Last.strftime('%d-%b-%Y')
    Current = request.form.get('Current')
    Android = request.form.get('Android')

    
    fields=[len(df)-1,app,cat,rating,review,size,Installs,Type,money,content,Genre,Last,Current,Android]
    with open(r'updated_proj_new.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    
    
    return render_template('user.html',message = message)

@app.route('/add_data_1',methods=['GET','POST'])
def data_2():
    message='Data Added'
    app = request.form['app-name']
    rev= request.form['enter-review']

    sentiment=tb(rev)
    sent='Neutral'
    pol_val = sentiment.polarity

    if pol_val > 0.0:
        sent = 'Positive'
    elif pol_val<0.0:
        sent='Negative'
    

    sent_sub = sentiment.subjectivity

    fields=[app,rev,sent,pol_val,sent_sub]

    with open(r'updated_project_d2.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

    


    return render_template('user.html',message=message)


if __name__ == '__main__':
    app.run(debug=True)
