from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from wall_app.models import * 
import bcrypt

def index(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=first_name, last_name=last_name,email= email, password=hash)
            request.session['userId'] = user.id         
            return redirect('/msg')
    return render(request,'index.html')



def login(request):
    if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                user = User.objects.get(email=email)
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    request.session["userId"] = user.id
                return redirect('/wall')
            except User.DoesNotExist:
                print("User does not exist")
    return redirect('/')

def logout(request):
    del request.session['userId']
    return redirect('/')

def wall(request):
    user = User.objects.get(id=request.session["userId"])
    context = {
        'messages' : Message.objects.all(),
        'comment': Comment.objects.all(),
        'user' : user
    }
    return render(request, 'wall.html', context)

def msg(request):
    if request.method == 'POST':
        message = Message.objects.create(message=request.POST['message'])
        message.save()
    return redirect('/wall')

def comment(request):
    if request.method == 'POST':
        comment = Comment.objects.create(comment=request.POST['comment'], user_id = User.objects.get(id = request.session['userId']), message_id = Message.objects.get(id = request.POST['msg_id']))
        comment.save()
    return redirect('/wall')