from cgi import parse_qs
from template import html

def application(environ, start_response) :
    d = parse_qs(environ['QUERY_STRING'])
    sum = 0
    mul = 0
    x = d.get('x',[''])[0]
    y = d.get('y',[''])[0]
    if x.isdigit() and y.isdigit() :
	x,y = int(x), int(y)
	sum = [x+y]
	mul = [x*y]
    response_body = html%{
	    'sum' : sum,
	    'mul' : mul
	}
    
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
	('Content-Length', str(len(response_body)))
    ])
    return [response_body]
