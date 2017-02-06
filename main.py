#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

# html boilerplate for the top of every page ...
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style>
        div {
            margin-left: 200px;
        }
    </style>
</head>
<body>
    <h1><center><a href="/">User Signup</a> Assignment</center>
    </h1>
</body>
</html>
"""

name_form = """
<form method="post">
    <br>
    <br>
<!--Field for adding user_name ...-->
    <div>
        <label>Please enter Username:
            <input type="text" name = "username" value="%(username)s"/>
        </label>
        <label style="color:red">  %(err_1)s</label>
        <p>
            <i>Username must be 3 - 20 characters,
            contain only digits, letters, dashes or underscores, and
            is case-sensitive.</i>
        </p>
    </div>
<form/>
"""

pw_form = """
<form method="post">
    <br>
    <br>
<!-- Field for adding password ...-->
    <div>
        <label>Please enter Password:
            <input type="password" name = "password" value="%(password)s"/>
        </label>
        <label style="color:red">  %(err_2)s</label>
        <p>
            <i>Password must be 3 - 20 characters,
            may contain digits, letters or any characters, and
            is case-sensitive.</i>
        </p>
    </div>
<form/>
"""

pw_verify_form = """
<form method="post">
<!-- Field for verifying password ...-->
    <div>
        <label>Please verify Password:
            <input type="password" name="verify" value="%(verify)s"/>
        </label>
        <label style="color:red">  %(err_3)s</label>
    </div>
<form/>
"""

email_form = """
<form method="post">
<!-- Field for entering email address ...-->
    <br>
    <br>
    <div>
        <label>Please enter Email:
            <input type="text" style="width:50em;" name="email" value="%(email)s"/>
        </label>
        <label style="color:red">  %(err_4)s</label>
        <p>
            <i>Note: Email address is optional !</i>
        </p>
    </div>
    <br>
    <center>
        <input type="submit" value="Submit"/>
    </center>
</form>
"""

welcome_form = """
<form action="/welcome" method="post"</form>
    <label>Welcome, %(welcomename)s</label>
"""

# ^ and & are beginning and end of the test string ...
user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pw_re = re.compile(r"^.{3,20}$")
email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def escape_html(s):
    return cgi.escape(s, quote  =True)

def ValidName(name):
    if " " not in name:
        return user_re.match(name)

def ValidPassWord(password):
    if " " not in password:
        return pw_re.match(password)

def ValidVerify(password,pw_verify):
    if password == pw_verify:
        return True

def ValidEmail(email):
    if " " not in email:
        return email_re.match(email)

class MainHandler(webapp2.RequestHandler):
    """ Handles root '/' requests """
    # The default for self.response.headers is html,
    # so self.response.headers is not needed ...
    # self.response.headers['Content-Type'#] = 'text/plain'

    # get in mainhandler just displays the form ...
    def WriteForm(self,username="",un_err="",
                       password="",pw_err="",
                       verify="",pwv_err="",
                       email="",em_err=""):
        content=page_header + name_form + pw_form + \
        pw_verify_form + email_form
        #self.response.out.write(content % {"error":error,
        self.response.out.write(content % {"username":escape_html(username),
                                           "err_1":un_err,
                                           "password":escape_html(password),
                                           "err_2":pw_err,
                                           "verify":escape_html(verify),
                                           "err_3":pwv_err,
                                           "email":escape_html(email),
                                           "err_4":em_err
                                           })

    def get(self):
        self.WriteForm()

    def post(self):
        # Preserve what the user entered ...
        user_name = self.request.get('username')
        user_pw = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        # Initialize Error messages ...
        un_err = ""
        pw_err = ""
        pwv_err = ""
        email_err = ""

        # Save validated input ...
        name = ValidName(user_name)
        password = ValidPassWord(user_pw)
        #email = ValidEmail(user_email)
        #if user_email and not user_name.isspace():
        email=""
        em_err=""
        if user_email:
            email = ValidEmail(user_email)

        err_flag = False
        # Check for error messages ...
        if not name:
            un_err="Invalid User Name"
            err_flag = True
        if not password:
            pw_err = "Invalid Password"
            user_pw=""
            err_flag = True

        if not ValidVerify(user_pw,user_verify):
            pwv_err = "This field must match the password you just entered!"
            err_flag = True

        if not email and user_email:
            em_err = "Invalid Email"
            err_flag = True

        if err_flag:
            #self.WriteForm(user_name,un_err)
            self.WriteForm(user_name,un_err,user_pw,pw_err,
                           user_verify,pwv_err,user_email,em_err
                           )
        else:
            self.redirect("/welcome?welcomename="+user_name)

class WelcomeHandler(webapp2.RequestHandler):
        def get(self):
            out_content=page_header+welcome_form

        # def post(self):
            user_name=self.request.get('welcomename')
            self.response.out.write(out_content % {"welcomename":user_name}+"!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
