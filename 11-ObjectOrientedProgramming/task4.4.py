from ebook import EBook

book = EBook("Dune", "Frank Herbert", 412)
book.open()
book.show_status()
book.next_page()
book.next_page()
book.show_status()
book.close()
book.next_page()    # nie powinno dzialac - ksiazka zamknieta