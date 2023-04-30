from flask import Flask, render_template, request, redirect, url_for
from forms import Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'moot' # csrf, cross site request foregery


@app.route('/', methods=['GET', 'POST']) # any method can be added to list, only of which can be used
def index():
    request_method = request.method
    if request_method == 'POST': 
        print('--------------') 
        print(request.form) # this request.form is what prints the response dict
        print('--------------')

        first_name = request.form['first_name']
        last_name = request.form['last_name']

        return redirect(url_for('name', first_name=first_name, last_name=last_name)) # to redirect to another page when the from is submitted, also have to pass the variables
    return render_template('index.html', request_method = request_method) # see the index.html


@app.route('/name/<string:first_name> <string:last_name>') # fetch the variables and print em
def name(first_name, last_name):
    return f'hello, {first_name} {last_name}' # when the post method in the above case worked fine this function was used as a place holder to redirect the response to
    # just added a space for h xD

# using Flask-WTF forms thingy a form can be created which cannot be csrf ed, GET to yk and POST to send the entered data to backend
@app.route('/todo', methods=['GET','POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit(): # this is basically used to validate or check if any data was entered and recieved
        print(todo_form.content.data) # prints content of the data
        return redirect('/success') # can be a successful page etc
    return render_template('todo.html', form= todo_form) # here form was used ???
 

@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ ==  '__main__':
    app.run(debug=True)