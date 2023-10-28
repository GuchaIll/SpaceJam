from flask import Flask, render_template

app = Flask(__name__, static_url_path = '/static')

@app.route("/")
def hello():
  return render_template('home.html')
print(__name__)
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
  

@app.route('Generate', methods=['POST'])
def Generate():
    # Your code to perform some action when the button is clicked
    print("called")
    return 'Action successful'  #