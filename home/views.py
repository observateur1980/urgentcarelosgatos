from django.shortcuts import render
from django.views.generic.base import TemplateView



class Home(TemplateView):
	template_name = 'home/home.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		return context



# class About(TemplateView):
# 	template_name = 'home/about.html'	
	
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(About, self).get_context_data(*args, **kwargs)
# 		return context



# class Services(TemplateView):
# 	template_name = 'home/services.html'	
	
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(Services, self).get_context_data(*args, **kwargs)
# 		return context



	
# class Events(TemplateView):
# 	template_name = 'home/events.html'	
	
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(Events, self).get_context_data(*args, **kwargs)
# 		return context


# class Contact(TemplateView):
# 	template_name = 'home/contact.html'	
	
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(Contact, self).get_context_data(*args, **kwargs)
# 		return context