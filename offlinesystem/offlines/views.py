
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

def homepage(request):

	if request.method == 'POST':
		companyname= request.POST['companyname']
		messageemail = request.POST['messageemail']
		# file = request.POST['file']
		message = request.POST['message']


 #Sending an email
		send_mail(
			companyname, #subject
			message, #message
			messageemail, #from who's email
			['hello@africartrack.com'], # to which email
		)


		return render(request, 'home.html', {'companyname':companyname})

	else:
		return render(request, 'home.html', {})

				# message = request.POST['message']

		# send_mail('Contact Form',
		#  message, 
		#  settings.EMAIL_HOST_USER,
		#  ['appcode254@gmail.com'], 
		#  fail_silently=False)