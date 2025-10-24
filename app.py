from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "برنامه Flask من با موفقیت در لیارا اجرا شد!"

if __name__ == '__main__':
    app.run()
