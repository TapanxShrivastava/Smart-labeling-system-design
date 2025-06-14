# label_generator.py
import qrcode
import uuid
from datetime import datetime
import os

def generate_label(device_id, batch_id, mfg_date, rohs_compliance):
    # Generate unique serial number
    serial_number = str(uuid.uuid4())[:8]

    # Prepare label content as a string
    label_data = {
        "Device ID": device_id,
        "Batch ID": batch_id,
        "Manufacturing Date": mfg_date,
        "RoHS Compliance": rohs_compliance,
        "Serial Number": serial_number
    }

    # Convert dict to multiline string
    label_text = "\n".join([f"{key}: {value}" for key, value in label_data.items()])

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(label_text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image in folder 'output_labels'
    output_dir = "output_labels"
    os.makedirs(output_dir, exist_ok=True)
    img_path = os.path.join(output_dir, f"label_{serial_number}.png")
    img.save(img_path)

    print(f"✅ Label generated and saved to {img_path}")
    return label_data, img_path

# This part runs only if you run this file directly (optional)
if __name__ == "__main__":
    label, path = generate_label("DVC1234", "BATCH567", datetime.now().strftime("%Y-%m-%d"), "Yes")
    print(label)
