
Wikipedia Content-Based Question Answering System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [License](#license)

## Introduction

This project aims to create a content-based question-answering system that leverages information from Wikipedia to provide accurate and relevant answers to user queries. The system is designed to be versatile, capable of handling a wide range of topics by loading relevant documents, splitting the text into manageable chunks, and utilizing a language model for generating responses.

## Features

- **Document Loading**: Fetches relevant documents from Wikipedia based on user queries.
- **Text Splitting**: Breaks down documents into smaller chunks for easier processing.
- **Vector Storage**: Uses embeddings to store and efficiently search through text chunks.
- **Language Model Integration**: Employs a language model for generating responses based on the context provided by similarity search.

## Getting Started

### Step 1: Download and Install Conda

1. Visit the [Anaconda website](https://www.anaconda.com/products/distribution) or the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) to download the installer appropriate for your operating system (Anaconda includes a full package manager and additional packages, while Miniconda includes only Conda and its dependencies).
2. Follow the installation instructions for your operating system.

### Step 2: Create a Virtual Environment

Once Conda is installed, you can create a virtual environment:
Open a terminal or command prompt and paste the following.

```bash
conda create --name myenv
```

### Step 3: Activate the Virtual Environment
After creating the virtual environment, activate it:

```bash
conda activate myenv
```

### Step 4: Install Packages
Once the virtual environment is activated, you can install packages into it using Conda:

```bash
conda install langchain==0.1.9
conda install langchain_openai==0.1.9
conda install langchain_community==0.0.24
conda install langchain_core==0.1.26
conda install chromadb==0.1.26
conda install bs4==0.0.2
conda install pydantic==2.6.2
```

FYI this was probably overkill but I wanted to make sure I included as much as I could to get it running

### Step 5: Enviorment Variables

```bash
conda env config vars set LANGCHAIN_TRACING_V2 = true
conda env config vars set LANGCHAIN_API_KEY =your_langchain_api_key_here
conda env config vars set OPENAI_API_KEY=your_openai_api_key_here
```

## Credits

https://docs.smith.langchain.com/
https://www.phind.com/
https://lilianweng.github.io/posts/2023-06-23-agent/

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details.

---
