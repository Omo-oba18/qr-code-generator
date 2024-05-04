import os
import uuid
import time
import qrcode
from PIL import Image

import uuid
import random
import time

def generate_qr_checker_url():
    prefix = '9b73'
    generated_uuid = ''

    # Generate UUIDs until we find one starting with the specified prefix
    while not str(generated_uuid).startswith(prefix):
        generated_uuid = uuid.uuid4()

    # Convert UUID to string with hyphens
    generated_code = str(generated_uuid)

    # Generate a random timestamp within a range (e.g., past week)
    current_time = int(time.time())
    random_timestamp = random.randint(current_time - (7 * 24 * 3600), current_time)  # Random timestamp within the past week

    # Construct the URL with the random timestamp
    base_url = "https://qr.cccwordwide.com/qrcode/checker/"
    url = f"{base_url}{prefix}{generated_code[len(prefix):]}/{random_timestamp}"

    return url

def generate_qr_code(url, output_folder, index):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=2, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    # Create PIL image from QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Define filename for the QR code image
    filename = f"ccc-qr-code-generated-{index}.png"

    # Save the QR code image to the output folder
    qr_image.save(os.path.join(output_folder, filename))

def main():
    # Prompt user to enter the number of QR codes to generate
    num_qr_codes = int(input("Enter the number of QR codes to generate: "))

    # Create a folder to store the generated QR code images
    output_folder = "generated_qr_codes"
    os.makedirs(output_folder, exist_ok=True)

    # Generate specified number of QR codes
    for i in range(1, num_qr_codes + 1):
        # Generate URL
        generated_url = generate_qr_checker_url()

        # Generate and save QR code image
        generate_qr_code(generated_url, output_folder, i)

        print(f"QR code {i} generated successfully.")

    print(f"All {num_qr_codes} QR codes generated and saved in '{output_folder}' folder.")

if __name__ == "__main__":
    main()
