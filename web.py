from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<head>
		<title> SOFTWARE COMPANIES REVENUE</title>
	</head>
	<body>
	<table border="2" cellspacing="3" cellpadding="4" width="40" height="60">
		<tr allign="center">
			<th bgcolor="blue">RANKING</th>
			<th bgcolor="blue">COMPANIES</th>
			<th bgcolor="blue">REVENUE</th>
		</tr>
		<tr allign="center">
			<th bgcolor="pink">1</th>
			<th  bgcolor="yellow">MICROSOFT</th>
			<th  bgcolor="purple">$203.08 billion</th>
		</tr>
		<tr allign="center">
            <th bgcolor="pink">2</th>
			<th  bgcolor="yellow">ORACLE</th>
			<th  bgcolor="purple">$46.07 billion</th>
        </tr>
		<tr allign="center">
            <th bgcolor="pink">3</th>
			<th  bgcolor="yellow">SAP SE</th>
			<th  bgcolor="purple">$32.97 billion</th>
        </tr>
		<tr allign="center">
            <th bgcolor="pink">4</th>
			<th  bgcolor="yellow">SALESFORCE</th>
			<th  bgcolor="purple">$30.29 billion</th>
        </tr>
		<tr allign="center">
            <th bgcolor="pink">5</th>
			<th  bgcolor="yellow">ADOBE</th>
			<th  bgcolor="purple">$17.61 billion</th>
        </tr>
    </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()