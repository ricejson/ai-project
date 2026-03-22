import os
from fpdf import FPDF
from langchain_core.tools import tool

BASE_DIR = "./pdf"

@tool
def generate_pdf(file_name: str, content: str) -> str:
    """Generate a PDF file with given content."""
    file_path = os.path.join(BASE_DIR, file_name)
    try:
        os.makedirs(BASE_DIR, exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        # 支持中文 - 使用 Arial Unicode
        pdf.add_font('ArialUnicode', '', '/Library/Fonts/Arial Unicode.ttf')
        pdf.set_font('ArialUnicode', size=12)
        # 写入内容
        pdf.multi_cell(0, 10, content)
        pdf.output(file_path)
        return f"PDF generated successfully to: {file_path}"

    except Exception as e:
        return f"Error generating PDF: {e}"

