from flask import Flask, request, render_template, redirect, url_for, session, flash
from datetime import datetime
from pytz import timezone
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def index():
    eastern = timezone('US/Eastern')
    now = datetime.now(eastern)
    if (int(now.strftime("%H")) == 12):
        current_time = now.strftime("%H:") + str(int(now.strftime("%M"))-2) + " PM"
    elif (int(now.strftime("%H")) > 12):
        current_time = str(int(now.strftime("%H"))%12) +  str(int(now.strftime("%M"))-2) + " PM"
    else:
        current_time = now.strftime("%H:") + str(int(now.strftime("%M"))-2) + " AM"
    return render_template('index.html',current_time = current_time)

if __name__ == "__main__":
    app.debug = True
    app.run()
