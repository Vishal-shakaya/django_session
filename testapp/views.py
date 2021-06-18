from django.http.response import HttpResponse
from django.shortcuts import render



def SetSession(request):
    # set Session id when user login : 
    request.session['session_id'] = 'vishalshakaya12345456'
    return  render(request,'Session/SetSession.html')

def GetSession(request):
    # get session id to check user is authenticated or valid or not :  
    session_id = request.session['session_id']
    context = {'session_id':session_id}
    return render(request,'Session/GetSession.html',context)
    

def DeleteSession(request):
    # logout user and delete  session id  assing to him / her: 
    is_session =  'session_id' in request.session
    if is_session:
      del request.session['session_id']
    return HttpResponse('<h1> Logout user Session deleted  </h1> ')