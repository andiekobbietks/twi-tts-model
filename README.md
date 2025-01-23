# Twi Text-to-Speech (TTS) Model using AfroLM

## Overview
This project aims to create a Twi text-to-speech (TTS) model by leveraging AfroLM, a multilingual pre-trained language model for African languages, and fine-tuning it with a pre-trained TTS model.

## Directory Structure
- `data/`: Contains raw and processed data.
- `models/`: Contains pre-trained and fine-tuned models.
- `notebooks/`: Jupyter notebooks for data preprocessing, model selection, and fine-tuning.
- `scripts/`: Python scripts for preprocessing text, selecting models, and fine-tuning.
- `src/`: Source code for data preprocessing, model selection, and fine-tuning.
- `tests/`: Unit tests for the project.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Steps to Create Twi TTS Model
1. Text Pre-processing
2. Model Selection
3. Fine-Tuning with AfroLM
4. Deployment

## Key Advantages of Using AfroLM
- Strong Twi understanding.

## Recommendations
1. Set CSV file encoding to UTF-8
2. Update database connection strings to use UTF-8
3. Implement proper character encoding in shipping label generation
4. Add encoding validation for data input forms

## Next Steps
1. Complete the Jupyter notebooks in the `notebooks/` directory:
   - Implement the `preprocess_text` function in `data_preprocessing.ipynb` to normalize text, convert numbers, and restore diacritics.
   - Implement the `fine_tune_tts_model` function in `fine_tuning.ipynb` to load data, initialize the model, and fine-tune it.
   - Implement the `evaluate_model` function in `model_selection.ipynb` to load models, evaluate them, and select the best one.

2. Integrate the scripts in the `scripts/` directory:
   - Complete the `preprocess_text.py` script to normalize text, convert numbers, and restore diacritics.
   - Complete the `fine_tune_model.py` script to load data, initialize the model, and fine-tune it.
   - Complete the `select_model.py` script to load models, evaluate them, and select the best one.

3. Implement the functions in the `src/` directory:
   - Implement the `preprocess_text` function in `data_preprocessing.py` to normalize text, convert numbers, and restore diacritics.
   - Implement the `fine_tune_model` function in `fine_tuning.py` to load data, initialize the model, and fine-tune it.
   - Implement the `evaluate_model` function in `model_selection.py` to load models, evaluate them, and select the best one.

## Compute and Data Requirements for Training the Model
Training a complex TTS model requires significant compute and data resources. Here are the key requirements:

### Compute Requirements
- **GPU**: A powerful GPU is essential for training deep learning models efficiently. Recommended GPUs include NVIDIA Tesla V100, A100, or similar.
- **Compute Time**: Training a TTS model can take several days to weeks, depending on the complexity of the model and the size of the dataset.

### Data Requirements
- **Volume of Data**: A large volume of high-quality text and audio data is crucial for training a robust TTS model. The dataset should cover a wide range of phonetic and linguistic variations in the Twi language.
- **Data Preprocessing**: Proper preprocessing of text and audio data is essential to ensure the quality and consistency of the training data.

## Limitations of Current Compute and Data Resources
Despite the comprehensive process outlined in this project, there are limitations to the current compute and data resources available:

### Compute Limitations
- **Limited Compute Credits**: The `cost_calculator.py` indicates a credit of $300, which translates to approximately 179.52 hours or 7.48 days of compute time. This may not be sufficient for training a complex TTS model.
- **Resource-Intensive Dependencies**: The `requirements.txt` lists dependencies like `torch`, `transformers`, and `tensorboard`, which are resource-intensive and may require more compute power than available.

### Data Limitations
- **Insufficient Data Volume**: The `README.md` outlines a comprehensive process for data preprocessing, model selection, and fine-tuning, but does not provide details on the volume of data available, which is crucial for training a robust model.
