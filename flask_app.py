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
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <p style="color:white;">I was born in Chicago, IL, and raised in Lake Geneva, WI.</p>
                <p style="color:white;">I love the outdoors and enjoy outdoor activities such as hiking, swimming, kayaking, paddleboarding, and recently even camping! I also like to play guitar.</p>
                <p style="color:white;">I have passions for coding, economics, data science, artificial intelligence, and machine learning.</p>
                <p style="color:white;">From January to March 2021, I attended the <a href="https://www.credly.com/badges/5913ad7b-74b1-4bfb-be65-ffaf10e8d610?source=linked_in_profile/">Data Incubator Fellowship</a>, a prestigous data science bootcamp. It has less than a 2 percent acceptance rate. It usually only accepts STEM Master's and STEM PhD's. The interview process included an intensive coding challenge. We studied applied data science, machine learning, Python, SQL, and other in demand tools and technologies, and built a series of rigorous, business-focused projects using real-world, public data sets, and concentrated computer programming modules.</p>
                <p style="color:white;">I found my passion for data science as an economic research analyst with the <a href="https://uww.edu/ferc">Fiscal and Economic Research Center</a> of <a href="https://uww.edu/">University of Wisconsin-Whitewater</a>. As an economic research analyst, I used Stata and R to conduct regression analysis. While attending Whitewater, I earned my B.S. in Economics with a minor in Mathematics.</p>
                <p style="color:white;">Then, for about 2 years and a half, I worked at Fidelity National Information Services (FIS)'s Global on the Artificial Intelligence (AI) - Machine Learning (ML) and Data Science Team as an AI/ML Quantitative Analyst in a Data Scientist role. As a Data Scientist, I used ML to develop AI integrated products and obtain data driven insights for FinTech solutions. I've worked on a variety of data science projects and solved them by utilizing a combination of my data science knowledge and by leveraging the AWS Data Science Stack, including SageMaker, Cloud9, CodeCommit, Lambda, EC2, S3, Glue, and Athena.</p>
                <br>
                <p style="color:white;">I hope you enjoy my website!</p>
            </body>
        </html>
    '''

@app.route('/coding_languages')
def coding_languages():
    return '''
        <html>
            <script>
                function mainJSFunction() {
                    // Get the screen width and height
                    const screenWidth = window.innerWidth;
                    const screenHeight = window.innerHeight;

                    // Get iframe ID
                    var iframe = document.getElementById('iframeID')

                    // Set width and height
                    var width = screenWidth;
                    var height = (373.5/600) * screenWidth;

                    // Reset width and height if needed
                    if (height > screenHeight) {
                        var height = screenHeight
                        var width = (600/373.5) * height
                    } else if (height < 373.5) {
                        var height = 373.5
                        var width = 600
                    }

                    // Set iframe width and height
                    iframe.width = width;
                    iframe.height = height;
                }
            </script>
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
            <body onload="mainJSFunction()" style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <div style="text-align: center;">
                    <iframe id="iframeID" frameborder="0" src="https://ghappy112.shinyapps.io/coding_skills/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle on Bottom Left of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/coding_skills">GitHub for this Shiny Dashboard</a></h1>
                </div>
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
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <h1><a href="https://ghappy112.pythonanywhere.com/reddit_political_sentiment_analysis">Reddit Political Sentiment Analysis Dashboard</a></h1>
                <br>
                <h1><a href="https://github.com/ghappy112/">GitHub</a></h1>
                <br>
                <h1><a href="https://public.tableau.com/app/profile/greg1281/vizzes">Tableau Dashboards</a></h1>
                <br>
                <h1><a href="https://ghappy112.pythonanywhere.com/shiny_dashboards">Shiny Dashboards</a></h1>
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
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <h1><a href="https://www.linkedin.com/in/gregory-happ-7bb578138/">Connect with me on LinkedIn!</a></h1>
                <br>
                <h1><a href="mailto: [greghapp700@gmail.com]?subject= &body=">Email Me!</a></h1>
            </body>
        </html>
    '''

@app.route("/reddit_political_sentiment_analysis")
def reddit_political_sentiment():
    html = '''
        <script>
            function mainJSFunction() {
                // Get the screen width and height
                const screenWidth = window.innerWidth;
                const screenHeight = window.innerHeight;

                // Get iframe ID
                var iframe = document.getElementById('powerBIiframeID')

                // Set width and height
                var width = screenWidth;
                var height = (373.5/600) * screenWidth;

                // Reset width and height if needed
                if (height > screenHeight) {
                    var height = screenHeight
                    var width = (600/373.5) * height
                } else if (height < 373.5) {
                    var height = 373.5
                    var width = 600
                }

                // Set iframe width and height
                iframe.width = width;
                iframe.height = height;
            }
        </script>
        <body onload="mainJSFunction()">
            <div style="text-align:center;">
                <h1>Political Candidates' Reddit Sentiment Dashboard</h1>
                <p>Dashboard updates every 3 hours with the latest Reddit data</p>
                <br>
                <iframe title="candidate_reddit_political_sentiment_dashboard" id="powerBIiframeID" src="https://app.powerbi.com/view?r=eyJrIjoiOWI0MjY4Y2UtYTgzNi00MmMxLTlmNWUtY2U3NWNlY2FlYmI0IiwidCI6IjlhM2MyZTdmLWMyYTgtNDgyYy1hYjE0LWY5MzY1N2I3MWRjNCIsImMiOjF9" frameborder="0" allowFullScreen="true"></iframe>
                <br>
                <h1><a href="https://github.com/ghappy112/reddit_political_sentiment">GitHub</a></h1>
            </div>
        </body>
        '''
    return html

@app.route('/shiny_dashboards')
def shiny_dashboards():
    return '''
        <html>
            <script>
                function mainJSFunction() {
                    // Get the screen width and height
                    const screenWidth = window.innerWidth;
                    const screenHeight = window.innerHeight;

                    // Get iframe ID
                    var iframe = document.getElementById('iframeID')

                    // Set width and height
                    var width = screenWidth;
                    var height = (373.5/600) * screenWidth;

                    // Reset width and height if needed
                    if (height > screenHeight) {
                        var height = screenHeight
                        var width = (600/373.5) * height
                    } else if (height < 373.5) {
                        var height = 373.5
                        var width = 600
                    }

                    // Set iframe width and height
                    iframe.width = width;
                    iframe.height = height;
                }
            </script>
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
            <body onload="mainJSFunction()" style="background-color:black;">
                <h1 style="color:white;">Greg Happ</h1>
                <h1 style="color:white; b">Data Science & Data Analytics</h1>
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
                <div style="text-align: center;">
                    <h1 style="color:white;">Shiny Dashboards</h1>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112">GitHub</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID" frameborder="0" src="https://ghappy112.shinyapps.io/coding_skills/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle on Bottom Left of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/coding_skills">GitHub for this Dashboard</a></h1>
                </div>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
