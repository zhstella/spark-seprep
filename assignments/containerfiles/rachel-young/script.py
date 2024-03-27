import random

def book_rec():
    books = [
        ("The Hobbit by J.R.R Tolkein", "fantasy "),
        ("Emma by Jane Austen", "comedy of manners "),
        ("Harry Potter and The Order of the Phoenix by J.K. Rowling", "fantasy middle grade "),
        ("Gone Girl by Gillian Flynn", "thriller "),
        ("The Secret History by Donna Tartt", "mystery"),
        ("Norwegian Wood by Haruki Murakami", "literary fiction"),
        ("Stay True by Hua Hsu", "memoir"),
        ("Normal People by Sally Rooney", "literary fiction"),
        ("Crying in H Mart by Michelle Zauner", "memoir"),
        ("The Outsiders by S.E. Hinton", "young adult")
    ]
    return random.choice(books)

rec = book_rec()
print("You should checkout", rec[0], "It's a ", rec[1], "novel")