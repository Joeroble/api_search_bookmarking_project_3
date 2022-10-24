
'''
User Interface will accept an input from the user, verify that it is a date
Using that input call the CalanderDate.py to create a userCalanderDate object

UI passes the calander object to the API Manager and the API Manager will make calls
to the three APIs using that date. 
'''
from datetime import datetime
from flask import Flask, render_template, request
from API_Movie_Call import movie_call
from API_Wiki_Call import API_Wiki_Call

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/get_date')
def get_date_info():
    print('form date is: ', request.args)
    date_to_search = request.args.get('search_date')
    movie_info = movie_call(date_to_search)
    # TODO handle this with a date module?
    year, month, day = date_to_search.split('-')
    wiki_date = datetime(int(year), int(month), int(day))
    wiki_info = API_Wiki_Call(wiki_date.strftime("%B %d"))
    return render_template('api_results.html', movie_info=movie_info.data,wiki_link=wiki_info.data[0])


if __name__ == '__main__':
    app.run()
## TODO Watch videos on Flask, set up a basic input. 