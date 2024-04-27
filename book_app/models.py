from django.db import models


class Category(models.Model):
    """
    A simple book category instance.

    Attributes:
        name (str): The name of the category.
        created_at (datetime): The date and time when the category was created.
        updated_at (datetime): The date and time when the category was last updated.
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name





class Book(models.Model):
    """
    A simple book instance.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        no_of_pages (int): The number of pages in the book.
        description (str): A brief description of the book.
        category (Category): The category of the book, a foreign key to the Category model.
        created_at (datetime): The date and time when the book was created.
        updated_at (datetime): The date and time when the book was last updated.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    no_of_pages = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: The title of the book.
        """
        return self.title

