from django.http import HttpResponse

# Create your views here.



def index(request):

	return HttpResponse("你好，你正在mybooklist 的书单界面")