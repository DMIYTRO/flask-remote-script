from flask import Flask, render_template, request
from flask_socketio import SocketIO
import subprocess
import sys
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, 
                   async_mode='threading',
                   cors_allowed_origins="*",
                   logger=True,
                   engineio_logger=True)

def read_output(pipe, socket_event):
    try:
        while True:
            line = pipe.readline()
            if not line:
                break
            decoded_line = line.decode('utf-8', errors='replace').rstrip()
            socketio.emit(socket_event, {'data': decoded_line})
    except Exception as e:
        socketio.emit('error', {'data': f'Error reading output: {str(e)}'})
    finally:
        pipe.close()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('status', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_process')
def handle_start_process():
    try:
        process = subprocess.Popen(['python', 'script.py'],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 bufsize=1,
                                 universal_newlines=False)
        
        stdout_thread = threading.Thread(target=read_output, args=(process.stdout, 'output'))
        stderr_thread = threading.Thread(target=read_output, args=(process.stderr, 'error'))
        
        stdout_thread.start()
        stderr_thread.start()
        
        return_code = process.wait()
        
        stdout_thread.join()
        stderr_thread.join()
        
        if return_code == 0:
            socketio.emit('output', {'data': 'Process completed successfully!'})
        else:
            socketio.emit('error', {'data': f'Process failed with return code {return_code}'})
            
    except Exception as e:
        socketio.emit('error', {'data': f'Failed to start process: {str(e)}'})
    finally:
        socketio.emit('process_finished')

if __name__ == '__main__':
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
        
    socketio.run(app, 
                debug=True, 
                host='127.0.0.1',
                port=5000,
                allow_unsafe_werkzeug=True) 