from django.http import HttpResponse
  
def home(request):
    return HttpResponse("<h2>Home</h2>")

def about(request):
    return HttpResponse("<h1>About us</h1>")

def contact(request):
    return HttpResponse("<h3>Contact</h3>")

def text(request):
    return HttpResponse("""
                        <h1>Hello world</h1>
                        <h2>Hello world</h2>
                        <h3>Hello world</h3>
                        <h4>Hello world</h4>
                        <h5>Hello world</h5>
                        <h6>Hello world</h6>
                        """)