from flask import Flask, request
app=Flask(__name__)


@app.route('/')
def home_page():
    return "welcome to My page"

@app.route('/search')
def search_page():
    return "what you want?"

@app.route('/string_upper')
def string_up():
    a=request.args.get('a')
    return a.upper()

@app.route('/string_lower')
def string_lo():
    b=request.args.get('b')
    return b.lower()
@app.route('/string_title')
def string_tit():
    c=request.args.get('c')
    
    return c.title()

@app.route('/string_split')
def string_split():
    d=request.args.get('d')
    
    return d.split()
if __name__=="__main__":
    app.run(debug=True)