import os

def apply_patches():
    input_file = "subsdk0"
    output_file = "subsdk0_patched"

    # Define our Hex Edits (Offsets from Build 1EDCF93889AC1016)
    # Format: { Offset: New_Hex_Bytes }
    patches = {
        0x002A4B80: "200080D2C0035FD6", # Auth Bypass
        0x002A4D10: "200080D2C0035FD6", # Token Mock
        0x002A50F4: "C0035FD6",         # Error Silencer
        0x0035A1E0: "64756D6D792E6E657400", # dummy.net redirect
        0x0024C1B0: "000080D2C0035FD6", # Free Chat
        0x004E8A30: "200080D2C0035FD6", # Unlock Cosmetics
    }

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found in repo!")
        return

    with open(input_file, "rb") as f:
        data = bytearray(f.read())

    for offset, hex_str in patches.items():
        patch_bytes = bytes.fromhex(hex_str)
        data[offset:offset+len(patch_bytes)] = patch_bytes
        print(f"Patched offset {hex(offset)}")

    with open(output_file, "wb") as f:
        f.write(data)
    
    # Rename to match Atmosphere requirements
    if os.path.exists("subsdk0_patched"):
        os.rename("subsdk0_patched", "subsdk0")

if __name__ == "__main__":
    apply_patches()