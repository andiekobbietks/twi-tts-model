import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqGeneration

class TwiTextPreprocessor:
    def __init__(self):
        self.diacritic_model = AutoModelForSeq2SeqGeneration.from_pretrained("t5-base")  # Replace with fine-tuned model path
        self.diacritic_tokenizer = AutoTokenizer.from_pretrained("t5-base")

    def normalize_tones(self, text):
        # Map complex diacritics to simple ones
        tone_mappings = {
            'ǎ': 'á',
            'ǐ': 'í',
            'ǒ': 'ó',
            'ǔ': 'ú',
            'ě': 'é'
        }
        for complex_tone, simple_tone in tone_mappings.items():
            text = text.replace(complex_tone, simple_tone)
        return text

    def convert_numbers(self, text):
        # Basic number conversion - expand this based on Twi number rules
        number_words = {
            '0': 'hwee', '1': 'baako', '2': 'mmienu',
            '3': 'mmiɛnsa', '4': 'nan', '5': 'num',
            '6': 'nsia', '7': 'nson', '8': 'nwɔtwe',
            '9': 'nkron', '10': 'du'
        }
        words = text.split()
        for i, word in enumerate(words):
            if word.isdigit() and word in number_words:
                words[i] = number_words[word]
        return ' '.join(words)

    def restore_diacritics(self, text):
        inputs = self.diacritic_tokenizer(text, return_tensors="pt", padding=True)
        outputs = self.diacritic_model.generate(**inputs)
        return self.diacritic_tokenizer.decode(outputs[0], skip_special_tokens=True)

    def preprocess(self, text):
        text = self.normalize_tones(text)
        text = self.convert_numbers(text)
        text = self.restore_diacritics(text)
        return text
