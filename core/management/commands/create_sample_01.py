from django.core.management.base import BaseCommand
from core.models import Book, Author, Category


class Command(BaseCommand):
    help = "Add Sample Data"

    def handle(self, *args, **options):
        author = Author.objects.create(name="김정진")
        category = Category.objects.create(name="IT")
        book1 = Book.objects.create(title="Django Ninja 로 익혀보는 계층형 설계", isbn="XX-XXXX-XXX0", published_date="2025-09-10", pages=350)
        book1.authors.add(author)
        book1.category = category
        book2 = Book.objects.create(title="Django Ninja 로 익혀보는 계층형 설계 2탄", isbn="XX-XXXX-XXX1", published_date="2026-09-10", pages=350)
        book2.authors.add(author)
        book2.category = category