# FILE: /twi-tts-model/twi-tts-model/scripts/fine_tune_model.py

import torch
from transformers import AfroLMTokenizer, AfroLMModel
from transformers import TTSModel, Trainer, TrainingArguments
from src.data_preprocessing import load_processed_data
from src.model_selection import select_pretrained_model

def fine_tune_tts_model():
    # Load processed Twi data
    train_data, eval_data = load_processed_data()

    # Load AfroLM tokenizer and model
    tokenizer = AfroLMTokenizer.from_pretrained('afro-lm')
    afro_lm_model = AfroLMModel.from_pretrained('afro-lm')

    # Select a pre-trained TTS model
    tts_model = select_pretrained_model()

    # Prepare training arguments
    training_args = TrainingArguments(
        output_dir='./models/fine_tuned',
        evaluation_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=tts_model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=eval_data,
    )

    # Fine-tune the model
    trainer.train()

if __name__ == "__main__":
    fine_tune_tts_model()