from flask import Flask, jsonify
import platform
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    hname = platform.node()
    ip = get_local_ip()

    data = {
        "hostname": hname,
        "local-ip": ip
    }
    return jsonify(data)

def get_local_ip():
    if platform.system() == "Windows":
        local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
    else:
        local = subprocess.getoutput("ifconfig | grep 'inet' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    return local

if __name__ == '__main__':
    app.run(debug=True, port=8080)