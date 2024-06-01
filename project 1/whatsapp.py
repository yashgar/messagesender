from flask import Flask, request, render_template
import pywhatkit as kit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('whatsapp.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    phone = request.form['phone']
    message = request.form['message']
    kit.sendwhatmsg_instantly(phone, message)
    return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)