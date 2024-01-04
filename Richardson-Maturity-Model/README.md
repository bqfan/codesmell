# Richardson Maturity Model

The Richardson Maturity Model, proposed by Leonard Richardson, is a model that defines different levels of maturity in designing and implementing RESTful APIs. It categorizes REST APIs into levels based on their adherence to REST principles and constraints.

The model consists of four levels, each representing a different degree of adherence to RESTful practices:

1. Level 0 - The Swamp of POX (Plain Old XML):
At this level, the API essentially uses HTTP as a transport mechanism without adhering to REST principles.
It often uses a single endpoint, typically a POST or GET request, to perform actions or retrieve data.
The API doesn’t make use of HTTP methods (GET, POST, PUT, DELETE) to manipulate resources, and the endpoints might not represent resources properly.

2. Level 1 - Resources:
Level 1 introduces the concept of resources and begins organizing API endpoints around resources.
Each resource is assigned a unique URI (Uniform Resource Identifier).
However, the HTTP methods are not yet used to their full extent, and the focus is on identifying resources rather than utilizing proper HTTP methods.

3. Level 2 - HTTP Verbs:
At this level, the API starts utilizing the HTTP methods (GET, POST, PUT, DELETE) properly.
Each method is used for its intended purpose: GET for retrieval, POST for creation, PUT for updating, DELETE for deletion.
Resources are better identified using URIs and manipulated using appropriate HTTP methods.

3. Level 3 - Hypermedia Controls (HATEOAS):
Level 3 represents the highest maturity level in RESTful APIs.
It emphasizes hypermedia as the engine of application state (HATEOAS), where responses include links to related resources.
Clients navigate through the API by following links embedded in the responses, reducing coupling between the client and server.
Adherence to higher levels of the Richardson Maturity Model generally leads to APIs that are more flexible, maintainable, and scalable. However, achieving higher levels of maturity often requires additional effort and careful design considerations, especially when implementing HATEOAS principles at Level 3.

# Code examples
Richardson Maturity Model code examples for level 0 (level-0.py) and level 2 (level-2.py) are written with fastapi framework for simplicity. You can run the examples as follow:

1. create python virtual environment and install python packages:
```
python3 -m venv venv 
source ./venv/bin/activate
pip install -r requirements.txt
```
2. start uvicorn:
```
uvicorn level-0:app --host 0.0.0.0 --port 8080 --reload
```
or
```
uvicorn level-2:app --host 0.0.0.0 --port 8080 --reload
```
3. access OpenAPI docs:
```
http://localhost:8080/docs
```