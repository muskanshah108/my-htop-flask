from flask import Flask
import os
import subprocess
import getpass
from datetime import datetime
import pytz  

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Muskan Shah"

    
    username = getpass.getuser()

    
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist)
    server_time_ist = now_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error running top command: {e}"

    # Build an HTML response
    return f"""
    <html>
        <head>
            <title>/htop Output</title>
        </head>
        <body>
            <h1>Name: {full_name}</h1>
            <h2>Username: {username}</h2>
            <h3>Server Time (IST): {server_time_ist}</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
