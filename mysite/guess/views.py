
from django.http import HttpResponse


def index(request):
    return HttpResponse("Add a number to the URL to guess the secret between 1 and 100 like /guess/25")
    #return HttpResponse("Hello, world. 3c2140d1 is the guess owner.")

def guess(request, guessvalue) :
    if guessvalue > 21:
        response = """<html><body><p>Too high</p></body></html>"""
    elif guessvalue < 21:
        response = """<html><body>
        <p>Too low</p>
        </body></html>"""
    elif guessvalue == 21:
        response = """<html><body>
        <p>Just right</p>
        </body></html>"""
    return HttpResponse(response)