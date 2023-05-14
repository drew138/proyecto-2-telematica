from instance.src.services.monitor_service import MonitorServiceServicer
from instance.src.monitor.monitor import Monitor
from instance.src.server.server import Server
import threading
from flask import Flask, request, jsonify, Response

app: Flask = Flask(__name__)


@app.route('/set-metric', methods=['POST'])
def create() -> Response:
    data = request.get_json()
    metric = data['metric']
    Monitor.set_metric(metric)
    response = {'message': 'Metric set successfully'}
    return jsonify(response)


def main():
    monitor_service = MonitorServiceServicer()
    api_port = 8080
    kwargs = {"host": "0.0.0.0", "port": api_port, "debug": True}
    threading.Thread(target=app.run, kwargs=kwargs).start()
    grpc_port = 8090
    server = Server(monitor_service, grpc_port)
    server.start()


if __name__ == "__main__":
    main()
