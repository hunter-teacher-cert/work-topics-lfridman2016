from flask import Flask, request, session 
from flask import render_template

app = Flask(__name__)
app.secret_key="something"

user = {'username': 'Lyuba'}
posts = [
            {
                'name': 'Mike',
                'description': 'Example Flask app',
                'link': 'https://replit.com/@LyubaFridman/flask-web-demo#app.py'
            },
            {
                'name': 'Lyuba',
                'description': 'CS Topics Project',
                'link': 'https://replit.com/@LyubaFridman/work-topics-lfridman2016#flask/app.py'
            }
        ]     
# the "root" route
@app.route('/')
@app.route('/index')
def index():  
  return render_template("index.html")

@app.route("/projects", methods=['GET','POST'])
def projects():      
  #print("Start of session")
  #print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1
  print("Count ")
  print(session['count'])    
  #if 'posts' not in session:
  if not session.get('posts'):
    #print("Not in session")
    session['posts'] = posts
  if request.method=="GET": 
    return render_template('posts.html', title='Home', user=user, posts=session['posts'])
  else:
    session['count'] = session['count'] +1
    #print("Session before append")
    #print(session['posts'])
    session['posts'].append(
      {'name': request.form['name'],
      'description': request.form['description'],
      'link': request.form['link']}
    )
    #print("Session after append")
    #print(session['posts'])
    #print(session['count'])

  return render_template('posts.html',title='Projects', user=user, posts=session['posts'])
   
app.run(host="0.0.0.0",port=5000,debug=True)