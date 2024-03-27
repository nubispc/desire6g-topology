# desire6g-topology

This server provides a simple API for storing and retrieving information about network nodes, including CPU, memory, and storage resources, using a site ID as a unique identifier.

## Setup

Ensure you have Python 3.x and pip installed. Install the required dependencies:

```bash
pip install fastapi uvicorn
```

## Running the Server

Start the server with the following command:

```bash
uvicorn topology_server:app --reload
```

The server will be available at `http://localhost:8000`.

## API Endpoints
- `POST /nodes/`: Add a new node to the database. The request body should contain the site ID, CPU, memory, and storage information in JSON format.
- `GET /nodes/{site_id}`: Retrieve information about a node using its site ID.

## Examples

### Adding a Node

Use the following curl command to add a new node:

```bash
curl -X 'POST' \
  'http://localhost:8000/nodes/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "site_id": "SITEID1",
  "cpu": 8,
  "mem": 32,
  "storage": 1024
}'
```

### Retrieving a Node

Use the following curl command to retrieve information about a node:

```bash
curl -X 'GET' \
  'http://localhost:8000/nodes/SITEID' \
  -H 'accept: application/json'
```

### Adding a Link

To add a network link with its latency, you would send a POST request to `/links/` with a JSON body specifying the source site, destination site, and latency:

```bash
curl -X 'POST' \
  'http://localhost:8000/links/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "source": "SITEID1",
  "destination": "SITEID2",
  "latency_ms": 12.5
}'
```

### Retrieving All Links

To retrieve all network links with their latency values, you can send a GET request to `/links/`:

```bash
curl -X 'GET' \
  'http://localhost:8000/links/' \
  -H 'accept: application/json'
```

