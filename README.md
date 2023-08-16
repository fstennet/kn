# KN

![Python](https://img.shields.io/badge/python-3.11-green.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.3.29-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.0.218-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [KN](#kn)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [TODOS](#todos)
  - [License](#license)

## Description

A small Python project that leverages OpenAI's API, LangChain, and a ChromaDB to provide answers to questions using your business logic (aka your documents).

## Requirements

- Python 3.11
- [List other dependencies here, like OpenAI's API, langchain, etc.]

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fstennet/kn.git
   ```
2. Navigate to the project directory:
    ```bash
    cd kn
    ```
3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The Flask project includes an endpoint that receives questions and responds based on llm embedded data and OpenAI's gpt3.5. The endpoint can be accessed via:

http://127.0.0.1:5000/api/ask (when running locally)

[Include more information about the endpoint and its usage]

## TODOS

- [ ] Replace sys arg with env config values
- [ ] Replace separate DBs with collections
- [ ] Add prompt
- [ ] Add memory (chat). ConversationBufferMemory
- [ ] Add compression

## License

