from flask import Flask, render_template, request
from imschool import *



app = Flask('app')




@app.route('/<count_n>', methods=['GET', 'POST'])
def hello_world(count_n):
    today_date_, lunch_info_, cal_info_  = sc_lunch(int(count_n))

    data = {
      "today_lunch" : today_date_,
      "lunch_food" : lunch_info_,
      "img" : cal_info_
      
    }
  
    return render_template('index.html', data=data, counting = count_n)

app.run(host='0.0.0.0', port=8080, debug=True)