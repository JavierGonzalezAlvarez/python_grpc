# grpc & microservices

## create virtual environment
$ virtualenv virtualServer -p python3.10
$ source virtualServer/bin/activate

$ pip install -r requirements.txt 

## create grpc code
path: /server/
$ python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/data.proto

## create DB
CREATE DATABASE grpc_python WITH OWNER test;
2525_ap

## create and insert data
.sql

## format memory response
clientele {
  id: 2
  name: "john"
}


