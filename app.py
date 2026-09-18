from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f'''
    <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1 style="color: #0096ff;">🐳 Docker + Flask Jonli Serverda!</h1>
        <p style="font-size: 18px;">Ushbu loyiha Docker konteyneri ichida muvaffaqiyatli ishga tushdi.</p>
        <p style="color: gray;">Konteyner ID (ID): {hostname}</p>
    </div>
    '''

if __name__ == '__main__':
    # 0.0.0.0 konteyner tashqarisidan ulanishlar qabul qilishi uchun shart!
    app.run(host='0.0.0.0', port=5000)
