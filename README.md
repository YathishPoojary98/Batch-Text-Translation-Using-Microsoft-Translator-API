## Batch Text Translation Using Microsoft Translator API

Key Features:

Batch Translation: Translates multiple lines of text from an input file.

Language Support: Supports all languages provided by the Microsoft Translator API.

Customizable: Allows specifying both source and target languages.

Seamless Integration: Easily configurable with your Azure Translator API credentials.

Usage:

Run the script from the command line with the following arguments:

python translate_script.py input.txt output.txt target_language

input.txt: File containing the text to be translated.

output.txt: File where the translated text will be saved.

target_language: Language code for the target language (e.g., kn for Kannada, es for Spanish).

Setup and Prerequisites:

Azure Subscription: Create a Translator service resource in Azure.

API Key and Endpoint: Obtain your subscription_key, endpoint, and region from Azure Portal.

Install the required Python library:

pip install requests

Example:

To translate the content of data.txt into Kannada (kn):

python translate_script.py data.txt translated_data.txt kn

Output: The translated content will be written to translated_data.txt.

Code Highlights:

Custom class MicrosoftTranslator for API handling.

Reads input line by line for efficient processing.

Handles empty lines gracefully.

Outputs clean, translated text line by line.

API Details:

Endpoint: https://api.cognitive.microsofttranslator.com/

API Version: 3.0

Required Headers: Ocp-Apim-Subscription-Key, Ocp-Apim-Subscription-Region, and Content-Type.

This script is ideal for automating text translation workflows, enabling seamless multilingual text processing with Microsoft Translator API.
