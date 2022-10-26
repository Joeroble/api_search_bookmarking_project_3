
'''
User Interface will accept an input from the user, verify that it is a date
Using that input call the CalanderDate.py to create a userCalanderDate object

UI passes the calander object to the API Manager and the API Manager will make calls
to the three APIs using that date. 
'''
from flask import Flask, render_template, request
from API_Movie_Call import movie_call # API_Manager
import API_Manager
import API_Database

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/get_date')
def get_date_info():
    print('form date is: ', request.args)
    date_to_search = request.args.get('search_date')  # this function is implemented in calender
    movie_info = movie_call(date_to_search) # date without spliting
    API_manager = API_Manager.api_nasa_call_response(date_to_search)
    nasa_info = API_manager
    API_Database.insert(date_to_search)
    API_Database.Select_All()
    return render_template('api_results.html', movie_info=movie_info.data, nasa_info=nasa_info.data)


if __name__ == '__main__':
    app.run(debug=True, port = 1000)
