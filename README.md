# Root Hair Counting and Image Super-Resolution

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

This repository contains the code and resources for the paper: **A Novel Approach for Plant Root-Hair Counting and Its Improvement via Image Super-Resolution**.

**[Link to the Published Paper (Will be added upon full publication)]**

## Overview

This project presents a novel image analysis pipeline for accurately counting plant root hairs. The core of the pipeline is implemented in the `root_hair_counting.py` script. The paper explores the effectiveness of this approach and demonstrates its improvement when combined with image super-resolution techniques.

This repository also includes supporting scripts for various image processing tasks used in the research. The `main.py` script provides a structured way to execute the different stages of the analysis.

## Repository Contents

* `root_hair_counting.py`: The main script implementing the root hair counting algorithm.
* `adaptive_thresholding.py`: Script for performing adaptive thresholding on images.
* `canny_edge detection.py`: Script for detecting edges in images using the Canny algorithm.
* `get_HSL_from_image.py`: Script to extract HSL (Hue, Saturation, Lightness) color information from images.
* `th_algorithm_selection.py`: Script potentially used for selecting or comparing different thresholding algorithms.
* `main.py`: A script to orchestrate the execution of the different analysis steps.
* `README.md`: This file, providing an overview of the repository.
* `https://www.google.com/search?q=LICENSE`: The license under which this code is distributed (e.g., MIT License). You should add a license file to your repository.
* `data/` (Optional): A directory to store example images or datasets (you might want to include a `.gitignore` file to avoid committing large datasets directly).
* `results/` (Optional): A directory where output images or counting results can be saved.
* `requirements.txt`: A list of Python packages required to run the code.

## Setup

### Prerequisites

* Python 3.x
* Required Python packages (see `requirements.txt`). You can install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

    *(You'll need to create this file listing dependencies like OpenCV, NumPy, etc.)*

### Installation

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd [repository name]
    ```

2.  (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The `main.py` script provides a central point for running the analysis. You can execute it with different options depending on the task you want to perform.

```bash
python main.py --help