from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	x = d.get('x', [''])[0]
	y = d.get('y', [''])[0]
	sum = 0
	mul = 0
	answer = ''
	try:
		x, y = float(x), float(y)
		sum = x + y
		mul = x * y
	except ValueError:
		answer = 'Please write the number'
		sum = 0
		mul = 0 
		
	response_body = html % {
		'sum' : sum,
		'mul' : mul,
		'answer' : answer,
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]
