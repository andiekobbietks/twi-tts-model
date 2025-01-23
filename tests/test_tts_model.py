import unittest
import torch
from transformers import AutoTokenizer
from src.models.tts_model import TTSModel

class TestTTSModel(unittest.TestCase):
    def setUp(self):
        self.model = TTSModel(input_dim=768, hidden_dim=512, output_dim=768)
        self.tokenizer = AutoTokenizer.from_pretrained("afro-lm")

    def test_train(self):
        # Create dummy data for training
        train_loader = [(
            torch.randn(1, 10, 768),  # inputs
            torch.randn(1, 10, 768)   # targets
        )]
        num_epochs = 1
        learning_rate = 0.001

        # Train the model
        self.model.train_model(train_loader, num_epochs, learning_rate)

        # Check if the model parameters have been updated
        for param in self.model.parameters():
            self.assertTrue(param.grad is not None)

    def test_generate_speech(self):
        input_text = "Hello, how are you?"
        generated_speech = self.model.generate_speech(input_text, self.tokenizer, max_length=50)

        # Check if the generated speech is a non-empty string
        self.assertIsInstance(generated_speech, str)
        self.assertGreater(len(generated_speech), 0)

if __name__ == '__main__':
    unittest.main()
