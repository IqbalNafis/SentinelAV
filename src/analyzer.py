def analyze_file(file_info):
    """
    Perform basic risk assessment based on file characteristics.
    """
    FILE_TYPE_EXTENSIONS = {
        "PE executable": [".exe", ".dll", ".sys"],
        "PDF document": [".pdf"],
        "PNG image": [".png"],
        "JPEG image": [".jpg", ".jpeg"]
    }
    file_type = file_info["file_type"]
    if file_type in FILE_TYPE_EXTENSIONS:
        valid_extensions = FILE_TYPE_EXTENSIONS[file_type]

        if extension not in valid_extensions:
            analysis["risk"] = "HIGH"
            analysis["reason"] = "File extension does not match detected file type"

    extension = file_info["extension"].lower()

    analysis = {
        "risk": "LOW",
        "reason": "No suspicious characteristics detected"
    }

    if extension in [".exe", ".bat", ".ps1", ".cmd"]:
        analysis["risk"] = "HIGH"
        analysis["reason"] = "Executable or script file"

    elif extension in [".zip", ".rar", ".7z"]:
        analysis["risk"] = "MEDIUM"
        analysis["reason"] = "Compressed archive"

    return analysis