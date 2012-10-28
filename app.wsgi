import os
from cgi import escape
from urlparse import parse_qs

def application(environ, start_response):
    page = escape(parse_qs(environ['QUERY_STRING']).get('page', [''])[0])

    status = '200 OK'
    output = make_output(page)
 
    response_headers = [('Content-type', 'text/html	'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
 
    return [output]

def make_output(page):
	if len(page) == 0:
		page = "home"

	page_path = "/srv/http/views/"+page+".html"
	
	if os.path.exists(page_path):
		page_content = open(page_path).read()
	else:
		page_content = open("/srv/http/static/html/not_exists.html").read()

	return open("/srv/http/static/html/header.html").read() + open("/srv/http/static/html/menu.html").read() + page_content + open("/srv/http/static/html/footer.html").read()
