import os
import sys
import tempfile
import pytest
import logging
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import generate_qr_code, main

def test_directory_already_exists():
    """Test when directory already exists"""
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir = os.path.join(temp_dir, "existing_dir")
        os.makedirs(sub_dir, exist_ok=True)
        
        file_path = os.path.join(sub_dir, "test.png")
        result = generate_qr_code("https://github.com", file_path)
        
        assert result is True
        assert os.path.exists(file_path)

def test_log_messages():
    """Test that log messages are generated correctly"""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "log_test.png")
        
        # Capture logs
        with patch('logging.Logger.info') as mock_info:
            with patch('logging.Logger.error') as mock_error:
                # Successful generation
                generate_qr_code("https://test-url.com", file_path)
                
                # Check correct log message was called
                mock_info.assert_any_call(f"QR code for URL 'https://test-url.com' successfully generated and saved to '{file_path}'")
        
        # Test error logging
        with patch('logging.Logger.info') as mock_info:
            with patch('logging.Logger.error') as mock_error:
                with patch('qrcode.QRCode', side_effect=Exception("Test log exception")):
                    # Failed generation
                    generate_qr_code("https://test-url.com", file_path)
                    
                    # Check error was logged
                    mock_error.assert_called_once()

def test_main_logging():
    """Test logging in the main function"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set environment variables
        with patch.dict(os.environ, {
            'QR_DATA_URL': 'https://test-main-logging.com',
            'QR_CODE_DIR': temp_dir,
            'QR_CODE_FILENAME': 'log_main.png',
        }):
            # Capture logs
            with patch('logging.Logger.info') as mock_info:
                # Run main
                main()
                
                # Check that URL was logged
                mock_info.assert_any_call(f"Generating QR code for URL: https://test-main-logging.com")



