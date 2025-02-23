from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        name = "Python"
        example_list = ["2.5", "2.6", "2.7", "3.1", "3.2", "3.3", "3.4"]
        return render_template('index.html', name = name, example_list = example_list)
    except Exception as e:
        return(str(e))

@app.route("/page-one/")
def pageone():
    try:
        name = "Page One"
        return render_template('page-one.html', name = name)
    except Exception as e:
        return(str(e))
    
@app.route("/about/")
def aboutepage():
    try:
        name = "About"
        return render_template('index.html', name = name)
    except Exception as e:
        return(str(e))
        
@app.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html')
        
if __name__ == "__main__":
    app.run()

