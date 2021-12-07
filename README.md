# PyFastCGIServer
A fast CGI server for Python.


## Instructions
1. install your web server of choice
2. install Python
3. install the fastcgi package from the Python Package Index
4. run "main.py" on the server you want your Python fast CGI server on
5. configure your web server to pass .py pages to port 9001 of your Python
fast CGI server
6. each .py page will have globals called "stdin", "stdout", and "args"
7. "stdin" will be a stream containing the data for a HTTP POST request
8. "stdout" will be a stream that you write your response to
9. "args" will be the query params passed via the web address (everything
after the "?"; converted to a dictionary)
