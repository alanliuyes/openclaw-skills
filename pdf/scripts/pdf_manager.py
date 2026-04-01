#!/usr/bin/env python3
"""
PDF Manager - PDF manipulation utilities
"""

from PyPDF2 import PdfReader, PdfWriter
import os

def extract_text(pdf_path):
    """Extract text from PDF"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDFs"""
    writer = PdfWriter()
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output_path, 'wb') as f:
        writer.write(f)
    return output_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        command = sys.argv[1]
        if command == "extract":
            text = extract_text(sys.argv[2])
            print(text[:1000])  # Print first 1000 chars