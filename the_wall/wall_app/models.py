from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not postData["first_name"]:
            errors["first_name"] = "Please enter your first name"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if not postData["last_name"]:
            errors["last_name"] = "Please enter your last name"
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        if not postData["password"]:
            errors["password"] = "Please enter password"
        elif postData["password"]  != postData["con-password"]:
            errors["password"] = "password don't match"
        elif len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name = "messages", blank=True, null=True, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_id =models.ForeignKey(Message, related_name = "comments", blank=True, null=True, on_delete=models.CASCADE)
    user_id =models.ForeignKey(User, related_name = "comments", blank=True, null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)