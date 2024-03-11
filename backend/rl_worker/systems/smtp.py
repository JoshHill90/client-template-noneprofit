import ssl
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from functools import reduce
from .kekeper import *
from logs.logging_config import logging





#-------------------------------------------------------------------------------------------------------#
# Secret Values
#-------------------------------------------------------------------------------------------------------#


class AutoReply:
    
	def __init__(self) -> None:
		
		self.email_host =  worker_host
		self.send_from = worker_send_email
		self.email_password = worker_send_passwd
		self.email_port = worker_port
		self.receive_email = worker_manager
	#------------------------#
	# Contact form auto reply
	#------------------------#

	def respond_to_form_submited(self, email, name, site, email2=None):
		print('preparing message')
		
		contact_subject = "Thanks for Submitting the Questionnaire"

		contact_body = f"""
Hi {name},

Thank you for submitting the questionnaire for {site} and kicking off the project process. I will be reaching out to you shortly to discuss the project details and cover the initial phase.

Best regards,
Josh
Josh@silkthreaddev.com
Silkthreaddev.com
		"""

		mailer = EmailMessage()
		
		mailer['From'] = formataddr(("NoReply - Silk Thread Dev", f"{self.send_from}"))
		mailer['To'] = [email, email2]
		mailer['Subject'] = contact_subject
		mailer.set_content(contact_body)

		with smtplib.SMTP(self.email_host, self.email_port) as server:
			try:
				server.starttls()
				server.login(self.send_from, self.email_password)
				server.sendmail(self.send_from, [email, email2], mailer.as_string())
				server.close()
				print('email sent to client')
			except Exception as e:
					print(f'Error when email sent to client {e}')
					logging.error("Error when email sent to client : %s", str(e))
					return (str(e))
    
	def new_form_submited(self, dataSet):
		print('preparing message' , self.send_from )
		contact_body = ''
		contact_subject = "New form Submited"
		for info_key, info_value in dataSet.items():
			quest_answer = f"Q: {info_key} \n\n A: {info_value} \n\n"
			contact_body += quest_answer
			
		

		mailer = EmailMessage()
		
		mailer['From'] = formataddr(("Josh - Silk Thread Dev", f"{self.send_from}"))
		mailer['To'] = self.receive_email
		mailer['Subject'] = contact_subject
		mailer.set_content(contact_body)

		with smtplib.SMTP(self.email_host, self.email_port) as server:
			try:
				server.starttls()
				server.login(self.send_from, self.email_password)
				server.sendmail(self.send_from, self.receive_email, mailer.as_string())
				server.close()
				print('email sent')
			except Exception as e:
					print(f'Error when email sent to me {e}')
					logging.error("Stripe invoice create operation failed: %s", str(e))
					return (str(e))

	def respond_to_contact_form(self, email, name, subject):
		print('preparing message')
		
		contact_subject = "Appreciation for Reaching Out"

		contact_body = f"""


Hey {name},

I hope this message finds you in good spirits. I wanted to extend my sincere thanks for reaching out to me regarding {subject}. Your initiative and interest mean a lot.

I'm currently going through messages and wanted to assure you that I'm fully committed to providing the support or information you need. Expect to hear from me shortly with a thoughtful response tailored to your inquiry.

Should you have any additional questions or thoughts in the meantime, please feel free to share them. I'm here to lend a hand in any way I can.

Once again, thank you for taking the time to connect. I'm looking forward to assisting you further on this journey.

Best regards,
Josh
Josh@silkthreaddev.com
Silkthreaddev.com
		"""

		mailer = EmailMessage()
		
		mailer['From'] = formataddr(("NoReply - Silk Thread Dev", f"{self.send_from}"))
		mailer['To'] = email
		mailer['Subject'] = contact_subject
		mailer.set_content(contact_body)

		with smtplib.SMTP(self.email_host, self.email_port) as server:
			try:
				server.starttls()
				server.login(self.send_from, self.email_password)
				server.sendmail(self.send_from, email, mailer.as_string())
				server.close()
				print('email sent to client')
			except Exception as e:
					print(f'Error when email sent to client {e}')
					logging.error("Error when email sent to client : %s", str(e))
					return (str(e))
    
	
	
				
#### Test 
"""test_send = os.getenv("TEST_SEND")

subject_test = "TEST"

body_test ="body"

SMTP = AutoReply()

SMTP.contact_request(test_send, 'john')
print('smtp request')
SMTP.contact_alart(test_send, 'john', subject_test, body_test)"""

