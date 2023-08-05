from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import UserInfo,Course
# Create your views here.
def home(request):
    return render(request,'home.html')
def handle_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')

        try:
            user_info = UserInfo.objects.get(username=username)
            data = {
                'username': user_info.username,
                'email': user_info.email,
                'applied_in_companies': user_info.applied_in_companies,
                'rejected': user_info.rejected,
                'in_process': user_info.in_process,
                'shortlisted': user_info.shortlisted,
            }
            return JsonResponse(data)
        except UserInfo.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
def userinformation(request):
    return render(request,'userdetails.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
def aboutus(request):
    return render(request,'aboutus.html')