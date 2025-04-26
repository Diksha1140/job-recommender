import PyPDF2
import docx
import os

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def extract_text(self):
        """Extract text from PDF or DOCX files"""
        file_extension = self.file_path.split('.')[-1].lower()
        
        if file_extension == 'pdf':
            return self._extract_from_pdf()
        elif file_extension in ['doc', 'docx']:
            return self._extract_from_docx()
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
    
    def _extract_from_pdf(self):
        """Extract text from PDF"""
        text = ""
        try:
            with open(self.file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page_num].extract_text()
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
        return text
    
    def _extract_from_docx(self):
        """Extract text from DOCX"""
        try:
            doc = docx.Document(self.file_path)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            return '\n'.join(full_text)
        except Exception as e:
            print(f"Error extracting text from DOCX: {e}")
            return ""
