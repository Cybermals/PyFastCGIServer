#!/usr/bin/python3
"""A CGI server."""

from socketserver import TCPServer
from fastcgi import FcgiHandler


#Classes
#=============================================================================
class RequestHandler(FcgiHandler):
    """HTTP request handler."""
    def handle(self):
        """Handle the request."""
        #Parse query
        args = dict([arg.split("=") for arg in self.environ["QUERY_STRING"].split("&")])
        
        #Load Python script and compile it
        with open(self.environ["SCRIPT_FILENAME"], "r") as f:
            co = compile(f.read(), self.environ["SCRIPT_FILENAME"], "exec")
            
        #Execute Python script in a sandbox
        print("Script: '{}'".format(self.environ["SCRIPT_FILENAME"]))
        print("Args: {}".format(args))
        print("Stdin: {}".format(self["stdin"].read()))
        print()
        
        sandbox = {
            "__builtins__": __builtins__, 
            "stdin": self["stdin"], 
            "stdout": self["stdout"],
            "args": args
        }
        exec(co, sandbox)
        
        
#Entry Point
#=============================================================================
if __name__ == "__main__":
    #Start the fast CGI server
    with TCPServer(("127.0.0.1", 9001), RequestHandler) as server:
        server.serve_forever()
        
