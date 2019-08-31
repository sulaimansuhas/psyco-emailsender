import psycopg2
import smtplib
conn = psycopg2.connect(user = "suhas", database = "suhas", host = "localhost", password = "password")
cur_test= conn.cursor()
cur_email = conn.cursor()
sender = smtplib.SMTP('smtp.gmail.com', 587)
sender.starttls()
sender.login("suhasnarreddy@gmail.com","p**s**rd")
message = "another row added"
cur_test.execute("""SELECT COUNT(*) FROM test""")
initial_row_no = cur_test.fetchall()
while True:
	cur_test.execute("""SELECT COUNT(*) FROM test""")
	current_row_no = cur_test.fetchall()
	if (current_row_no[0][0]>initial_row_no[0][0]):
		cur_email.execute("""SELECT * FROM email""")
		cur_test.execute("""SELECT * FROM test""")
		print(current_row_no[0][0])
		message = str(cur_test.fetchall()[(current_row_no[0][0]-1)][0]) + " "
		cur_test.execute("""SELECT * FROM test""")
		message = message + cur_test.fetchall()[(current_row_no[0][0]-1)][1] 		
		emails = cur_email.fetchall()
		for email in emails:
			sender.sendmail("suryasuhas@gmail.com", email[0], message)
		initial_row_no = current_row_no
	
