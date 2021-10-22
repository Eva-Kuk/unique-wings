from django.db import models

# Create your models here.

SUBJECT_MENU = (
    ('general_query', 'General Query'),
    ('delivery_query', 'Delivery Query'),
    ('return_query', 'Return Query'),
    ('blog_contribution', 'Blog Contribution'),
    ('complaint', 'Complaint'),
)


class Contact(models.Model):
    """ Contact Model stores users queries in the backend for the admin """
    full_name = models.CharField(
        max_length=50, null=False,
        blank=False)
    email = models.EmailField(
        max_length=254, null=False,
        blank=False)
    subject = models.CharField(
        max_length=100, choices=SUBJECT_MENU,
        default='general_query',
        null=False, blank=False)
    date_posted = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.subject
