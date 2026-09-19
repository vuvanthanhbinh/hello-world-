class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Tên sách:", self.title)
        print("Tác giả:", self.author)

books = [
    Book("Dế Mèn Phiêu Lưu Ký", "Tô Hoài"),
    Book("Lão Hạc", "Nam Cao"),
    Book("Nhà Giả Kim", "Paulo Coelho")
]
print("DANH SÁCH SÁCH")
print("-" * 30)

for book in books:
    book.display()
    print("-" * 30)