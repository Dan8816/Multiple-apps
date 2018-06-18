from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    print(response)
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "djangoapp/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = request.POST['name']  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    response = "placeholder to display blog "
    return HttpResponse(response + number)

def edit(request, number):
    response = "placeholder to edit blog "
    return HttpResponse(response + number)

def destroy(request, number):
    return redirect('/')