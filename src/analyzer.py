def analyze_file(file_info):
    """
    Perform basic risk assessment based on file characteristics.
    """

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