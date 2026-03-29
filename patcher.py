import os
import sys

def apply_patches():
    # We expect 'subsdk0' to be in the folder thanks to the GitHub Action
    file_path = "subsdk0"
    
    if not os.path.exists(file_path):
        print("Error: subsdk0 not found!")
        sys.exit(1)

    # Verified Offsets for Among Us 1EDCF93889AC1016
    patches = {
        0x002A4B80: "200080D2C0035FD6", # Auth Bypass
        0x002A4D10: "200080D2C0035FD6", # Token Mock
        0x002A50F4: "C0035FD6",         # Error Silencer (Kills NintendoAuthFailed)
        0x0035A1E0: "64756D6D792E6E657400", # dummy.net redirect
        0x0024C1B0: "000080D2C0035FD6", # Free Chat
        0x004E8A30: "200080D2C0035FD6", # Unlock Cosmetics
        0x004B21F0: "200080D2C0035FD6", # Always Host
        0x004C5A10: "200080D2C0035FD6"  # Always Impostor
    }

    with open(file_path, "rb") as f:
        data = bytearray(f.read())

    for offset, hex_str in patches.items():
        patch_bytes = bytes.fromhex(hex_str)
        data[offset:offset+len(patch_bytes)] = patch_bytes
        print(f"Patched {hex(offset)}")

    with open("subsdk0", "wb") as f:
        f.write(data)

if __name__ == "__main__":
    apply_patches()