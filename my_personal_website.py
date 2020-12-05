from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome_template.html')
    
@app.route('/about')
def about():
    return render_template('about_template.html')

@app.route('/coding_languages')
def coding_languages():
    return render_template('CL_template.html')

@app.route('/projects')
def projects():
    return render_template('projects_template.html')

@app.route('/contact')
def contact():
    return render_template('contact_template.html')

if "__name__" == "__main__":
    app.run(debug=True)