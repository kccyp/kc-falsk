from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
  return "home page"

@app.route('/hello')
def hello():
  # return render_template('index.html', name="Alex")
  return render_template('index.html')


@app.route('/articles')
def api_articles():
  return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
  return 'You are reading ' + articleid

# Request Methods (HTTP Verbs)
@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
  if request.method == 'GET':
    return "ECHO: GET\n"

  elif request.method == 'POST':
    return "ECHO: POST\n"

  elif request.method == 'PATCH':
    return "ECHO: PACTH\n"

  elif request.method == 'PUT':
    return "ECHO: PUT\n"

  elif request.method == 'DELETE':
    return "ECHO: DELETE"


if __name__ == '__main__':
  app.run(debug = True)