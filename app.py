from flask import Flask
from flask import render_template, url_for, redirect, request
import requests

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/search", methods=['POST'])
def form_submit():
    user_query = request.form['search_query']
    redirect_url = url_for('.search', query_string=user_query)
    return redirect(redirect_url)


@app.route("/search/<query_string>", methods=['GET'])
def search(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q":query_string}

    headers = {
        'x-rapidapi-key': "5a66af61acmsh346a479a795a5bbp1ed712jsn994b808dd826",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    return render_template("search-result.html",data = data)




    

@app.route("/")
def homepage():
    user_account = "Dick"
    return render_template("landing-page.html", user_account = user_account, account_type = "Premium", length= len(user_account))

@app.route("/error")
def errorpage():
	return  render_template("error404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")


