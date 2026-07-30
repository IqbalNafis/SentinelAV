from datetime import datetime
from logging import log


def save_log(file_info, analysis):
    with open("reports/scan_history.log", "a") as log:

        log.write("\n" + "=" * 40 + "\n")
        log.write("SentinelAV Scan Event\n")
        log.write("=" * 40 + "\n")

        log.write(f"Time       : {datetime.now()}\n")
        log.write(f"Filename   : {file_info['name']}\n")
        log.write(f"Extension  : {file_info['extension']}\n")
        log.write(f"Size       : {file_info['size']} bytes\n")

        log.write("\nSHA256\n")
        log.write(f"{file_info['sha256']}\n")

        log.write("\nRisk Assessment\n")
        log.write(f"Risk       : {analysis['risk']}\n")
        log.write(f"Reason     : {analysis['reason']}\n")

        log.write("=" * 40 + "\n")
