from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
            <style>
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                        <br>
                        <h1 style="color:white; b">Welcome to my personal website!</h1>
                    </div>
                </div>
            </body>
        </html>
    '''

@app.route('/about')
def about():
    return '''
        <html>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
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
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body onload="mainJSFunction()" style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                    </div>
                </div>
                <div style="text-align: center;">
                    <h1 style="color:white;">Get to Know Me Network Graph!</h1>
                    <br>
                    <iframe id="iframeID" frameborder="0" src="https://ghappy112.shinyapps.io/about_me_network_graph/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle in Bottom Left Corner of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/about_me">GitHub for this Shiny Dashboard</a></h1>
                </div>
            </body>
        </html>
    '''

@app.route('/coding_languages')
def coding_languages():
    return '''
        <html>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
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
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body onload="mainJSFunction()" style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                    </div>
                </div>
                <div style="text-align: center;">
                    <h1 style="color:white;">Coding Languages</h1>
                    <br>
                    <iframe id="iframeID" frameborder="0" src="https://ghappy112.shinyapps.io/coding_skills/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle in Bottom Left Corner of Dashboard</h2>
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
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
            <style>
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                        <br>
                        <h1>&#128187 <a href="https://github.com/ghappy112/">GitHub</a></h1>
                        <br>
                        <h1>&#128202 <a href="https://ghappy112.pythonanywhere.com/reddit_political_sentiment_analysis">Reddit Political Sentiment Dashboard</a></h1>
                        <br>
                        <h1>&#128200 <a href="https://ghappy112.pythonanywhere.com/shiny_dashboards">Shiny Dashboards</a></h1>
                        <br>
                        <h1>&#128201 <a href="https://public.tableau.com/app/profile/greg1281/vizzes">Tableau Dashboards</a></h1>
                    </div>
                </div>
            </body>
        </html>
    '''

@app.route('/contact')
def contact():
    return '''
        <html>
            <head>
                <meta charset="UTF-8">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
            <style>
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                        <br>
                        <h1>&#128101 <a href="https://www.linkedin.com/in/gregory-happ-7bb578138/">Connect with me on LinkedIn!</a></h1>
                        <br>
                        <h1>&#128231 <a href="mailto: [greghapp700@gmail.com]?subject= &body=">Email Me!</a></h1>
                    </div>
                </div>
            </body>
        </html>
    '''

@app.route("/reddit_political_sentiment_analysis")
def reddit_political_sentiment():
    html = '''
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
        </head>
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
        <style>
            /* Apply Roboto font to the body */
            body {
                font-family: 'Roboto', sans-serif;
            }

            /* Apply Roboto to headings */
            h1, h2, h3 {
                font-family: 'Roboto', sans-serif;
            }

            .left-justified-text {
                display: inline-block; /* Make the container adapt to its content */
                text-align: left; /* Left justify the text inside */
            }
        </style>
        <body onload="mainJSFunction()">
            <div style="text-align:center;">
                <h1>Political Candidates' Reddit Sentiment Dashboard</h1>
                <!-- <p>Dashboard updates every 3 hours with the latest Reddit data</p> -->
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
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
            </head>
            <script>
                function mainJSFunction() {
                    // Get the screen width and height
                    const screenWidth = window.innerWidth;
                    const screenHeight = window.innerHeight;

                    // Get iframes IDs
                    var iframe1 = document.getElementById('iframeID1')
                    var iframe2 = document.getElementById('iframeID2')
                    var iframe3 = document.getElementById('iframeID3')
                    var iframe4 = document.getElementById('iframeID4')
                    var iframe5 = document.getElementById('iframeID5')

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

                    // Set iframes widths and heights
                    iframe1.width = width;
                    iframe1.height = height;
                    iframe2.width = width;
                    iframe2.height = height;
                    iframe3.width = width;
                    iframe3.height = height;
                    iframe4.width = width;
                    iframe4.height = height;
                    iframe5.width = width;
                    iframe5.height = height;
                }
            </script>
            <style>
                /* Apply Roboto font to the body */
                body {
                    font-family: 'Roboto', sans-serif;
                }

                /* Apply Roboto to headings */
                h1, h2, h3 {
                    font-family: 'Roboto', sans-serif;
                }

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

                .left-justified-text {
                    display: inline-block; /* Make the container adapt to its content */
                    text-align: left; /* Left justify the text inside */
                }
            </style>
            <body onload="mainJSFunction()" style="background-color:black;">
                <div style="text-align: center;">
                    <div class="left-justified-text">
                        <h1 style="color:white;">Greg Happ</h1>
                        <h1 style="color:white; b">Data Science & Data Analytics</h1>
                        <form method="get" action="/about">
                            <button type="submit" class="button">About</button>
                        </form>
                        <form method="get" action="/coding_languages">
                            <button type="submit" class="button">Coding Languages</button>
                        </form>
                        <form method="get" action="/projects">
                            <button type="submit" class="button">Portfolio</button>
                        </form>
                        <form method="get" action="/contact">
                            <button type="submit" class="button">Contact</button>
                        </form>
                    </div>
                </div>
                <br>
                <div style="text-align: center;">
                    <h1 style="color:white;">Shiny Dashboards</h1>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112">GitHub</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID1" frameborder="0" src="https://ghappy112.shinyapps.io/Super_Store/"></iframe>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/super_store">GitHub for this Dashboard</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID2" frameborder="0" src="https://ghappy112.shinyapps.io/iris_clustering/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle in Bottom Left Corner of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/iris_clustering">GitHub for this Dashboard</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID3" frameborder="0" src="https://ghappy112.shinyapps.io/lending_club/"></iframe>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/lending_club">GitHub for this Dashboard</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID4" frameborder="0" src="https://ghappy112.shinyapps.io/about_me_network_graph/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle in Bottom Left Corner of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/about_me">GitHub for this Dashboard</a></h1>
                    <br>
                    <br>
                    <br>
                    <iframe id="iframeID5" frameborder="0" src="https://ghappy112.shinyapps.io/coding_skills/"></iframe>
                    <h2 style="color:white;">Filter Panel Toggle in Bottom Left Corner of Dashboard</h2>
                    <br>
                    <h1><a href="https://github.com/ghappy112/R_Shiny_dashboards_ghappy112/tree/main/coding_skills">GitHub for this Dashboard</a></h1>
                </div>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
