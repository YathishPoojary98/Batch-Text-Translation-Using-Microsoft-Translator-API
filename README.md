# 🌍 Batch Text Translation Using Microsoft Translator API

A Python script for **batch text translation** using the **Microsoft Translator API**, allowing seamless multilingual text processing. This tool is ideal for automating text translation workflows with efficient handling of multiple lines from an input file.

---

## 🚀 Key Features

✅ **Batch Translation** – Translates multiple lines of text from an input file.  
✅ **Language Support** – Supports all languages provided by Microsoft Translator API.  
✅ **Customizable** – Specify both **source** and **target** languages.  
✅ **Seamless Integration** – Easily configurable with your **Azure Translator API** credentials.  

---

## 🛠 Setup & Prerequisites

### 1️⃣ **Azure Subscription**
- Create a **Translator service resource** in **Azure**.
- Obtain your **API Key**, **Endpoint**, and **Region** from the **Azure Portal**.

### 2️⃣ **Install Required Libraries**
Make sure you have **requests** installed:
```bash
pip install requests
📌 Usage
Run the script from the command line with the following arguments:

bash
Copy
Edit
python translate_script.py input.txt output.txt target_language
Arguments:
input.txt – File containing the text to be translated.
output.txt – File where the translated text will be saved.
target_language – Language code for translation (e.g., kn for Kannada, es for Spanish).
Example
To translate data.txt into Kannada (kn) and save it to translated_data.txt:

bash
Copy
Edit
python translate_script.py data.txt translated_data.txt kn
Output: The translated content will be written to translated_data.txt.

📜 API Details
Endpoint: https://api.cognitive.microsofttranslator.com/
API Version: 3.0
Required Headers:
Ocp-Apim-Subscription-Key
Ocp-Apim-Subscription-Region
Content-Type
🔍 Code Highlights
✅ Custom Class MicrosoftTranslator – Handles API communication.
✅ Efficient Processing – Reads input line by line for optimized translation.
✅ Handles Empty Lines – Skips empty lines gracefully.
✅ Clean Output – Outputs translated text line by line in the specified language.

💡 Ideal Use Cases
✔ Bulk Text Translation – Automate translation of large text files.
✔ Multilingual Content Processing – Process documents in multiple languages.
✔ Workflow Automation – Enhance applications needing translation services.
