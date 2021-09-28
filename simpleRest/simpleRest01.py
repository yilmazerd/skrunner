#!/usr/bin/env python  
from flask import Flask, request
import subprocess
import time

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def get_user():
  username = request.form.get('username')
  #request_data = request.get_json()
  #s = " "
  #for r in request_data:
  #	s = s + r
  #print(request.data)	  	
  #password = request.form['password']
  #login(arg,arg) is a function that tries to log in and returns true or false
  f = open("demofile2.py", "a")
  request_data_str = str(request.data,'utf-8')
  f.write(request_data_str)
  f.close()
  #time.sleep(1)
  
  #r = subprocess.call("python demofile2.py",shell=False) 
  #r = subprocess.call("/Users/erdemyilmaz/Desktop/JAVAPROJECTS/pythonContainer/simpleRest/demofile2.py",shell=False) 
  #print(r)
  #r = subprocess.call("cat simpleRest01.py ",shell=False) 
  #p = subprocess.Popen(["pwd"], stdout=subprocess.PIPE)
  string="python demofile2.py"
  result=subprocess.getoutput(string)
  #print("########### ",result)
  subprocess.getoutput("rm demofile2.py")
  return result
