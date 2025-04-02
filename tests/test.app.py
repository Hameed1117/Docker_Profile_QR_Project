import unittest
import os
import sys
import tempfile

# Add the parent directory to sys.path to allow importing app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import generate_qr_code

class TestQRCodeGenerator(unittest.TestCase):
    
    def test_qr_code_generation(self):
        """Test that QR code generation works with default parameters"""
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "test_qr.png")
            
            # Generate a QR code
            test_url = "https://github.com/Hameed1117"
            result = generate_qr_code(test_url, file_path)
            
            # Check if the function reported success
            self.assertTrue(result)
            
            # Check if the file was actually created
            self.assertTrue(os.path.exists(file_path))
            
            # Check that the file is not empty
            self.assertGreater(os.path.getsize(file_path), 0)
    
    def test_qr_code_with_custom_colors(self):
        """Test QR code generation with custom colors"""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "test_qr_color.png")
            
            # Generate a QR code with custom colors
            test_url = "https://github.com/Hameed1117"
            result = generate_qr_code(test_url, file_path, fill_color="blue", back_color="yellow")
            
            # Check if the function reported success
            self.assertTrue(result)
            
            # Check if the file was created
            self.assertTrue(os.path.exists(file_path))
            
            # Check that the file is not empty
            self.assertGreater(os.path.getsize(file_path), 0)

if __name__ == "__main__":
    unittest.main()