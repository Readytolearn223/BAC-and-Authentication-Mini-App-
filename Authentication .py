# Hardcoded users with their roles
users = {
    "jake": "admin",
    "bob": "user"
}

# Simulated login function
def login():
    while True:
        username = input("Enter your username: ").strip()
        if username in users:
            role = users[username]
            print(f"Login successful! Welcome {username}. Your role is '{role}'.\n")
            return role
        else:
            print("Unknown user. Please try again.\n")

# Protected actions
def admin_actions():
    print("Admin Actions:")
    print("- Access Users")
    print("- Access Cameras")
    print("- Access Settings\n")

def user_actions():
    print("User Actions:")
    print("- Access Settings")
    print("- Change Password\n")

# Access control function
def access_control(role):
    if role == "admin":
        admin_actions()
    elif role == "user":
        user_actions()
    else:
        print("Access Denied! Unknown role.")

# --- Simulation ---
role = login()
access_control(role)


#Explanation of how my app shows one part of the CIA triad
"""
How my apps demonstrates the Confidentiality aspect of the CIA triad by enforcing role-based access control.
 It will ensure that only authorized users such as admins or regular users have the ability to access certain 
 actions or data .This will prevent unauthorized access and keep sensitive information restricted to the correct 
 role.

"""