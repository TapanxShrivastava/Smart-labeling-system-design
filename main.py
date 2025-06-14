print("🔧 Script started")

import random
from label_generator import generate_label
from qr_decoder import decode_qr
from label_validator import validate_label_data
from logger import log_inspection
from datetime import datetime

# Example simulated input
device_id = f"DEV{random.randint(1000, 9999)}"
batch_id = f"BATCH{random.randint(1000, 9999)}"
mfg_date = datetime.now().strftime("%Y-%m-%d")
rohs = "Yes"

# Generate label
label_data, image_path = generate_label(device_id, batch_id, mfg_date, rohs)

# Decode QR content
decoded_texts = decode_qr(image_path)

# Validate data
result = "PASS" if validate_label_data(label_data, decoded_texts) else "FAIL"

print(f"\n📦 Label saved at: {image_path}")
print(f"✅ Inspection Result: {result}")

# Log inspection
log_inspection(label_data, result)

print("🔧 Script finished")
