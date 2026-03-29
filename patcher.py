import os

def apply_patches():
    # This script assumes you used curl to download 'subsdk0' into the runner
    file_path = "subsdk0"
    
    if not os.path.exists(file_path):
        print("Error: subsdk0 not found!")
        return

    with open(file_path, "rb") as f:
        data = bytearray(f.read())

    def patch_pattern(search_hex, replace_hex, name):
        search_bytes = bytes.fromhex(search_hex)
        replace_bytes = bytes.fromhex(replace_hex)
        index = data.find(search_bytes)
        if index != -1:
            data[index:index+len(replace_bytes)] = replace_bytes
            print(f"Patched: {name} at {hex(index)}")
        else:
            print(f"Warning: Could not find pattern for {name}")

    # --- TAGNX UPDATED PATCHES ---
    
    # 1. Auth Bypass: Forces 'IsAuthenticated' to True
    patch_pattern("F30300AAF40301AA", "200080D2C0035FD6", "Auth Bypass")
    
    # 2. Token Mock: Forces successful token return
    patch_pattern("FF0301D1F44F02A9", "200080D2C0035FD6", "Token Mock")
    
    # 3. Server Redirect: Redirects nintendo.net to dummy.net
    # This search pattern looks for the string 'nintendo.net'
    patch_pattern("6E696E74656E646F2E6E6574", "64756D6D792E6E657400", "Server Redirect")

    # 4. Free Chat: Bypasses the 'Guest' account restriction
    patch_pattern("F44FBEA9FD7B01A9", "000080D2C0035FD6", "Free Chat")

    # 5. All Cosmetics: Unlock Skins, Pets, and Hats
    patch_pattern("F657BD91F44F01A9", "200080D2C0035FD6", "Cosmetic Unlock")

    with open("subsdk0", "wb") as f:
        f.write(data)
    print("Patching Complete.")

if __name__ == "__main__":
    apply_patches()