import PyPDF2
import os

def split_last_page_from_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_pdf = os.path.join(input_folder, filename)
            try:
                # Open the PDF file
                with open(input_pdf, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    total_pages = len(reader.pages)

                    # Check if there are pages to split
                    if total_pages == 0:
                        print(f"The PDF '{input_pdf}' is empty.")
                        continue

                    # Get the last page
                    last_page = reader.pages[total_pages - 2]

                    # Write the last page to a new PDF
                    writer = PyPDF2.PdfWriter()
                    writer.add_page(last_page)

                    output_pdf = os.path.join(output_folder, f'last_page_{filename}')
                    with open(output_pdf, 'wb') as output_file:
                        writer.write(output_file)

                print(f"Extracted the last page of '{input_pdf}' to '{output_pdf}'.")

            except Exception as e:
                print(f"Failed to process '{input_pdf}': {e}")

# Usage
input_folder = 'C:\INPUT PAKUTANDANG\INPUT PAKUTANDANG FOUR'  # Replace with the path to your input folder
output_folder = 'C:\INPUT PAKUTANDANG\PDF SU FOUR'  # Replace with your desired output folder
split_last_page_from_folder(input_folder, output_folder)
