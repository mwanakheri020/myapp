from django.db import models # type: ignore

class House(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"Booking for {self.user} on {self.date}"

class Review(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.user} - Rating: {self.rating}"

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords for security

    def __str__(self):
        return self.username