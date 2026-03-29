import os

def apply_patches():
    if not os.path.exists("subsdk0"):
        print("Error: subsdk0 not found!")
        return

    with open("subsdk0", "rb") as f:
        data = bytearray(f.read())

    # We use "Pattern Matching" instead of hard offsets to find your version's code
    # This searches for the function logic and replaces it
    def patch_pattern(search_hex, replace_hex, name):
        search_bytes = bytes.fromhex(search_hex)
        replace_bytes = bytes.fromhex(replace_hex)
        index = data.find(search_bytes)
        if index != -1:
            data[index:index+len(replace_bytes)] = replace_bytes
            print(f"Successfully patched: {name} at {hex(index)}")
        else:
            print(f"Failed to find pattern for: {name}")

    # 1. Auth Bypass (Force True)
    patch_pattern("F30300AAF40301AA", "200080D2C0035FD6", "Auth Bypass")
    
    # 2. Token Mock
    patch_pattern("FF0301D1F44F02A9", "200080D2C0035FD6", "Token Mock")
    
    # 3. Server Redirect (nintendo.net -> dummy.net)
    patch_pattern("6E696E74656E646F2E6E6574", "64756D6D792E6E657400", "Server Redirect")

    # 4. Free Chat
    patch_pattern("F44FBEA9FD7B01A9", "000080D2C0035FD6", "Free Chat")

    with open("subsdk0", "wb") as f:
        f.write(data)

if __name__ == "__main__":
    apply_patches()