class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def show_member(self):
        print(f"Member Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {self.borrowed_books}")


member = Member("Mehedi", "M001")

member.show_member()