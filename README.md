# 'BookEdx'  (in progress)
#  App deployed: https://bookedx.herokuapp.com/ 


Project based on the CS50's Web Programming the project 1 of course on Edx Website. Using python, Flask and PostgreSQL. I've used SQlalchemy ORM for this project. 

### Models
Declare the tables in SQLPostgres. 

I use 3 tables: 
| books        | Data Type           |
| ------------- |:-------------:| 
| title         | character varying(30) | 
| author        | character varying(30)	   |  
| book_id       | integer Incremento automático      |   
| ISBN          | character(10)      |   
| year          | integer      |   

 
| users        | Data Type     |
| -------------|:-------------:| 
| id_user      | integer Incremento automático  | 
| email        | character varying(100)  | 
| username     | character varying(100)  | 
| password     | character varying	   |



| reviews      | Data Type           |
| -------------|:-------------:| 
| review_id      | integer NULL	  Primary key |	
| score        | integer  | 
| review_text     | character varying(500)	   |	
| user_id      | integer NULL	Foreign  Key   |	
| book_id      | integer NULL	Foreign Key   |	
| timestamp      | DataTime   |	

 Create a import.py program to import books (books.csv file) into my database.

### Set a virtual environment
I decided to use pipenv to make easier the deployment.

### Dependencies 
* flask_login to store the active user in the session and  let them log in  and out. 
* Blueprints:  to organize the app with components. 
* python-dotenv =  manage the .env files 
* flask-sqlalchemy = Connection with Database set in PostgreSql
* flask-login = handle users login and sessions
* psycopg2 = Adapts my database to Python language
* gunicorn = as a web server gategay Interface
* requests =  to make http request to GoodReads Api

### FrontEnd
Bootstrap as a Css Framework. Templates rendered by render_templates from flask. 

### Files 
###### __init__.py 
Set the configuration for the Database and Create flask app. Also declare the Blueprint 
###### auth.py
Define the routes for the login and authentication of the users. Also set hash the passwords. 
###### main.py 
 Routes for the profile where the user can search the books. Do the queries to check if the value in the search bar matches with the information. When user types ISBN number of a book, the title of a book, or an author of the book, the site displays the matching records and a Notfound message if there arent not matches.
###### books.py
Renders the template when of the book from the results of the search page. Provides the details about the book: its title, author, publication year, ISBN number, and the  reviews that users  left for the book on my website.
###### api.py
Set route "/api/<isbn>" so users can access to information about that book, review score and average hosted in my Databaase. It returns a JSON response. If it's not in the database it returns 404 error.
##### static files
Images for the app and the  css styles
