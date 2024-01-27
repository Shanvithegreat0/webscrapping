import fitz  # PyMuPDF
import re

def extract_information(text):
    # Extract Name
    name_match = re.search(r'Name: (.+)', text)
    name = name_match.group(1) if name_match else 'N/A'

    # Extract Education details
    education_match = re.search(r'Education: (.+)', text)
    education = education_match.group(1) if education_match else 'N/A'

    # Extract Work experience
    experience_match = re.search(r'Work Experience: (.+)', text)
    experience = experience_match.group(1) if experience_match else 'N/A'

    return name, education, experience

def scrape_pdf(file_path):
    pdf_document = None

    try:
        # Open the PDF file
        pdf_document = fitz.open(file_path)

        # Iterate through each page and extract text
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text = page.get_text()

            # Print raw text for debugging
            print(f"Raw Text from Page {page_number + 1}:\n{text}\n{'='*50}")

            # Extract information from the text
            name, education, experience = extract_information(text)

            # Print or process the extracted information as needed
            print(f"Page {page_number + 1} - Name: {name}\nEducation: {education}\nWork Experience: {experience}")
            print('='*50)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the PDF document if it was opened successfully
        if pdf_document:
            pdf_document.close()

def main():
    # Get user input for the PDF file path
    pdf_file_path = input("Enter the path of the PDF file on your desktop: ")

    # Call the function to scrape the PDF
    scrape_pdf(pdf_file_path)

if __name__ == "__main__":
    main()
