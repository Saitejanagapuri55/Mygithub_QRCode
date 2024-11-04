import qrcode
import os

def generate_qr():
    # Retrieve environment variables
    url = os.getenv('QR_DATA_URL', 'https://github.com/Saitejanagapuri55')  # Your GitHub profile URL
    fill_color = os.getenv('FILL_COLOR', 'black')
    back_color = os.getenv('BACK_COLOR', 'white')
    qr_code_dir = os.getenv('QR_CODE_DIR', '/app/qr_codes')  # Directory set to save in the container
    filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    if not os.path.exists(qr_code_dir):
        os.makedirs(qr_code_dir)
    img.save(os.path.join(qr_code_dir, filename))
    print(f"QR code generated and saved as {filename} in {qr_code_dir}")

if __name__ == "__main__":
    generate_qr()
