import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    
    with open(filename, 'r') as f:
        password = f.readline().strip()
    
    encrypted_password = caesar_encrypt(password)
    
    with open(filename, 'w') as f:
        f.write(encrypted_password)

if __name__ == "__main___":
    encrypt_single_pass("examples/example1.txt")

def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    
    with open(filename, 'r') as f:
        lector = csv.reader(file)

        for file in lector:
            print(file)
            
    for i in range(1, len(rows)): 
        rows[i][2] = caesar_encrypt(rows[i][2])
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(file)
        writer.writerows(rows)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]
    
    found = False
    
    for i in range(1, len(rows)):
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)
            found = True
            break
    
    if not found:
        return False
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    
    encrypted = caesar_encrypt(password)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted])