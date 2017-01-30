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
        main_form = """
        <form action="/main" method="post">
            <br>
            <br>
        <!--Field for adding user_name ...-->
            <label>Please enter Username:
                <input type="text" name = "username"/>
            </label>

        <!-- Field for adding password ...-->
            <br>
            <br>
            <label>Please enter Password:
                <input type="password" name = "password"/>
            </label>
            <p><i>Password must be 8 - 20 characters,
                contain only digits and letters and
                is case-sensitive</i>
            </p>

        <!-- Field for verifying password ...-->
            <label>Please verify Password:
                <input type="password" name="verify"
            </label>

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

        content = page_header + main_form
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
