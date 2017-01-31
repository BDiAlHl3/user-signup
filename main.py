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

# html boilerplate for the top of every page ...
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style>
        label {
            margin-left: 200px;
        }
        p {
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
<form action="/name" method="post">
    <br>
    <br>
<!--Field for adding user_name ...-->
    <label>Please enter Username:
        <input type="text" name = "username"/>
    </label>
<form/>
"""

pw_form = """
<form action="/pw" method="post">
    <br>
    <br>
<!-- Field for adding password ...-->
    <label>Please enter Password:
        <input type="password" name = "password"/>
    </label>
    <p><i>Password must be 8 - 20 characters,
        contain only digits and letters and
        is case-sensitive.</i>
    </p>
<form/>
"""

pw_verify_form = """
<form action="/pwver" method="post">
<!-- Field for verifying password ...-->
    <label>Please verify Password:
        <input type="password" name="verify"
    </label>
<form/>
"""

email_form = """
<form action="/email" method="post">
<!-- Field for entering email address ...-->
    <br>
    <br>
    <label>Please enter Email:
        <input type="text" style="width:50em;" name="email"
    </label>
    <p>
        <i>Note: Email address is optional !</i>
    </p>
    <br>
    <center>
        <input type="submit" value="Submit"/>
    </center>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    """ Handles root '/' requests """
    # The default for self.response.headers is html,
    # so self.response.headers is not needed ...
    # self.response.headers['Content-Type'#] = 'text/plain'

    # get in mainhandler just displays the form ...
    def get(self):
        username=""

        #% {'username' : }

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + \
        "</p>" if error else ""

        content = page_header + name_form + pw_form + \
        pw_verify_form + email_form + \
        "in MainHandler" + error_element
        self.response.write(content)

#class MainProcess(webapp2.RequestHandler):
class NameEnter(webapp2.RequestHandler):
    """ Handles '/name' requests """

    def post(self):
        error_msg = ""
        # Check to see if user input username ...
        user_name = self.request.get("username")

        # Username cannot be blank ...
        if " " in user_name:
            error_msg = 'User name cannot be blank; please reenter.'

        if error_msg != "":
            error_msg = cgi.escape(error_msg)
            self.redirect('/?error=' + error_msg)

        content = page_header + name_form + pw_form + \
        pw_verify_form + email_form + \
        "<p>In MainProcess</p>" + \
        "<p>username=*" + user_name + "*</p>"
        self.response.write(content)
        #self.response.write(content)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/name', NameEnter)

], debug=True)
