from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.core.mail import send_mail
from urgentcarelosgatos.settings import EMAIL_HOST_USER
from django.http import JsonResponse

class Home(TemplateView):
	
	template_name = 'home/home.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		return context



class Billing(TemplateView):
	template_name = 'home/billing.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Billing, self).get_context_data(*args, **kwargs)
		return context



class Services(TemplateView):
	template_name = 'home/services.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Services, self).get_context_data(*args, **kwargs)
		return context



	
class Facilty(TemplateView):
	template_name = 'home/facilty.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Facilty, self).get_context_data(*args, **kwargs)
		return context

class Blog(TemplateView):
	template_name = 'home/blog.html'	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Blog, self).get_context_data(*args, **kwargs)
		return context


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



def sending_email(request):
	
	my_response = 'OK'
	
	if request.is_ajax():
		form_name = request.POST.get('form_name')
		form_email = request.POST.get('form_email')
		form_subject = request.POST.get('form_subject')
		form_phone = request.POST.get('form_phone')
		form_message = request.POST.get('form_message')

		message = 'Name: ' + form_name + '\n' + 'Phone: ' + form_phone + '\n' + 'Email: ' + form_email + '\n' + form_message
		
		email_from = EMAIL_HOST_USER
		recipient_list = ['pacoqara@gmail.com',]
		send_mail( form_subject, message, form_email, recipient_list )
		
	data = { 'my_response': my_response }

	return JsonResponse(data)
        



def make_appointment(request):
	
	my_response = 'OK'
	
	if request.is_ajax():
		modal_form_name = request.POST.get('modal_form_name')
		modal_form_email = request.POST.get('modal_form_email')
		modal_form_phone = request.POST.get('modal_form_phone')
		
		modal_form_appontment_date = request.POST.get('modal_form_appontment_date')
		modal_form_message = request.POST.get('modal_form_message')

		message = 'Name: ' + modal_form_name + '\n' + 'Phone: ' + modal_form_phone + '\n' + 'Email: ' + modal_form_email + '\n'  + 'Appointment date: '  + modal_form_appontment_date + '\n' +'Message body: ' + modal_form_message 
		
		email_from = EMAIL_HOST_USER
		recipient_list = ['pacoqara@gmail.com',]
		send_mail( 'Appoinment', message, modal_form_email, recipient_list )
		
	data = { 'my_response': my_response }

	return JsonResponse(data)
        
    

    
def make_appointment_home(request):
	
	my_response = 'OK'
	
	if request.is_ajax():
		form_name = request.POST.get('form_name')
		form_email = request.POST.get('form_email')
		form_phone = request.POST.get('form_phone')
		form_reservation_date = request.POST.get('form_reservation_date')
		form_message = request.POST.get('form_message')

		message = 'Name: ' + form_name + '\n' + 'Phone: ' + form_phone + '\n' + 'Email: ' + form_email + '\n'  + 'Appointment date: ' + form_reservation_date + '\n' + 'Message body: ' + form_message 
		
		email_from = EMAIL_HOST_USER
		recipient_list = ['pacoqara@gmail.com',]
		send_mail( 'Appoinment', message, form_email, recipient_list )
		
	data = { 'my_response': my_response }

	return JsonResponse(data)
        
    
    
