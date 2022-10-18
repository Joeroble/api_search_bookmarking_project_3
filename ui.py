
'''
User Interface will accept an input from the user, verify that it is a date
Using that input call the CalanderDate.py to create a userCalanderDate object

UI passes the calander object to the API Manager and the API Manager will make calls
to the three APIs using that date. 
'''
from flask import Flask, render_template, request
from API_Movie_Call import movie_call

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/get_date')
def get_date_info():
    print('form date is: ', request.args)
    date_to_search = request.args.get('search_date')
    movie_info = movie_call(date_to_search)
    return render_template('api_results.html', movie_info=movie_info.data)


if __name__ == '__main__':
    app.run()
## TODO Watch videos on Flask, set up a basic input. 