from flask import Flask, url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def base():
    return render_template('ex_navbar.html')



@app.route('/ex_login_page' , methods = ['POST', 'GET'])
def login_pro():
        return render_template('ex_login_page.html')

@app.route('/Users',methods = ['POST', 'GET'])
def Users():
   if request.method == 'POST':
      #result = request.form
      return render_template("after_login.html")

# REGISTRATION 
@app.route('/Registration')
def Registration():
    return render_template('ex_registration_page2.html')

@app.route('/Booking1')
def Booking():
    return render_template('ex_bookroom_page1.html')

#AFTER --- LOGIN 

@app.route('/after_login' , methods = ['POST', 'GET'])
def after_login():
        return render_template('after_login.html')

if __name__=='__main__':
    app.run(debug=True)