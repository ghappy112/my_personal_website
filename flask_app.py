from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <style>
                .button {
                    background-color: Transparent;
                    /*background-repeat: no-repeat;*/
                    border-color: white;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                }
                form {
                    display: inline-block; //Or display: inline;
                }
            </style>
            <body style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Junior Data Scientist</h1>
                <form method="get" action="/about">
                    <button type="submit" class="button">About</button>
                </form>
                <form method="get" action="/coding_languages">
                    <button type="submit" class="button">Coding Languages</button>
                </form>
                <form method="get" action="/projects">
                    <button type="submit" class="button">Personal Coding Projects</button>
                </form>
                <form method="get" action="/contact">
                    <button type="submit" class="button">Contact</button>
                </form>
                <br>
                <h1 style="color:white; b">Welcome to my personal website!</h1>
            </body>
        </html>
    '''

@app.route('/about')
def about():
    return '''
        <html>
            <style>
            .button {
              background-color: Transparent;
              /*background-repeat: no-repeat;*/
              border-color: white;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
            }
            form {
                display: inline-block; //Or display: inline;
            }
            </style>
            <body style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Junior Data Scientist</h1>
                <form method="get" action="/coding_languages">
                    <button type="submit" class="button">Coding Languages</button>
                </form>
                <form method="get" action="/projects">
                    <button type="submit" class="button">Personal Coding Projects</button>
                </form>
                <form method="get" action="/contact">
                    <button type="submit" class="button">Contact</button>
                </form>
                <p style="color:white;">Hi! My name is Greg Happ!</p>
                <p style="color:white;">I was born in Chicago, IL, and raised in Lake Geneva, WI. I currently work remotely in Lake Geneva, but will eventually be moving to Milwaukee, WI, to work in person.</p>
                <p style="color:white;">I have passions for both coding and data science.</p>
                <p style="color:white;">From January to March 2021, I attended the <a href="https://www.credly.com/badges/5913ad7b-74b1-4bfb-be65-ffaf10e8d610?source=linked_in_profile/">Data Incubator Fellowship</a>, a prestigous data science bootcamp. It has a 2 percent acceptance rate. It usually only accepts STEM Master's and STEM PHD's, but I still got accepted despite only having a bachelor's degree. The interview process included an intensive coding challenge. We studied applied data science, machine learning, Python, SQL, and other in demand tools and technologies, and built a series of rigorous, business-focused projects using real-world, public data sets, and concentrated computer programming modules.</p>
                <p style="color:white;">I found my passion for data science as an economic research analyst with the <a href="https://uww.edu/ferc">Fiscal and Economic Research Center</a> of <a href="https://uww.edu/">University of Wisconsin-Whitewater</a>. As an economic research analyst, I used Stata and R to conduct regression analysis. While attending Whitewater, I earned my Bachelor's of Science in Economics with a minor in Mathematics.</p>
                <p style="color:white;">I recently joined Fidelity National Information Services (FIS)'s Global AI - Machine Learning and Data Science (AI/ML) Team as a Quantitative Analyst in a Junior Data Scientist role. I'm very excited to start, and can't wait to learn more about AI's role in the FinTech Industry!</p>
                <br>
                <p style="color:white;">I hope you enjoy my website!</p>
            </body>
        </html>
    '''

@app.route('/coding_languages')
def coding_languages():
    return '''
        <html>
            <style>
            .button {
              background-color: Transparent;
              /*background-repeat: no-repeat;*/
              border-color: white;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
            }
            form {
                display: inline-block; //Or display: inline;
            }
            </style>
            <body style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Junior Data Scientist</h1>
                <form method="get" action="/about">
                    <button type="submit" class="button">About</button>
                </form>
                <form method="get" action="/projects">
                    <button type="submit" class="button">Personal Coding Projects</button>
                </form>
                <form method="get" action="/contact">
                    <button type="submit" class="button">Contact</button>
                </form>
                <br>
                <h1 style="color:#0062FF; b">Python</h1>
                <h1 style="color:#099FFF; b">R</h1>
                <h1 style="color:#0033FF; b">Stata</h1>
                <h1 style="color:#FFFF00; b">SQL</h1>
                <h1 style="color:#ff5349; b">Spark</h1>
                <h1 style="color:#ffa343; b">Java</h1>
                <h1 style="color:#FF6600; b">HTML</h1>
                <h1 style="color:#9D00FF; b">CSS</h1>
                <h1 style="color:#099FFF; b">VBA</h1>
            </body>
        </html>
    '''

@app.route('/projects')
def projects():
    return '''
        <html>
            <style>
            .button {
              background-color: Transparent;
              /*background-repeat: no-repeat;*/
              border-color: white;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
            }
            form {
                display: inline-block; //Or display: inline;
            }
            </style>
            <body style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Junior Data Scientist</h1>
                <form method="get" action="/about">
                    <button type="submit" class="button">About</button>
                </form>
                <form method="get" action="/coding_languages">
                    <button type="submit" class="button">Coding Languages</button>
                </form>
                <form method="get" action="/contact">
                    <button type="submit" class="button">Contact</button>
                </form>
                <br>
                <h1 style="color:white; b">Check out my Github for my personal coding projects:</h1>
                <h1><a href="https://github.com/ghappy112/">ghappy112</a></h1>
            </body>
        </html>
    '''

@app.route('/contact')
def contact():
    return '''
        <html>
            <style>
            .button {
              background-color: Transparent;
              /*background-repeat: no-repeat;*/
              border-color: white;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
            }
            form {
                display: inline-block; //Or display: inline;
            }
            </style>
            <body style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Junior Data Scientist</h1>
                <form method="get" action="/about">
                    <button type="submit" class="button">About</button>
                </form>
                <form method="get" action="/coding_languages">
                    <button type="submit" class="button">Coding Languages</button>
                </form>
                <form method="get" action="/projects">
                    <button type="submit" class="button">Personal Coding Projects</button>
                </form>
                <br>
                <h1 style="color:white; b">Connect with me on LinkedIn:</h1>
                <h1><a href="https://www.linkedin.com/in/gregory-happ-7bb578138/">Greg Happ's LinkedIn Profile</a></h1>
                <br>
                <h1 style="color:white; b">Email me:</h1>
                <h1 style="color:white; b">greghapp700@gmail.com</h1>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
