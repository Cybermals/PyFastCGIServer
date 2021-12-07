RESPONSE = """<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <p>Hello World!</p>
        <p>Args: {}</p>
    </body>
</html>\r\n"""


stdout.write(b"Content-Type: text/html\r\n\r\n")
stdout.write(RESPONSE.format(args).encode("ascii"))
