import fitz  # PyMuPDF
from PIL import Image
import os

def pdf_to_image(pdf_file):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_file)
        total_pages = len(doc)
        print(f"PDF loaded successfully. Total pages: {total_pages}")

        while True:
            page_number = input("Enter the page number to convert (or type 'exit' to quit): ")
            if page_number.lower() == 'exit':
                print("Exiting program.")
                break

            if not page_number.isdigit():
                print("Invalid input. Please enter a valid page number.")
                continue

            page_number = int(page_number)
            if 1 <= page_number <= total_pages:
                # Get the selected page
                page = doc[page_number - 1]
                
                # Convert the page to an image
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                # Save the image
                image_filename = f"page_{page_number}.png"
                img.save(image_filename, "PNG")
                print(f"Page {page_number} saved as {image_filename}")
            else:
                print("Page number out of range. Try again.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_filename = "File_Name.pdf"
    if not os.path.exists(pdf_filename):
        print(f"Error: File '{pdf_filename}' not found!")
    else:
        pdf_to_image(pdf_filename)
