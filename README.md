# WSGI Server

This is a basic implementation of a WSGI (Web Server Gateway Interface) server in Python. The server listens on a specified host and port, accepts incoming HTTP requests, and routes them to a simple "Hello, World!" WSGI application. It also includes functionality for graceful shutdown and killing idle worker threads.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)


## Features

- Basic WSGI server template.
- Graceful server shutdown with signal handling (SIGINT).
- Automatic killing of idle worker threads.
- Simple "Hello, World!" WSGI application included.

## Getting Started

### Prerequisites

- Python 3.x

### Installation
1. Clone the repository:

  ```shell
   git clone https://github.com/nky001/wsgi.git
  ```
2. Change to the project directory:
  ```shell
    cd wsgi
  ```
3. (Optional) Create and activate a virtual environment:

  ```shell
    python -m venv venv
    source venv/bin/activate
  ```
4. Install the required dependencies:
  ```shell
    pip install -r requirements.txt
  ```

## Usage
To start the WSGI server, run the following command:

```shell
  python wsgi.py
```
The server will start listening on the specified host and port. You can access it in a web browser or using HTTP client tools.

## Customization
The provided WSGI application is a simple "Hello, World!" example. You can customize the application method in wsgi.py to implement your own WSGI application logic.

Additionally, you can modify other parts of the code to fit your specific requirements.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

  Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your branch to your fork.
- Create a pull request to the main repository's main branch.

