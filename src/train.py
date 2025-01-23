import torch
from torch.utils.data import DataLoader
from torch.optim import Adam
from tqdm import tqdm
from model import TwiTTSModel
from preprocessing import TwiTextPreprocessor

def train(config):
    model = TwiTTSModel(config)
    preprocessor = TwiTextPreprocessor()
    optimizer = Adam(model.parameters(), lr=config['learning_rate'])
    
    # Training loop
    for epoch in range(config['epochs']):
        model.train()
        for batch in tqdm(train_dataloader):
            text, audio = batch
            
            # Preprocess text
            text = preprocessor.preprocess(text)
            
            # Forward pass
            mel_output = model(text)
            
            # Calculate loss
            loss = torch.nn.functional.mse_loss(mel_output, audio)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

if __name__ == "__main__":
    config = {
        'encoder_dim': 512,
        'decoder_dim': 1024,
        'encoder_layers': 3,
        'mel_bins': 80,
        'learning_rate': 1e-4,
        'epochs': 10  # Reduced the number of epochs to fit within the available compute time
    }
    
    train(config)
