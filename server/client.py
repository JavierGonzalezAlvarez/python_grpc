import grpc
from data_pb2_grpc import getClientStub
from data_pb2 import Client, Address, GetClientRequest
import traceback
import sys

def client():
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = getClientStub(channel)
        request = GetClientRequest(user_id=1)
        response = stub.Clients(request)
        print("response: ", response)
        print("id: ", response.clientele.id)
        print("name: ", response.clientele.name)
    except Exception as e:
        print("No records") 
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_traceback))

if __name__ == "__main__":
    client()