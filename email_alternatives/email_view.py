from django.shortcuts import render

def email_design(req):
    return render(req, 'avaliation.html')