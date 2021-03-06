from bottle import Bottle, static_file, response, request, template, run
from scrapeImport import scrape
import os

# # Get required port, default to 5000.
# port = os.environ.get('PORT', 5000)

# # Run the app.
# run(host='0.0.0.0', port=port)

app = Bottle()

tournamentName = "None"

@app.route('/')
def index():
    return template("index.tpl", {'tournament':tournamentName})

@app.post('/')
def formhandler():

    tournamentURL = request.forms.get('input')
    # print(tournament)
    tournamentName = scrape(tournamentURL)
    return template("index.tpl", {'tournament':tournamentName})

@app.route("/about")
def about():
    # scrape(link)
    response.content_type = 'text/plain'
    return "hii"

@app.route("/downloadFile")
def download():
    return static_file('speaks.xlsx', root='', download='speaks.xlsx')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port, debug=True)