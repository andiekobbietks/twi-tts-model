# FILE: /twi-tts-model/twi-tts-model/scripts/select_model.py

import os
import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_pretrained_models(model_dir):
    models = {}
    for model_name in os.listdir(model_dir):
        model_path = os.path.join(model_dir, model_name)
        if os.path.isdir(model_path):
            models[model_name] = {
                'model': AutoModelForCausalLM.from_pretrained(model_path),
                'tokenizer': AutoTokenizer.from_pretrained(model_path)
            }
    return models

def select_best_model(models, evaluation_metric):
    best_model = None
    best_score = float('-inf')
    
    for model_name, model_info in models.items():
        score = evaluate_model(model_info['model'], evaluation_metric)
        if score > best_score:
            best_score = score
            best_model = model_name
            
    return best_model

def evaluate_model(model, metric):
    # Placeholder for model evaluation logic
    # This should return a score based on the evaluation metric
    return torch.rand(1).item()  # Random score for demonstration

if __name__ == "__main__":
    model_dir = '../models/pretrained'
    evaluation_metric = 'accuracy'  # Example metric
    models = load_pretrained_models(model_dir)
    best_model = select_best_model(models, evaluation_metric)
    print(f"The best model is: {best_model}")