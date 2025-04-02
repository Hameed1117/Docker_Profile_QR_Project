import os
import qrcode
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_qr_code(url, file_path, fill_color="black", back_color="white"):
    """
    Generate a QR code and save it to file_path
    
    Args:
        url (str): The URL to encode in the QR code
        file_path (str): The path where the QR code image will be saved
        fill_color (str): Color of the QR code
        back_color (str): Background color
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save it
        img.save(file_path)
        logger.info(f"QR code for URL '{url}' successfully generated and saved to '{file_path}'")
        return True
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        return False

def main():
    # Get parameters from environment variables with defaults
    url = os.environ.get('QR_DATA_URL', 'https://github.com/kaw393939')  # Default to professor's GitHub
    qr_code_dir = os.environ.get('QR_CODE_DIR', 'qr_codes')
    filename = os.environ.get('QR_CODE_FILENAME', 'github_qr.png')
    fill_color = os.environ.get('FILL_COLOR', 'black')
    back_color = os.environ.get('BACK_COLOR', 'white')
    
    # Construct file path
    file_path = os.path.join(qr_code_dir, filename)
    
    # Generate QR code
    logger.info(f"Generating QR code for URL: {url}")
    logger.info(f"Using colors - Fill: {fill_color}, Background: {back_color}")
    
    success = generate_qr_code(url, file_path, fill_color, back_color)
    
    if success:
        logger.info("QR code generation completed successfully")
    else:
        logger.error("QR code generation failed")

if __name__ == "__main__":
    main()