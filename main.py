from flask import Flask, render_template, request
import Caesar
from random import randint
from my_weather import weather, currcity


web = Flask(__name__)

@web.route('/')
def caesar():
	return render_template('entry.html', weather = "Сейчас в " + str(currcity) + " " + "0"+'°C' + ', ')

@web.route('/register')
def caesar_register():
	return render_template('register.html')

@web.route('/ID-getting', methods=['POST'])
def get_for_id():
	id = str(randint(100000, 999999))
	password = request.form['password']
	with open('ids-passwords.txt', 'r') as login:
		for line in login:
			print(line)
			while id in line:
				id = str(randint(100000, 999999))
				
	with open('ids-passwords.txt', 'a') as login:
		print(id, password, file = login)
	return render_template('id-get.html', id=id)
	
@web.route('/result', methods=['POST'])
def results():
	word = request.form['word']
	sdvig = request.form['sdvig']
	sdvig = int(sdvig)
	result = str(Caesar.caesar(word, sdvig))
	id = request.form['C-ID']
	password = request.form['password']
	with open('ids-passwords.txt', 'r') as login:
		for line in login:
			line = line[:len(line)-1]
			if id + ' ' + password == line:
				with open('logs/'+id+'.log', 'a') as id_log:
					print(result, sdvig, file = id_log)
					return render_template("result.html",
							word=word,
							sdvig=sdvig,
							result=result
							)
		return render_template("error.html", error = "Такой связки [C-ID - password] не существует.")
		
@web.route('/viewlog-login')
def view_log_login():
	return render_template('login.html')

@web.route('/viewlog', methods = ['POST'])
def view_the_log():
	id = request.form['C-ID']
	password = request.form['password']
	with open('ids-passwords.txt', 'r') as login:
		for line in login:
			line = line[:len(line)-1]
			if id + ' ' + password == line:
				try:
					with open('logs/'+id+'.log') as id_log:
						beatview = id_log.read()
						return render_template('view-log.html', log = beatview, CID = id)
				except FileNotFoundError:
					return render_template("error.html", error = "Этот пользователь еще не создал лог.")
	return render_template("error.html", error = "Такой связки [C-ID - password] не существует.")


if __name__ == '__main__':
	web.run(debug=True)