# Twi Text-to-Speech (TTS) Model using AfroLM

## Overview
This project aims to develop a Twi text-to-speech (TTS) model by utilizing AfroLM, a multilingual pre-trained language model tailored for African languages. The model will be fine-tuned with a pre-trained TTS model to enhance its performance in generating natural-sounding speech in Twi.

## Project Structure
The project is organized into the following directories and files:

- **data/**
  - **raw/**: Contains the raw text data used for training the TTS model.
  - **processed/**: Holds the processed text data after pre-processing steps have been applied.

- **models/**
  - **pretrained/**: Stores the pre-trained TTS models selected for fine-tuning.
  - **fine_tuned/**: Contains the fine-tuned TTS models after training with Twi data.

- **notebooks/**
  - **data_preprocessing.ipynb**: Documents the data pre-processing steps, including text normalization and diacritic restoration.
  - **model_selection.ipynb**: Outlines the model selection process, comparing different pre-trained TTS models.
  - **fine_tuning.ipynb**: Details the fine-tuning process of the selected TTS model using AfroLM embeddings.

- **scripts/**
  - **preprocess_text.py**: Implements the text pre-processing functions, including normalization and token conversion.
  - **select_model.py**: Handles the logic for selecting the appropriate pre-trained TTS model.
  - **fine_tune_model.py**: Contains the code for fine-tuning the selected TTS model with the processed Twi data.

- **src/**
  - **__init__.py**: Marks the directory as a Python package.
  - **data_preprocessing.py**: Defines functions and classes related to data pre-processing tasks.
  - **model_selection.py**: Defines functions and classes for model selection and evaluation.
  - **fine_tuning.py**: Defines functions and classes for the fine-tuning process of the TTS model.

- **requirements.txt**: Lists the dependencies required for the project, including libraries for TTS, data processing, and machine learning.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines
- Use the Jupyter notebooks in the `notebooks/` directory to explore data pre-processing, model selection, and fine-tuning processes.
- Run the scripts in the `scripts/` directory for automated tasks related to text pre-processing, model selection, and fine-tuning.
- Modify the source code in the `src/` directory as needed to customize the TTS model development process.

## Contribution
Contributions to improve the model and its performance are welcome. Please submit a pull request or open an issue for discussion.