from django.db import models

# Create your models here.
class Book ( models.Model):
    name= models.CharField(max_length = 40)
    price = models.IntegerField()
    author = models.CharField(max_length  =40)
    is_available = models.BooleanField(default =True)
    
    def __str__(self):
        return self.name

book1 = Book(1, "Victory City" ,1200, "Salman Rushdie",True)
book2 = Book(2, "The God of Small Things" ,2200, "Arundhati Roy",True)
book3 = Book(3, "Kavya Tulika" ,4100, "Usha Kiran Moodgal",True)
book4 = Book(4, "The Namesake" ,300, "Jhumpa Lahiri.",True)
book5 = Book(5, "Twisters" ,200, "Vanshika Mishra",False)
book6 = Book(6, "The Shadow line" ,1200, "Amitav Ghosh",True)
book7 = Book(7, "The Pride of T20 Cricket" ,1200, "Abhishek Kapoor",True)
book8 = Book(8, "A suitable boy" ,1200, "Vikram Seth",True)
book9 = Book(9, "Get the Hack" ,100, "Trek Rushdie",True)
book10 = Book(10, "Bank Scam" ,2400, "Salman Eudra",True)
book11= Book(11, "Vice City" ,1400, "Eric Fried",False)
book12 = Book(12, "Rich City" ,1200, "Tom holand",True)
book13= Book(13, "Former PM" ,300, "Ben Trump",True)
book14 = Book(14, "Opencase" ,1300, "Sal Opera",True)
book15= Book(15, "Victory cry" ,1500, "Otter Dal",True)
book16 = Book(16, "Uber crime" ,200, "Persal",True)
book17 = Book(17, "Hello Ride" ,400, "Quickey kelvin",True)
book18= Book(18, "Band Bomb" ,1200, "Keyl",True)
book19 = Book(19, "Out of park" ,400, "Reddy Rai",True)
book20= Book(20, "Numerly" ,300, "Tonny Dry",True)
book1.save()
book2.save()
book3.save()
book4.save()
book5.save()
book6.save()
book7.save()
book8.save()
book9.save()
book10.save()
book11.save()
book12.save()
book13.save()
book14.save()
book15.save()
book16.save()
book17.save()
book18.save()
book19.save()
book20.save()

