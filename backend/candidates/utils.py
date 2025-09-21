import PyPDF2
import docx
import re
import spacy

class SimpleResumeParser:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            self.nlp = None
    
    def extract_text_from_pdf(self, file_path):
        """Simple PDF text extraction"""
        text = ""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"PDF extraction error: {e}")
        return text
    
    def extract_text_from_docx(self, file_path):
        """Extract text from DOCX"""
        try:
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"DOCX extraction error: {e}")
            return ""
    
    def extract_skills(self, text):
        """Basic skill extraction"""
        common_skills = [
            'Python', 'Java', 'JavaScript', 'C++', 'Django', 'React', 
            'Node.js', 'MySQL', 'PostgreSQL', 'AWS', 'Git', 'HTML', 'CSS'
        ]
        
        found_skills = []
        text_lower = text.lower()
        
        for skill in common_skills:
            if skill.lower() in text_lower:
                found_skills.append(skill)
        
        return found_skills
    
    def extract_experience_years(self, text):
        """Extract years of experience"""
        patterns = [
            r'(\d+)\+?\s*years?\s*of\s*experience',
            r'(\d+)\+?\s*years?\s*experience'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        return 0
