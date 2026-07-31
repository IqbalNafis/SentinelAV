def display_report(file_info, analysis, action = None):
    print("\n" + "=" * 40)
    print("        SentinelAV Scan Report")
    print("=" * 40)

    print("\nFILE INFORMATION")
    print("=" * 40)

    print(f"Filename   : {file_info['name']}")
    print(f"Extension  : {file_info['extension']}")
    print(f"Size       : {file_info['size']} bytes")
    print(f"Created    : {file_info['created']}")
    print(f"Modified   : {file_info['modified']}")
    print("\nFILE FINGERPRINT")
    print("=" * 40)
    print("\nSHA256")
    print(file_info['sha256'])
    print("\nRISK ASSESSMENT")
    print("=" * 40)
    print(f"Risk Level : {analysis['risk']}")
    print(f"Reason     : {analysis['reason']}")
    print("\nACTION")
    print("=" * 40)

    if action:
        print(f"Status     : {action}")
        print("=" * 40)
