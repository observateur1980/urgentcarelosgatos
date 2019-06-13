from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.core.mail import send_mail
from urgentcarelosgatos.settings import EMAIL_HOST_USER


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


class Contact(FormView):
	template_name = 'home/contact.html'
	form_class = ContactForm
	success_url = 'contact'

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(Contact, self).get_context_data(*args, **kwargs)		
	# 	context["bck_image"] = 'images/contact.jpg'
	# 	context["active_page"] = 'contact'
	# 	return context
	
	def form_valid(self, form):
		name = form.cleaned_data['name']
		phone = form.cleaned_data['phone']
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject']
		message =form.cleaned_data['message']
		message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + message
		email_from = EMAIL_HOST_USER
		recipient_list = ['pacoqara@gmail.com',]
		send_mail( subject, message, email_from, recipient_list )
		return super(Contact, self).form_valid(form)