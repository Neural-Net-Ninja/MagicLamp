from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak

# Register the font (replace 'Calibri-Light.ttf' with the path to your .ttf file)
pdfmetrics.registerFont(TTFont('Calibri-Light', 'C:\Fonts\calibril.ttf'))


def text_to_pdf(text_file, pdf_file):
    # Create a new PDF document
    doc = SimpleDocTemplate(pdf_file,
                            pagesize=letter,
                            leftMargin=0.5*inch,
                            rightMargin=0.5*inch,
                            topMargin=0.5*inch,
                            bottomMargin=0.5*inch)
    elements = []

    # Set up styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = styles["BodyText"]
    title_style.fontName = 'Calibri-Light'
    body_style.alignment = 4  # Justify text
    
    # Define a custom style for preformatted text to preserve spaces
    preformatted_style = ParagraphStyle(
        'Preformatted',
        fontName='Courier',
        fontSize=10,
        leading=12,
        spaceBefore=10,
        spaceAfter=10
    )

    # Title
    title = "Sprint Momentum Stocks"
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 0.2 * inch))

    # Define a custom style for the author's name
    author_style = ParagraphStyle(
        'Author',
        parent=body_style,
        textColor='grey',
        alignment=2  # Right alignment
    )

    # Author
    author = "Dhananjay Umalkar"
    elements.append(Paragraph(author, author_style))
    elements.append(Spacer(1, 0.2 * inch))

    # Description
    description = """
    This algorithm employs a sophisticated blend of technical analysis strategies to identify potential bullish opportunities in the stock market. The key components are:

    Momentum Indicator: Identifies stocks whose closing prices have increased by at least 2% for three consecutive days, suggesting strong upward momentum.

    Bullish Engulfing Pattern: A classic signal of a bullish trend reversal, formed when a larger bullish candlestick completely engulfs the prior smaller bearish candlestick, indicating a potential shift from a downtrend to an uptrend.

    Three White Soldiers: Consists of three consecutive green candlesticks, each opening higher than the previous day's open, indicating a robust and sustained uptrend.

    52-Week High Breakout: Identifies stocks whose current day's closing price exceeds the highest high of the past 52 weeks, suggesting a potential bullish run and significant upward momentum.

    Rising Volume: Tracks volume trends to identify stocks with increasing trading volume. Rising volume alongside price increases confirms the strength of the bullish trend, indicating heightened investor interest and commitment.

    Combining these strategies helps detect stocks with strong bullish signals by leveraging momentum, pattern recognition, and volume confirmation.
    """
    for line in description.strip().split('\n'):
        elements.append(Paragraph(line.strip(), body_style))
    
    # Open the text file and add its content as preformatted text
    with open(text_file, 'r') as f:
        file_content = f.read()
    
    preformatted_paragraph = Preformatted(file_content, preformatted_style)
    elements.append(preformatted_paragraph)

    # Build the PDF
    doc.build(elements)

# Example usage:
text_to_pdf('momentum_stocks.txt', 'momentum_stocks.pdf')
