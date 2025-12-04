import socket
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
  return jsonify({
    'time': datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
    'hostname': socket.gethostname(),
    'message': 'You are doing great, human!! :)'
  }), 200

@app.route('/api/v1/health')
def health():
  return jsonify({ 'status': 'up' }), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0')
