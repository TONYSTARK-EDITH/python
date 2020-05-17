import os
import smtplib
import socket
import sqlite3
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import filedialog, messagebox, ttk


class gmail:
	def __init__(self):
		self.conn = sqlite3.connect("from_Email.db")
		self.con = sqlite3.connect("to_Email.db")
		self.conn_1 = self.conn.cursor()
		self.con_2 = self.con.cursor()
		self.c = self.conn.execute('''CREATE TABLE IF NOT EXISTS from_Mail
             (mail VARCHAR(100) , pwd VARCHAR(100))''')
		self.d = self.con.execute('''CREATE TABLE IF NOT EXISTS to_Mail
             (mail VARCHAR(100))''')
		self.root = Tk()
		self.root.title("Email ")
		self.root.iconphoto(False, PhotoImage(file="ab.png"))
		self.root.geometry("600x450+150+150")
		self.frame = Frame(self.root)
		self.frame.pack()
		self.frame_1 = Frame(self.root)
		self.frame_1.pack()
		self.aaa = PhotoImage(file="a.png")
		self.browsebutton = Button(self.frame_1, image=self.aaa, command=self.browsefunc)
		self.browsebutton.grid(row=6, pady=10)
		self.fromm = self.create(self.frame, "From", 0, 0)
		self.to = self.create(self.frame, "To", 0, 1)
		self.pwd = self.create(self.frame, "Pwd", 0, 2)
		self.check = ttk.Checkbutton(self.frame, text="Remember Me",
		                             command=lambda: self.add(self.fromm.get(), self.pwd.get()))
		self.check.grid(column=3, row=2)
		self.sub = self.create(self.frame, "Sub:", 0, 3)
		self.body = self.create(self.frame, "Body", 0, 4)
		self.attach = ""
		self.frame_2 = Frame(self.root)
		self.frame_2.pack()
		self.a = PhotoImage(file="send.png")
		self.send_b = Button(self.frame_2, image=self.a,
		                     command=lambda: self.send(self.fromm.get(), self.to.get(), self.pwd.get(),
		                                               self.sub.get(), self.body.get(), self.attach))
		self.send_b.grid(row=6, pady=10)
		self.root.mainloop()
	
	def add(self, mail, pwd):
		print(self.check.state())
		if "selected" in self.check.state():
			if mail != "" and pwd != "":
				self.conn_1.execute('''
					Select * from from_Mail where mail =  ?
					''', (mail,))
				# noinspection PyAttributeOutsideInit
				self.maill = self.conn_1.fetchall()
				print(self.maill)
				if self.maill:
					if self.maill[0][1] != pwd and messagebox.askyesno("Update", "Do You Want To Update The Password?"):
						self.conn_1.execute('''
							Update from_Mail Set pwd = ? where mail = ?
							''', (pwd, mail))
					else:
						return None
				else:
					self.conn_1.execute('''
						INSERT INTO from_Mail(mail,pwd) VALUES(?,?)
						''', (mail, pwd))
				self.conn.commit()
			else:
				messagebox.showerror("Warning", "Enter Username And Password")
				self.check.state(['!selected'])
		else:
			self.conn.rollback()
	
	# noinspection PyMethodMayBeStatic
	def create(self, frame, text, c, r):
		Label(frame, text=text, pady=20).grid(column=c, row=r)
		small_font = ('Cambria', 10)
		from_e = Entry(frame, font=small_font, width=25)
		if text == "Pwd":
			from_e = Entry(frame, font=small_font, show="*", width=25)
		if text == "Body":
			from_e = Entry(frame, width=25)
			from_e.grid(column=c + 1, row=r, padx=20, ipady=25, ipadx=23)
		else:
			from_e.grid(column=c + 1, row=r, padx=20)
		return from_e
	
	def browsefunc(self):
		# noinspection PyAttributeOutsideInit
		self.attach = filedialog.askopenfilename()
		if len(list(self.attach)) != 0:
			self.browsebutton['image'] = ""
		else:
			self.browsebutton['image'] = self.aaa
		t = "..." if len(list(self.attach.split("/")[-1])) > 10 else ""
		self.browsebutton['text'] = "".join(list(self.attach.split("/")[-1])[0:10]) + t
	
	# noinspection PyMethodMayBeStatic,PyUnusedFunction,PyAttributeOutsideInit
	
	def send(self, fromm, to, pwd, sub, body, attachh):
		try:
			# adding to mail to db
			self.con_2.execute('''
			INSERT INTO to_Mail(mail) VALUES(?)
			''', (to,))
			self.con.commit()
			# instance of MIMEMultipart
			self.data = MIMEMultipart()
			# storing the senders email address
			self.data['From'] = fromm
			# storing the receivers email address
			self.data['To'] = to
			# storing the subject
			self.data['Subject'] = sub
			# attach the body with the msg instance
			self.data.attach(MIMEText(body, 'plain'))
			# open the file to be sent
			try:
				while 1:
					self.filename = attachh.split("/")[-1]
					self.size = os.stat(attachh).st_size / (1024 * 1024)
					if self.size <= 25:
						self.attachment = open(attachh, "rb")
						# instance of MIMEBase and named as p
						self.p = MIMEBase('application', 'octet-stream')
						# To change the payload into encoded form
						self.p.set_payload(self.attachment.read())
						# encode into base64
						encoders.encode_base64(self.p)
						self.p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
						# attach the instance 'p' to instance 'msg'
						self.data.attach(self.p)
						break
					else:
						if messagebox.askokcancel("Warning", "Please Chose a file which is less than 25 mb"):
							self.browsebutton.invoke()
						else:
							break
			except FileNotFoundError:
				pass
			# creates SMTP session
			self.s = smtplib.SMTP('smtp.gmail.com', 587)
			# start TLS for security
			self.s.starttls()
			# Authentication
			self.s.login(fromm, pwd)
			# Converts the Multipart msg into a string
			self.text = self.data.as_string()
			# sending the mail
			self.s.sendmail(fromm, to, self.text)
			# terminating the session
			self.s.quit()
			messagebox.showinfo("Success", "Mail Sent")
		except TypeError:
			messagebox.showerror("Warning", "Please Enter The Details")
		except smtplib.SMTPAuthenticationError:
			messagebox.showerror("Warning", "Please Check Your Username/Password")
		except smtplib.SMTPRecipientsRefused:
			messagebox.showerror("Warning", "Please Check The To Address")
			self.con.rollback()
		except socket.gaierror:
			messagebox.showerror("Warning", "Please Connect to Internet")


gmail()
