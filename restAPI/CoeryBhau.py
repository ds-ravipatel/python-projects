from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/func1')
@app.route('/func1otherlink') #both links will point to same function
def func1():
    return "Hello world"


posts = [
    {
        'author': 'Ravi Patel',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted':'Mar 26, 2020'
    },
    {
        'author': 'Manoj Bangad',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted':'Feb 26, 2020'
    }
]


@app.route('/home')
@app.route('/')
def home():
    #return '<h> Home Page </h>'
    # posts details are passed to page as a parameter
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')
    #return '<h> About Page </h>' #directly return

app.run(debug=True, port=5000)