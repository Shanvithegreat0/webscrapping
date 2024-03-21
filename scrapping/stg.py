import pdfplumber
import re
import os
import json

def extract_information(text):
    # Initialize variables to store extracted data
    extracted_data = {}

    # Define patterns for extracting information
    patterns = {
        "Name": r'(\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b',
        "Education": r'EDUCATION(?:\s*SKILLS)?\s*(.*?)(?=WORK EXPERIENCE|\bACHIEVEMENTS\b|$)',
        "Work Experience": r'WORK EXPERIENCE\s*(.*?)(?=ACHIEVEMENTS|$)',
    }

    # Extract information using regular expressions
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        extracted_data[key] = match.group(1).strip() if match else 'N/A'

    return extracted_data

def scrape_pdf(file_path):
    raw_text_data = ""

    try:
        # Open the PDF file
        with pdfplumber.open(file_path) as pdf_document:
            # Iterate through each page and extract text
            for page_number in range(len(pdf_document.pages)):
                page = pdf_document.pages[page_number]
                text = page.extract_text()

                # Append raw text to the variable
                raw_text_data += f"Raw Text from Page {page_number + 1}:\n{text}\n{'='*50}\n"

                # Print raw text for debugging
                print(f"Raw Text from Page {page_number + 1}:\n{text}\n{'='*50}\n")

                # Extract information from the text
                extracted_data = extract_information(text)

                # Print or process the extracted information as needed
                print(f"Page {page_number + 1} - Extracted Data: {extracted_data}")
                print('='*50)

    except Exception as e:
        print(f"Error: {e}")

    return raw_text_data, extracted_data

def main():
    # Get user input for the PDF file path
    pdf_file_path = input("Enter the path of the PDF file: ")

    # Call the function to scrape the PDF
    raw_text_data, extracted_data = scrape_pdf(pdf_file_path)

    # Save raw text data to a text file
    with open('raw_text_data.txt', 'w', encoding='utf-8') as file:
        file.write(raw_text_data)

    # Convert extracted data to JSON format
    json_data = json.dumps(extracted_data, indent=4)

    # Save JSON data to a file
    with open('extracted_data.json', 'w') as json_file:
        json_file.write(json_data)

    # Delete the raw text file
    os.remove('raw_text_data.txt')

if __name__ == "__main__":
    main()
