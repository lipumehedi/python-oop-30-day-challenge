def login_required(func):
    def wrraper(is_logged_in):
        if is_logged_in:
            func()
            
        else:
            print("Access denied! Please login first.")
            
    return wrraper

@login_required
def dashboard():
    print("Welcome to your dashboard")
    
dashboard(True)
dashboard(False)