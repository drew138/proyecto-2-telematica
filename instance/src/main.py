from instance.src.services.monitor_service import MonitorServiceServicer
from instance.src.monitor.monitor import Monitor
from instance.src.server.server import Server
import threading
from flask import Flask, request, jsonify, Response
from instance.src.client.client import Client
import os


def create_grpc_client():
    # Sacar ip del orchestrator
    orchestrator_ip = os.getenv('ORCHESTRATOR_IP')
    grpc_port = os.getenv('GRPC_PORT')
    socket = f'{orchestrator_ip}:{grpc_port}'
    # Conectar por grpc con esa ip
    return Client(socket)


grpc_client = create_grpc_client()

app: Flask = Flask(__name__)

@app.route('/set-metric', methods=['POST'])
def create() -> Response:
    data = request.get_json()
    metric = data['metric']
    Monitor.set_metric(metric)
    response = {'message': 'Metric set successfully'}
    return jsonify(response)

@app.route('/unregister', methods=['POST'])
def unregister() -> Response:
    self_id = os.getenv('SELF_ID')
    grpc_client.unregister(self_id)
    response = {'message': 'Instance unregistered succesfully'}
    return jsonify(response)


def main():
    # Mandar register
    self_id = os.getenv('SELF_ID')
    grpc_client.register(self_id)

    # Iniciar servicios
    monitor_service = MonitorServiceServicer()
    api_port = os.getenv('API_PORT')
    kwargs = {"host": "0.0.0.0", "port": api_port, "debug": True}
    threading.Thread(target=app.run, kwargs=kwargs).start()
    grpc_port = os.getenv('GRPC_PORT')
    server = Server(monitor_service, grpc_port)
    server.start()


if __name__ == "__main__":
    main()
