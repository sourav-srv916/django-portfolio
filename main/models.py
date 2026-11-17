from django.db import models, transaction

# Create your models here.


class Profile(models.Model):

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=150)

    introduction = models.TextField()

    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=150)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    about = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100, blank=True)

    level = models.CharField(max_length=50, blank=True)

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'id']

    def save(self, *args, **kwargs):

        if self._state.adding and self.display_order == 0:

            last_order = type(self).objects.aggregate(
                models.Max('display_order')
            )['display_order__max'] or 0

            self.display_order = last_order + 1

        super().save(*args, **kwargs)


class Experience(models.Model):

    job_title = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    start_date = models.CharField(max_length=50)

    end_date = models.CharField(max_length=50)

    description = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.job_title} - {self.company}"

    class Meta:
        ordering = ['display_order', 'id']

    def save(self, *args, **kwargs):

        if self._state.adding and self.display_order == 0:

            with transaction.atomic():

                type(self).objects.all().update(
                    display_order=models.F('display_order') + 1
                )

                super().save(*args, **kwargs)

            return

        super().save(*args, **kwargs)


class Project(models.Model):

    name = models.CharField(max_length=150)

    description = models.TextField()

    technologies = models.CharField(max_length=300)

    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'id']

    def save(self, *args, **kwargs):

        if self._state.adding and self.display_order == 0:

            last_order = type(self).objects.aggregate(
                models.Max('display_order')
            )['display_order__max'] or 0

            self.display_order = last_order + 1

        super().save(*args, **kwargs)


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']