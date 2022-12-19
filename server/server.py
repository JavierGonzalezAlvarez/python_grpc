# server/server.py
from concurrent import futures
import psycopg2

import grpc

from data_pb2 import (
    Client,
    Address,
    GetClient,
    GetClientResponse,
)

import data_pb2_grpc

#clientes = [ 
#        GetClient(id=1, name="sara"), 
#        GetClient(id=2, name="john"),  
#        GetClient(id=3, name="12john"),      
#]

def get_userId(id):
    connection = psycopg2.connect(host="localhost", dbname="grpc_python", user="test", password="2525_ap")
    result = connection.cursor()
    result.execute("SELECT user_id, name FROM client where user_id = '%s'",  (id,))
    res = result.fetchall()
    if res == None:
        print("no records")
    return res

class getService(data_pb2_grpc.getClientServicer):

    def Clients(self, request, context):
        #print("request: ", request)
        print("request user: ", request.user_id)
        res = get_userId(request.user_id)
        print("getting request...: ", res[0][0])
        keys = ["id", "name"]
        data= dict(zip(keys, res[0]))

        if res == None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Record not found")

        return GetClientResponse(clientele=data)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_getClientServicer_to_server(
        getService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server listening ...")
    server.wait_for_termination()

if __name__ == "__main__":
    server()