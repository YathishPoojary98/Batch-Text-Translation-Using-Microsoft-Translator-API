import requests
import sys

class MicrosoftTranslator:
    def __init__(self, subscription_key, endpoint, region):
        self.subscription_key = subscription_key
        self.endpoint = endpoint
        self.region = region
        self.path = '/translate'
        self.url = f"{self.endpoint}{self.path}"
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Ocp-Apim-Subscription-Region': self.region,
            'Content-Type': 'application/json'
        }

    def translate(self, text, to_language, from_language=None):
        params = {
            'api-version': '3.0',
            'to': to_language
        }
        if from_language:
            params['from'] = from_language

        body = [{'text': text}]
        response = requests.post(self.url, params=params, headers=self.headers, json=body)
        response.raise_for_status()
        translations = response.json()
        return translations[0]['translations'][0]['text']

def translate_file(input_file, output_file, target_language, translator, from_language=None):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if line:  # Skip empty lines
                translated_line = translator.translate(line, target_language, from_language)
                outfile.write(translated_line + '\n')

# Example Usage
if __name__ == "__main__":
    # Replace with your Azure API details
    subscription_key = your_api_key
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    region = "centralindia"

    translator = MicrosoftTranslator(subscription_key, endpoint, region)
    
    input_file_path = sys.argv[1]  # Input file containing text to translate
    output_file_path = sys.argv[2]  # File to save the translated text
    target_language = sys.argv[3]  # Target language code (e.g., 'kn' for Kannada)

    translate_file(input_file_path, output_file_path, target_language, translator)
    print(f"Translation completed. Output saved to {output_file_path}.")
