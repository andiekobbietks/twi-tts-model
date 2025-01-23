import torch
import torch.nn as nn
import torch.optim as optim

class TTSModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(TTSModel, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out)
        return output

    def train_model(self, train_loader, num_epochs, learning_rate):
        criterion = nn.MSELoss()
        optimizer = optim.Adam(self.parameters(), lr=learning_rate)

        self.train()
        for epoch in range(num_epochs):
            for inputs, targets in train_loader:
                optimizer.zero_grad()
                outputs = self(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
            print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

    def generate_speech(self, input_text, tokenizer, max_length):
        self.eval()
        with torch.no_grad():
            input_ids = tokenizer.encode(input_text, return_tensors='pt')
            outputs = self(input_ids)
            generated_ids = torch.argmax(outputs, dim=-1)
            generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return generated_text
