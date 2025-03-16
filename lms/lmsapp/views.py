from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from .models import *

def home(request):
    return render(request,'home.html')
def introduction(request):
    return render(request,'introduction.html')
def wzb1(request):
    return render(request,'wzb1.html')
def wzb2(request):
    return render(request,'wzb2.html')
def wzb3(request):
    return render(request,'wzb3.html')
def book(request):
    return render(request,'book.html')

#GayPT
def to_borrow(request):
    search_query_name = request.GET.get('query_borrow_name', '')  # Get borrower name
    search_query_password = request.GET.get('query_borrow_password', '')
    search_query_isbn = request.GET.get('query_borrow_isbn', '')
    book = Book.objects.filter(book_isbn__exact=search_query_isbn).first()  # Get book instance
    reader = Reader.objects.filter(reader_name__exact=search_query_name, reader_password__exact=search_query_password, active=True).first()  # Get active reader instance

    if book:  # Check if the book exists
        if book.book_stock_number > 0:  # Check if book is available
            if reader:  # Check if the reader exists and is active
                # Split the borrower names into a list
                if book.book_borrower_name:
                    book_borrowers = book.book_borrower_name.split(', ')
                else:
                    book_borrowers = []

                # Check if the reader has already borrowed the book
                if search_query_name in book_borrowers:
                    context = {'to_borrow_response': "You can't borrow the same book twice."}
                    return render(request, 'home.html', context)
                else:
                    # Append the borrower's name
                    if book.book_borrower_name:
                        book.book_borrower_name += ', ' + search_query_name
                    else:
                        book.book_borrower_name = search_query_name

                    # Update stock and save changes
                    book.book_stock_number -= 1
                    book.save()  # Save changes to the database

                    # Record the borrowing history
                    Borrowed_history.objects.create(
                        history='Book:' + book.book_title + '-' + search_query_isbn + ' Reader:' + search_query_name)

                    context = {'to_borrow_response': 'Borrow successful.'}
                    return render(request, 'home.html', context)
            else:
                context = {'to_borrow_response': "Invalid account or account is inactive."}
                return render(request, 'home.html', context)
        else:
            context = {'to_borrow_response': "Book unavailable."}
            return render(request, 'home.html', context)
    else:
        context = {'to_borrow_response': "Incorrect ISBN."}
        return render(request, 'home.html', context)
#wzb1
def borrow_wzb1(request):
    search_query_name = request.GET.get('wzb1_borrow_name', '')  # Get borrower name
    search_query_password = request.GET.get('wzb1_borrow_password', '')
    search_query_isbn = str(9787214269973)
    book = Book.objects.filter(book_isbn__exact=search_query_isbn).first()  # Get book instance
    reader = Reader.objects.filter(reader_name__exact=search_query_name, reader_password__exact=search_query_password, active=True).first()  # Get active reader instance

    if book.book_stock_number > 0:  # Check if book is available
        if reader:  # Check if the reader exists and is active
            # Split the borrower names into a list
            if book.book_borrower_name:
                book_borrowers = book.book_borrower_name.split(', ')
            else:
                book_borrowers = []

            # Check if the reader has already borrowed the book
            if search_query_name in book_borrowers:
                context = {'to_borrow_response': "You can't borrow the same book twice."}
                return render(request, 'wzb1.html', context)
            else:
                # Append the borrower's name
                if book.book_borrower_name:
                    book.book_borrower_name += ', ' + search_query_name
                else:
                    book.book_borrower_name = search_query_name

                # Update stock and save changes
                book.book_stock_number -= 1
                book.save()  # Save changes to the database

                # Record the borrowing history
                Borrowed_history.objects.create(
                    history='Book:' + book.book_title + '-' + search_query_isbn + ' Reader:' + search_query_name)

                context = {'to_borrow_response': 'Borrow successful.'}
                return render(request, 'wzb1.html', context)
        else:
            context = {'to_borrow_response': "Invalid account or account is inactive."}
            return render(request, 'wzb1.html', context)
    else:
        context = {'to_borrow_response': "Book unavailable."}
        return render(request, 'wzb1.html', context)
#wzb2
def borrow_wzb2(request):
    search_query_name = request.GET.get('wzb2_borrow_name', '')  # Get borrower name
    search_query_password = request.GET.get('wzb2_borrow_password', '')
    search_query_isbn = str(9787214269980)
    book = Book.objects.filter(book_isbn__exact=search_query_isbn).first()  # Get book instance
    reader = Reader.objects.filter(reader_name__exact=search_query_name, reader_password__exact=search_query_password, active=True).first()  # Get active reader instance

    if book.book_stock_number > 0:  # Check if book is available
        if reader:  # Check if the reader exists and is active
            # Split the borrower names into a list
            if book.book_borrower_name:
                book_borrowers = book.book_borrower_name.split(', ')
            else:
                book_borrowers = []

            # Check if the reader has already borrowed the book
            if search_query_name in book_borrowers:
                context = {'to_borrow_response': "You can't borrow the same book twice."}
                return render(request,  'wzb2.html', context)
            else:
                # Append the borrower's name
                if book.book_borrower_name:
                    book.book_borrower_name += ', ' + search_query_name
                else:
                    book.book_borrower_name = search_query_name

                # Update stock and save changes
                book.book_stock_number -= 1
                book.save()  # Save changes to the database

                # Record the borrowing history
                Borrowed_history.objects.create(
                    history='Book:' + book.book_title + '-' + search_query_isbn + ' Reader:' + search_query_name)

                context = {'to_borrow_response': 'Borrow successful.'}
                return render(request,'wzb2.html', context)
        else:
            context = {'to_borrow_response': "Invalid account or account is inactive."}
            return render(request, 'wzb2.html', context)
    else:
        context = {'to_borrow_response': "Book unavailable."}
        return render(request, 'wzb2.html', context)

#wzb3
def borrow_wzb3(request):
    search_query_name = request.GET.get('wzb3_borrow_name', '')  # Get borrower name
    search_query_password = request.GET.get('wzb3_borrow_password', '')
    search_query_isbn = str(9787214269966)
    book = Book.objects.filter(book_isbn__exact=search_query_isbn).first()  # Get book instance
    reader = Reader.objects.filter(reader_name__exact=search_query_name, reader_password__exact=search_query_password, active=True).first()  # Get active reader instance

    if book.book_stock_number > 0:  # Check if book is available
        if reader:  # Check if the reader exists and is active
            # Split the borrower names into a list
            if book.book_borrower_name:
                book_borrowers = book.book_borrower_name.split(', ')
            else:
                book_borrowers = []

            # Check if the reader has already borrowed the book
            if search_query_name in book_borrowers:
                context = {'to_borrow_response': "You can't borrow the same book twice."}
                return render(request, 'wzb3.html', context)
            else:
                # Append the borrower's name
                if book.book_borrower_name:
                    book.book_borrower_name += ', ' + search_query_name
                else:
                    book.book_borrower_name = search_query_name

                # Update stock and save changes
                book.book_stock_number -= 1
                book.save()  # Save changes to the database

                # Record the borrowing history
                Borrowed_history.objects.create(
                    history='Book:' + book.book_title + '-' + search_query_isbn + ' Reader:' + search_query_name)

                context = {'to_borrow_response': 'Borrow successful.'}
                return render(request, 'wzb3.html', context)
        else:
            context = {'to_borrow_response': "Invalid account or account is inactive."}
            return render(request, 'wzb3.html', context)
    else:
        context = {'to_borrow_response': "Book unavailable."}
        return render(request, 'wzb3.html', context)

def to_return(request):
    search_query_name = request.GET.get('query_return_name', '')  # Get borrower name
    search_query_isbn = request.GET.get('query_return_isbn', '')  # Get book ISBN
    search_query_password = request.GET.get('query_return_password', '')
    book = Book.objects.filter(book_isbn__exact=search_query_isbn).first()  # Get book instance
    reader = Reader.objects.filter(reader_name__exact=search_query_name, reader_password__exact=search_query_password, active=True).first()  # Get reader instance

    if book:  # Check if the book exists
        if reader:
            if search_query_name in book.book_borrower_name.split(', '):  # Check if the book is borrowed by the reader
                borrowers = book.book_borrower_name.split(', ')
                borrowers.remove(search_query_name)  # Remove the borrower's name
                book.book_borrower_name = ', '.join(borrowers)  # Join the remaining names
                book.book_stock_number += 1
                book.save()  # Save changes
                context = {'to_return_response': 'Return successful.'}
                return render(request, 'home.html', context)
            else:
                context = {'to_return_response': "Return unavailable."}
                return render(request, 'home.html', context)
        else:
            context = {'to_return_response': "Invalid account or account is inactive."}
            return render(request, 'home.html', context)
    else:
        context = {'to_return_response': "Incorrect ISBN."}
        return render(request, 'home.html', context)
