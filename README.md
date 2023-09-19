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
- [License](#license)

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
   git clone https://github.com/nky001/wsgi
