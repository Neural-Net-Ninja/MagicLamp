from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from PIL import Image

def image_to_watermark_pdf(image_path, output_pdf, opacity=0.21):
    # Open the image file
    with Image.open(image_path) as img:
        # Get image size
        img_width, img_height = img.size

    # Create a new PDF with Reportlab
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Calculate position for centering the image at the bottom of the page
    page_width, page_height = letter
    x = (page_width - img_width) / 2
    y = 0  # position at bottom

    # Set the alpha value before drawing the image
    c.setFillAlpha(opacity)

    # Draw the image to the canvas
    c.drawImage(image_path, x, y, width=img_width, height=img_height, mask='auto')

    # Finish the page and save the PDF
    c.showPage()
    c.save()

# Example usage:
image_to_watermark_pdf('bull.jpg', 'momentum_stocks.pdf')