from django.db import models  
   
class Author(models.Model):  
    full_name = models.TextField(verbose_name=("Имя автора"))  
    birth_year = models.SmallIntegerField(null=True, verbose_name=("Год рождения"))  
    country = models.CharField(max_length=50, null=True, verbose_name=("Страна")) 
    
    def __str__ (self):
        return self.full_name

class Publishing(models.Model): 
    name = models.TextField(verbose_name=("Название"))   
    year_foundation = models.SmallIntegerField(verbose_name=("Год основания")) 
    
    def __str__ (self):
        return self.name

#  модель друга
class Friend(models.Model):
    FIO = models.CharField(max_length=100, verbose_name=("ФИО Друга"))
    PhoneNumber = models.CharField(max_length=20, verbose_name=("Номер телефона"))

    def __str__(self):
        return self.FIO

class Book(models.Model):  
    ISBN = models.CharField(max_length=13, null=True, verbose_name=("Международный стандартный книжный номер"))  
    description = models.TextField(verbose_name=("Описание"))  
    year_release = models.SmallIntegerField(verbose_name=("Дата выпуска"))  
    copy_count = models.IntegerField(default=1, verbose_name=("Количесвто копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=("Цена")) 
    title = models.CharField(max_length=128, verbose_name=("Название книги"))
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE, related_name='book_publishing', null=True, blank=True, verbose_name=("Издательство"))
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
        verbose_name=('Авторы'),
    )
    friend = models.ForeignKey(Friend, related_name="friend_books", related_query_name="friend_book",
                                        on_delete=models.SET_NULL, null=True, blank=True, verbose_name=("Одолжил друг"))
    cover = models.ImageField(upload_to='user_cover/%Y/%m/%d', blank=True, verbose_name='Обложка книги') # обложка книги

    def __str__(self):
        return self.title

# вдохновитель inspirer для автора author при написании книги book
class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
        null=True,
    )
    