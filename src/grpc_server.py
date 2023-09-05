import grpc
from concurrent import futures
import authservice_pb2
import authservice_pb2_grpc

class MyService(authservice_pb2_grpc.MyServiceServicer):
    def GetHelloMessage(self, request, context):
        return authservice_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    authservice_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
