from django.db import models

class PersonalDetail(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bio = models.TextField()
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='family_photos/')
    occupation = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
        return f"{self.relation} - {self.name}"  # ✅ 4 spaces!
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200)
    maps_link = models.URLField()
    photo = models.ImageField(upload_to='education_photos/')

    def __str__(self):
        return f"{self.degree} at {self.institution}"
class EducationImage(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='education_gallery/')

    def __str__(self):
        return f"Image for {self.education.institution}"
class PersonalSkill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()  # Use web images for now

    def __str__(self):
        return self.title
