# Oasis - A Real Estate Price Prediction

<p align="center">
  <img src="./docs/images/oasis_logo.png" alt="Oasis logo"/>
</p>

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Hugging Face Spaces](https://img.shields.io/badge/HuggingFace-Spaces-blue)](https://huggingface.co/spaces/oasisorg/oasis-web)

## Project Overview

This project aims to predict real estate prices, primarily focusing on the impact of **climatic events**. Our goal is to identify **safe and profitable locations** by analyzing how various weather and climate patterns influence property values. As the project evolves, we plan to incorporate other significant events that might affect real estate prices.

## Table of Contents

  * [Project Overview](#project-overview)
  * [Folder Structure](#folder-structure)
  * [Setup and Installation](#setup-and-installation)
  * [Usage](#usage)
  * [Contributing](#contributing)
  * [License](#license)

## Folder Structure

This project follows a structured approach to machine learning development. Here's an overview of the directories:

  * `data/`: Stores all **raw and processed data**. This includes historical real estate data, climate event data, and any derived features used for training.
  * `mlflow/`: Dedicated to **MLflow server configuration**. This directory will contain files necessary for setting up and deploying an MLflow tracking server (e.g., Dockerfiles, server-specific `requirements.txt`).
  * `models/`: Holds the **python files** related to the training of the ML models.
  * `notebooks/`: Contains **Jupyter notebooks** for exploratory data analysis (EDA), model experimentation, training, and result visualization.
  * `README.md`: This file, providing an overview and instructions for the project.
  * `web/`: Houses the code for the **web application** (frontend) that interacts with the prediction API to display results or allow user input.

## Requirements

This project requires:
  * [Python 3.13](https://www.python.org/)

## Setup and Installation

To get this project up and running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone --recurse-submodules https://github.com/nclsprsnw/oasis.git
    cd oasis
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv oasis
    source oasis/bin/activate  # On Windows: `oasis\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt # (You'll need to create this file with your project dependencies)
    ```
4.  **Set up environment variables:**
    Create a `.env` file in the root directory by copying the `.env.sample` file and filling the missing values.

## Project dependencies

This project uses several others git repositories as submodules.

  - `web`: this directory contains [the web application](https://huggingface.co/spaces/oasisorg/oasis-web) code hosted on Hugging Face Spaces, which is used to interact with the API.
  - `mlflow`: this directory contains [the MLflow server](https://huggingface.co/spaces/oasisorg/oasis-mlflow) configuration files hosted on Hugging Face Spaces, which are used to track experiments and manage models.

## Usage

### Data Preparation

  * Place your raw data files in the `data/` directory.
  * Refer to notebooks in `notebooks/` for data cleaning, preprocessing, and feature engineering steps.

### Model Training & Experimentation

  * Explore and run the Jupyter notebooks in `notebooks/` to understand the model development process.
  * MLflow tracking will automatically log parameters, metrics, and models to the configured MLflow server).

### Running the Web Application

  * Navigate to the `web/` directory.
  * Instructions for setting up and running the web frontend will be provided there.

## Contributing

We welcome contributions to this project\! Please see our `CONTRIBUTING.md` (if you plan to create one) for guidelines on how to contribute.

