import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class TwiTTSModel(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.afrolm = AutoModel.from_pretrained("afrolm/afrolm-base")
        self.tokenizer = AutoTokenizer.from_pretrained("afrolm/afrolm-base")
        
        # TTS specific layers
        self.encoder = nn.LSTM(
            input_size=self.afrolm.config.hidden_size,
            hidden_size=config['encoder_dim'],
            num_layers=config['encoder_layers'],
            batch_first=True,
            bidirectional=True
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(config['encoder_dim'] * 2, config['decoder_dim']),
            nn.ReLU(),
            nn.Linear(config['decoder_dim'], config['mel_bins'])
        )

    def forward(self, text):
        # Get AfroLM embeddings
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        embeddings = self.afrolm(**inputs).last_hidden_state
        
        # Encode sequence
        encoder_output, _ = self.encoder(embeddings)
        
        # Generate mel-spectrograms
        mel_output = self.decoder(encoder_output)
        
        return mel_output

    def generate_speech(self, text):
        self.eval()
        with torch.no_grad():
            mel_specs = self.forward(text)
            # Convert mel spectrograms to audio (implement vocoder here)
            return mel_specs
