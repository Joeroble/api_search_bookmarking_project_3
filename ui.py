
'''
User Interface will accept an input from the user, verify that it is a date
Using that input call the CalanderDate.py to create a userCalanderDate object

UI passes the calander object to the API Manager and the API Manager will make calls
to the three APIs using that date. 
'''
from flask import Flask, render_template, request
import API_Manager
import CalendarDate

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/get_date')
def get_date_info():
    print('form date is: ', request.args)
    date_returned = request.args.get('search_date')

    date_for_movie = CalendarDate.get_date_parts(date_returned)
    date_for_wiki = CalendarDate.get_date_month_day_str(date_returned)
    date_for_nasa = CalendarDate.check_date_limits(date_returned)

    movie_info = API_Manager.api_moive_call_response(date_for_movie)
    wiki_info = API_Manager.api_wiki_call_response(date_for_wiki)
    nasa_info = API_Manager.api_nasa_call_response(date_for_nasa)

    return render_template('api_results.html', movie_info=movie_info.data,wiki_link=wiki_info.data[0],nasa_info=nasa_info.data)


if __name__ == '__main__':
    app.run()
