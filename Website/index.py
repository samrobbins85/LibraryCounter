from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        import urllib
        from bs4 import BeautifulSoup
        quote_page = 'https://www.dur.ac.uk/library/'
        page = urllib.request.urlopen(quote_page)
        data = page.read()
        sibling_soup = BeautifulSoup(data, 'html.parser')
        tag = int(sibling_soup.svg.text.replace(",",""))
        self.wfile.write(str(tag).encode())



        return