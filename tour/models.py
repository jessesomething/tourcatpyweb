from django.db import models
from django.utils import timezone

class Event(models.Model):
    STATE_CHOICES = (
    (None, 'Select State'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),)

    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default='NA')
    venue = models.CharField(max_length=200)
    #todo add more info
    # tour_name = models.CharField(max_length=200)
    # other_bands_1 = models.CharField(max_length=100, blank=True)
    # other_bands_2 = models.CharField(max_length=100, blank=True)
    # other_bands_3 = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField(
    blank=True,
    default="DD/MM/YYYY HH:MM")

    def save_event(self):
        self.save()

    def __str__(self):
        return self.venue

class Merch(models.Model):
    TYPE_CHOICES = (
    ('T-Shirt','T-Shirt'),
    ('Sweatshirt','Sweatshirt'),
    ('Other Apparel','Other Apparel'),
    ('Record/LP/45','Record/LP/45'),
    ('CD','CD'),
    ('Cassette','Cassette'),
    ('Digital DL','Digital DL'),
    ('Pin/Button','Pin/Button'),
    ('Sticker','Sticker'),
    ('Poster','Poster'),
    ('Other','Other'),)

    name = models.CharField(max_length=100)
    merch_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='tshirt')
    price = models.IntegerField()
    quantity = models.IntegerField()

    def edit_merch(self, num):
        self.quantity = self.quantity + num

    def save_merch(self):
        # todo Doesn't currently check if item already exists
        # had some trouble trying to get this to work in here
        all_merch = Merch.objects.all()
        for merch in all_merch:
            print(merch.name)
            if merch.name == self.name and merch.merch_type == self.merch_type:
                merch.quantity = merch.quantity + self.quantity
            else:
                self.save()

    def __str__(self):
        return self.name
