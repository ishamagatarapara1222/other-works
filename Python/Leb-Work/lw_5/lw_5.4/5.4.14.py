#14. Inherit Admin from User and pass initial values up to the User constructor using super().

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email, access_level):
        # Forwarding initialization parameters up to User initialization chain
        super().__init__(username, email)
        self.access_level = access_level

    def show_profile(self):
        print(f"Admin User: {self.username} | Email: {self.email} | Access: {self.access_level}")

# Testing
admin_user = Admin("root_admin", "admin@domain.com", "Superuser / Full Access")
admin_user.show_profile()
