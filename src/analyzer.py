
def analyze_file(file_info):
    """
    Assess file risk using a simple, explainable scoring model.

    Scores are heuristic indicators, not proof of malware.
    """

    FILE_TYPE_EXTENSIONS = {
        "PE executable": [".exe", ".dll", ".sys"],
        "PDF document": [".pdf"],
        "PNG image": [".png"],
        "JPEG image": [".jpg", ".jpeg"]
    }

    EXECUTABLE_EXTENSIONS = [
        ".exe", ".dll", ".sys", ".bat", ".ps1", ".cmd"
    ]

    ARCHIVE_EXTENSIONS = [".zip", ".rar", ".7z"]

    extension = file_info["extension"].lower()
    file_type = file_info.get("file_type", "Unknown")

    score = 0
    evidence = []

    # Rule 1: Executables and scripts
    if extension in EXECUTABLE_EXTENSIONS:
        score += 4
        evidence.append("Executable or script file")

    # Rule 2: File type and extension mismatch
    if file_type in FILE_TYPE_EXTENSIONS:
        valid_extensions = FILE_TYPE_EXTENSIONS[file_type]

        if extension not in valid_extensions:
            score += 4
            evidence.append(
                "File extension does not match detected file type"
            )

    # Rule 3: Compressed archives
    if extension in ARCHIVE_EXTENSIONS:
        score += 2
        evidence.append("Compressed archive")

    # Convert the score into a risk category
    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    reason = "; ".join(evidence) if evidence else (
        "No suspicious characteristics detected by current rules"
    )

    return {
        "risk": risk,
        "reason": reason,
        "score": score,
        "evidence": evidence
    }
