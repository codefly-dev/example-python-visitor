import time
import subprocess
from concurrent import futures
import grpc
from google.protobuf.empty_pb2 import Empty
import python.cli.v0.cli_grpc as cli

class Launcher:
    def __init__(self):
        self.cmd = None
        self.cli = None

    @staticmethod
    def launch_up_to():
        cmd = subprocess.Popen(["codefly", "run", "service", "--exclude-root", "--server"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        port = 10000
        wait = 5
        while True:
            time.sleep(1)
            try:
                with grpc.insecure_channel(f'localhost:{port}') as channel:
                    cli = cli.CLIClient(channel)
                    cli.Ping(Empty())
                    break
            except Exception as e:
                wait -= 0.5
                if wait <= 0:
                    raise Exception("timeout waiting for connection") from e
            time.sleep(0.5)
        return Launcher(cmd, cli)

    def wait_for_ready(self):
        wait = 5
        while True:
            time.sleep(1)
            try:
                status = self.cli.GetFlowStatus(Empty())
                if status.ready:
                    break
            except Exception as e:
                wait -= 0.5
                if wait <= 0:
                    raise Exception("timeout waiting for flow to be ready") from e
            time.sleep(0.5)

    def close(self):
        self.cli.StopFlow(Empty())
