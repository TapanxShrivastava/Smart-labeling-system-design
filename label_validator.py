def validate_label_data(original_data, decoded_texts):
    # Join all decoded strings (usually only one QR string)
    combined_text = "\n".join(decoded_texts)

    success = True
    for key, value in original_data.items():
        if value not in combined_text:
            print(f"❌ Mismatch or Missing: {key} -> {value}")
            success = False
        else:
            print(f"✅ Matched: {key} -> {value}")
    
    return success
