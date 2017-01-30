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

class MainHandler(webapp2.RequestHandler):
    """ Handles root '/' requests """
    def get(self):

        # Field for adding user_name ...
        username_form = """
        <form action="/user" method="post">
            <br>
            <br>
            <label>Please enter Username:
                <input type="text" name = "user-name"/>
            </label>
            <input type="submit" value="User Name"/>
        </form>
        """

        # Field for adding password ...
        # Use <input> name for pw=self.request.get("password")
        # within post method for password ...
        pw_form = """
        <form action="/pw" method="post">
            <br>
            <br>
            <label>Please enter Password:
                <input type="text" name = "password"/>
            </label>
            <input type="submit" value="Password"/>
            <p><i>Password must be 8 - 20 characters,
                contain only digits and letters and
                is case-sensitive</i>
            </p>
        </form>
        """

        # Field for verifying password ...
        pw_verify_form = """
        <form action="/pw_verify" method="post">
            <br>
            <br>
            <label>Please verify Password:
                <input type="text" name="pw-verify"
            </label>
            <input type="submit" value="Verify Password"/>
        </form>
        """

        # Field for entering email address ...
        email_form = """
        <form action="/email" method="post">
            <br>
            <br>
            <label>Please enter Email:
                <input type="text" style="width:50em;" name="email"
            </label>
            <input type="submit" value="Email Address"/>
            <p>
                <i>Note: Email address is optional !</i>
            </p>
        </form>
        """


        content = page_header + username_form +pw_form \
            + pw_verify_form + email_form
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
