import os
import sys
import json

def scan_files(target_path):
    # 1. Validation: Make sure the path actually exists
    if not os.path.exists(target_path):
        # We output a small JSON error so Godot knows what happened
        print(json.dumps({"error": f"Path '{target_path}' not found."}))
        return

    results = []

    # 2. The Jungle: Scanning the directory
    try:
        with os.scandir(target_path) as entries:
            for entry in entries:
                try:
                    # Defensive Check: Some files (like sockets) don't have a 'size'
                    info = entry.stat()
                    size_mb = info.st_size / (1024 * 1024)
                except (OSError, PermissionError):
                    # Default to 0 if the OS blocks us
                    size_mb = 0.0

                # 3. Data Collection: Building the "DNA" for each tower
                results.append({
                    "name": entry.name,
                    "size": round(size_mb, 2),
                    "is_dir": entry.is_dir(),
                    "is_hidden": entry.name.startswith('.')
                })
    except PermissionError:
        print(json.dumps({"error": "Permission denied to access this folder."}))
        return

    # 4. The Handshake: Output the final list as a JSON string
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    # If you provide a path like: python scanner.py ~/Downloads
    if len(sys.argv) > 1:
        scan_files(sys.argv[1])
    else:
        # Default to current directory if no argument is given
        scan_files('.')
