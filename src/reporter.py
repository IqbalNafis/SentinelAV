def display_report(file_info, analysis):
    print("\n" + "=" * 40)
    print("        SentinelAV Scan Report")
    print("=" * 40)

    print(f"Filename   : {file_info['name']}")
    print(f"Risk Level : {analysis['risk']}")
    print(f"Reason     : {analysis['reason']}")
    print(f"Extension  : {file_info['extension']}")
    print(f"Size       : {file_info['size']} bytes")
    print(f"Created    : {file_info['created']}")
    print(f"Modified   : {file_info['modified']}")

    print("\nSHA256")
    print(file_info['sha256'])
    print("\nRisk Assessment")
    print(f"Risk       : {analysis['risk']}")
    print(f"Reason     : {analysis['reason']}")
    
    print("=" * 40)