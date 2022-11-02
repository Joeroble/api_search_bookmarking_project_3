This application utiziles flask, a database, and APIs.  You select a date on the main page, and click search, this will then search the NASA APOD, Movie Database, and Wikipedia.  It will then return a movie, and APOD from that date in time.  Plus the wiki article covering events that happened on that day in history.  The user will then have the option to save this data, and can retrieve it later on another page to go back to the information from that day saved.

The program is broken up into 8 parts, and tests - the API_Database, API_Manager, API calls (Movie, Nasa, Wiki), CalendarDate, API_Response, UI, and unittests.

The API manager handles all of the calls - for example the UI calls upon it to get the data from the APIs in order to display it to the user.  It also handles database creation, saving and retrieving.

The API calls have error handling in case of a bad connection, or user error, and their main focus is to retrieve the data, format/process it, save it into a api_response, and send it back out.

API_Database saves the movie url, the movie poster image url, the nasa image url, and the wiki article url.

API_Response is what the API's returned data is stored in, it has 3 fields - Data (proper data returned from the api that has, ideally, been formatted), 
user_error (holds errors due to the user such as wrong dates, formatting of dates), and connection_error(stores exceptions, and errors in connecting with the API).

CalendarDate has a variety of functions that ensure the date is valid, and has functions for formatting the date i.e. 2022-11-02 is turned into November 2, or November 2 2022.

UI handles flask, displaying the information to the user, and calling on api manager/calendardate to get the calls, and proper date formats.

The unittest tests test API_Manager, API_Respoonse, CalendarDate, API_Movie_Call, API_Nasa_Call, API_Wiki_Call currently.

API keys - 

Movie Database - Go to https://www.themoviedb.org/signup to sign up for a new account

From there you can go into the account settings to get the API key, or click the link provided on this page - https://developers.themoviedb.org/3/getting-started/introduction

NASA - Go to https://api.nasa.gov/ 
You will then supply your email, and what you are using it for (optional).  They will email you the key, and the key itself will populate on the screen.

Wiki - Does not require an API key

Parts of the code have been modified or converted from class examples, and homework.




Photo by <a href="https://unsplash.com/@michalmatlon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Michal Matlon</a> on <a href="https://unsplash.com/s/photos/something-went-wrong?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  