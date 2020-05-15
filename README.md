# Postboy

This is a small utility meant to suit some of my personal needs

## Getting Started

```
$> ./src/postboy.py --path=<URL_PATH> <FILE>
```

- URL_PATH: path that will be used in every http calls
- FILE: file containing all needed hostnames

### Prerequisites

- python >= 3.5

### Example

with a file named `ips` containing the following:

```
127.0.0.1:8080
127.0.0.1:8081
127.0.0.1:8082
127.0.0.1:8083
127.0.0.1:8084
```

this command:

```
$> ./src/postboy.py --path=/api/v1/status ips
```

should output something similar to:

```
calling: http://127.0.0.1:8080/api/v1/status
{
    "status": "up",
    "version": "1.0.0"
}

calling ...
```
