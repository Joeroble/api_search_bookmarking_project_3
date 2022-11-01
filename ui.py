
'''
User Interface will accept an input from the user, verify that it is a date
Using that input call the CalanderDate.py to create a userCalanderDate object

UI passes the calander object to the API Manager and the API Manager will make calls
to the three APIs using that date. 
'''
from flask import Flask, render_template, request, redirect
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
    display_date = CalendarDate.get_date_for_display(date_returned)
    date_for_movie = CalendarDate.get_date_parts(date_returned)
    date_for_wiki = CalendarDate.get_date_month_day_str(date_returned)
    date_for_nasa = CalendarDate.check_date_limits(date_returned)

    movie_info = API_Manager.api_movie_call_response(date_for_movie)
    wiki_info = API_Manager.api_wiki_call_response(date_for_wiki)
    nasa_info = API_Manager.api_nasa_call_response(date_for_nasa)

    return render_template(
        'api_results.html', 
        movie_info=movie_info.data,
        wiki_link=wiki_info.data[0],
        nasa_info=nasa_info.data,
        date_info={'display':display_date,'hidden':date_returned})

@app.route('/save')
def save_the_day():
    
    value_question_mark = request.args.get('save_the_day')
    if value_question_mark:
        saved_date = request.args.get('search_day')
        movie_title = request.args.get('movie_title')
        movie_img = request.args.get('movie_img')
        nasa_title = request.args.get('nasa_title')
        nasa_image = request.args.get('nasa_img')
        wiki_link = request.args.get('wiki_url')

        bookmark_data = prep_bookmark_info(
            ['date','movie_title', 'movie_img', 'nasa_title', 'nasa_img', 'wiki_link'],
            [saved_date, movie_title, movie_img, nasa_title, nasa_image, wiki_link])
        API_Manager.save_to_database(bookmark_data)

    return redirect("/")

@app.route('/bookmarks')
def display_bookmarks():
    bookmark_data = API_Manager.get_bookmarks()
    return render_template('bookmarks.html', bookmark_data=bookmark_data)


def prep_bookmark_info(list_of_keys, list_of_values):
    return dict(zip(list_of_keys, list_of_values))

if __name__ == '__main__':
    app.run()
