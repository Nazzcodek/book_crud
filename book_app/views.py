from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Category model
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new category object based on the request data,
        performs creation, and returns a response with a success message and data.
        
        Parameters:
            self: the instance of the CategoryViewSet
            request: the request object
            *args: additional positional arguments
            **kwargs: additional keyword arguments
        
        Returns:
            Response: a response with a success message and the created data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': f"{serializer.data['name']} category has been created",
                         'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Updates a category object based on the provided request data.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response containing a message and the updated data.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': f"{serializer.data['name']} category has been updated",
                         'data': serializer.data})
    
    def destroy(self, request, *args, **kwargs):
        """
        Deletes a category object and returns a response with a message indicating the deletion.
        
        Parameters:
            self: the CategoryViewSet instance
            request: the request object
            *args: additional positional arguments
            **kwargs: additional keyword arguments
        
        Returns:
            Response: a response with a message indicating the successful deletion
        """
        category = self.get_object()
        message = f'{category.name} category has been deleted'
        category.delete()
        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)




class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new book object based on the request data, performs creation,
        and returns a response with a success message and data.
        
        Parameters:
            self: the instance of the BookViewSet
            request: the request object
            *args: additional positional arguments
            **kwargs: additional keyword arguments
        
        Returns:
            Response: a response with a success message and the created data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': f"{serializer.data['title']} has been created",
                         'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Updates a book object based on the provided request data.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response containing a message and the updated data.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': f"{serializer.data['title']} has been updated",
                         'data': serializer.data})
    
    def destroy(self, request, *args, **kwargs):
        """
        Deletes a book object and returns a response with a message indicating the deletion.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response with a message indicating the successful deletion.
        """
        book = self.get_object()
        message = f'{book.title} has been deleted'
        book.delete()
        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)