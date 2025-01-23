from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer
from src.models.tts_model import TTSModel

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model = TTSModel(input_dim=768, hidden_dim=512, output_dim=768)
model.load_state_dict(torch.load('path_to_fine_tuned_model.pth'))
tokenizer = AutoTokenizer.from_pretrained("afro-lm")

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    with torch.no_grad():
        input_ids = tokenizer.encode(text, return_tensors='pt')
        outputs = model(input_ids)
        generated_ids = torch.argmax(outputs, dim=-1)
        generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    
    return jsonify({'audio': generated_text})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get('text')
    # Implement text-to-speech generation logic
    return jsonify({"speech": "Generated speech for the given text"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
