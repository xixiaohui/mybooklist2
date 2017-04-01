from django.http import HttpResponse

from django.template import Context,Template,loader
# Create your views here.



# def index(request):
# 	template = Template("my name is  {{ my_name }}.")

# 	context = Context({
# 		'my_name':'xixiaohui',
# 	})

# 	return HttpResponse(template.render(context))

def index(request):
	template = loader.get_template("mybooklist/index.html")

	context = Context({
		'my_name':'xixiaohui',
	})

	return HttpResponse(template.render(context))	
