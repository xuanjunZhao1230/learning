"""
代码题：图书借阅管理器（难度：适中）

请使用面向对象编程完成一个小型图书馆：
1. Book 类保存书名、馆藏数量和可借数量，并能计算已借数量。
2. Library 类用字典保存图书，用“读者姓名: 已借图书集合”保存借阅记录。
3. 实现添加图书、借书、还书；不允许重复借同一本书，也不能借出库存为 0 的书。
4. 输出图书借出量排名（借出量降序、书名升序）和每位读者当前借阅的图书。
"""


class Book:
    def __init__(self, title, total):
        self.title = title
        self.total = total
        self.available = total

    @property
    def borrowed(self):
        return self.total - self.available

    def borrow(self):
        if self.available == 0:
            return False
        self.available -= 1
        return True

    def return_book(self):
        if self.available == self.total:
            return False
        self.available += 1
        return True


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.records = {}

    def add_book(self, title, total):
        if not title or total <= 0 or title in self.books:
            return False
        self.books[title] = Book(title, total)
        return True

    def borrow_book(self, reader, title):
        book = self.books.get(title)
        borrowed_books = self.records.get(reader, set())
        if not reader or book is None or title in borrowed_books:
            return False
        if not book.borrow():
            return False
        self.records.setdefault(reader, set()).add(title)
        return True

    def return_book(self, reader, title):
        borrowed_books = self.records.get(reader)
        if borrowed_books is None or title not in borrowed_books:
            return False
        if not self.books[title].return_book():
            return False
        borrowed_books.remove(title)
        if not borrowed_books:
            del self.records[reader]
        return True

    def book_ranking(self):
        return sorted(self.books.values(), key=lambda book: (-book.borrowed, book.title))

    def print_report(self):
        print(f'===== {self.name} =====')
        print('【图书借出量排名】')
        for index, book in enumerate(self.book_ranking(), start=1):
            print(f'{index}. {book.title}：已借 {book.borrowed} 本，剩余 {book.available} 本')

        print('\n【当前借阅记录】')
        if not self.records:
            print('暂无借阅记录')
        for reader, titles in sorted(self.records.items()):
            print(f'{reader}：' + '、'.join(sorted(titles)))


def main():
    library = Library('晨光图书馆')
    for title, total in [('Python 编程入门', 3), ('算法图解', 2), ('数据结构入门', 1)]:
        library.add_book(title, total)

    library.borrow_book('小王', 'Python 编程入门')
    library.borrow_book('小李', 'Python 编程入门')
    library.borrow_book('小张', '算法图解')
    library.borrow_book('小李', '数据结构入门')
    library.return_book('小张', '算法图解')
    library.borrow_book('小李', '算法图解')
    library.print_report()


if __name__ == '__main__':
    main()
