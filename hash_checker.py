import hashlib

def get_file_hash(file_path, algorithm):
    hash_obj = hashlib.new(algorithm)

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()

print("===================================")
print("      FILE HASH CHECKER")
print("===================================")

file_path = input("Enter file path: ")

try:
    md5_hash = get_file_hash(file_path, "md5")
    sha256_hash = get_file_hash(file_path, "sha256")

    print("\n[MD5]")
    print(md5_hash)

    print("\n[SHA-256]")
    print(sha256_hash)

    choice = input("\nCompare with existing hash? (Y/N): ").upper()

    if choice == "Y":
        user_hash = input("Enter hash value: ")

        if user_hash.lower() == md5_hash.lower():
            print("\n[SUCCESS] MD5 Hash Match!")
        elif user_hash.lower() == sha256_hash.lower():
            print("\n[SUCCESS] SHA-256 Hash Match!")
        else:
            print("\n[WARNING] Hash Mismatch! File may have changed.")

except FileNotFoundError:
    print("\n[ERROR] File not found.")
except Exception as e:
    print(f"\n[ERROR] {e}")