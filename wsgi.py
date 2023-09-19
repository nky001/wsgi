import socket
import io
import sys
import os
import signal
import concurrent.futures
import time

class WSGIServer:
    def __init__(self, host, port, max_workers=4):
        self.host = host
        self.port = port
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers)
        self.worker_kill_interval = 60  # Kill idle workers after 60 seconds of inactivity
        self.last_worker_kill_time = time.time()
        self.worker_counter = 0  # Unique worker counter
        self.worker_activity = {}  # Store worker activity timestamps

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

        # Register a signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.shutdown)

    def start(self):
        print(f"WSGI server listening on {self.host}:{self.port}")
        while True:
            client_sock, client_addr = self.sock.accept()
            self.worker_counter += 1
            worker_number = self.worker_counter
            self.worker_activity[worker_number] = time.time()  # Record worker start time
            self.executor.submit(self.handle_request, client_sock, worker_number)

            # Check if it's time to kill idle workers
            if time.time() - self.last_worker_kill_time > self.worker_kill_interval:
                self.last_worker_kill_time = time.time()
                self.kill_idle_workers()

    def handle_request(self, client_sock, worker_number):
        client_data = client_sock.recv(1024)
        environ = self.parse_request(client_data.decode('utf-8'))
        response = self.application(environ, self.start_response)
        self.send_response(client_sock, response)
        client_sock.close()
        self.worker_activity[worker_number] = time.time()

    def parse_request(self, request_data):
        # Parse the HTTP request data and create an environment dictionary
        # You can implement a more robust request parser as needed.
        request_lines = request_data.strip().split('\n')
        method, path, _ = request_lines[0].split(' ')
        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            # Add other necessary environment variables here
        }
        return environ

    def start_response(self, status, headers):
        self.status = status
        self.headers = headers

    def send_response(self, client_sock, response):
        # Send the HTTP response to the client
        client_sock.sendall(f"HTTP/1.1 {self.status}\r\n".encode('utf-8'))
        for header in self.headers:
            client_sock.sendall(f"{header[0]}: {header[1]}\r\n".encode('utf-8'))
        client_sock.sendall(b'\r\n')  # End of headers
        for data in response:
            client_sock.sendall(data)

    def application(self, environ, start_response):
        # Your WSGI application logic goes here
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Hello, World!']

    def shutdown(self, signum, frame):
        print("Shutting down the server...")
        self.executor.shutdown(wait=False)
        self.sock.close()
        sys.exit(0)

    def kill_idle_workers(self):
        """
        Kills idle worker threads that are not actively processing requests.
        """
        current_time = time.time()
        workers_to_kill = []
        for worker_number, activity_time in self.worker_activity.items():
            if current_time - activity_time > self.worker_kill_interval:
                workers_to_kill.append(worker_number)
        for worker_number in workers_to_kill:
            del self.worker_activity[worker_number]
        print(f"Total workers killed due to inactivity: {len(workers_to_kill)}")

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    max_workers = 4
    server = WSGIServer(host, port, max_workers)
    server.start()
