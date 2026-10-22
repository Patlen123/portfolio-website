import os.path

from django.db import models

from root_app import settings


# Apparently it's a security risk to just use the original filename, so we will make one here based on position
def pic_path(instance, filename):
    position = instance.position
    extension = os.path.splitext(filename)[-1].lower()
    new_filename = f"{position}{extension}"
    return os.path.join('img/committee_pics', new_filename)


def about_image_path(instance, filename):
    position = 0
    try:
        position = AboutImage.objects.count()
    except Exception:
        position = 0

    extension = os.path.splitext(filename)[-1].lower()
    new_filename = f"{position}{extension}"
    return os.path.join(f"img/about_images/{new_filename}")


# Positions are split up like this based on section, because of how the layout works
# Might not be an ideal way to do this, but I really couldn't think of any better way
class ExecMember(models.Model):
    POSITION_CHOICES = [
        ('president', 'President'),
        ('vpsec', 'Vice-President Secretary'),
        ('vptreasurer', 'Vice-President Treasurer')
    ]

    name = models.CharField(max_length=255, default="Vacant")
    pronouns = models.CharField(max_length=255, default="", blank=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES, unique=True, blank=True)
    picture = models.ImageField(upload_to=pic_path,
                                default="/img/committee_pics/vacant.png")
    discord_name = models.CharField(max_length=255, default="", blank=True)
    about_me = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class IdentityMember(models.Model):
    POSITION_CHOICES = [
        ('gaymens', 'Gay & MLM Officer'),
        ('lesbian', 'Lesbian & WLW Officer'),
        ('bi', 'Bi/Pan Officer'),
        ('trans', 'Trans Officer'),
        ('nonbinary', 'Non-Binary Officer'),
        ('acearo', 'Ace/Aro Officer'),
        ('postmat', 'PostMat Officer'),
        ('international', 'International Officer'),
        ('poc', 'PoC Officer'),
        ('disability', 'Disability Officer'),
        ('firstyear', "First Year Officer"),
    ]

    name = models.CharField(max_length=255, default="Vacant")
    pronouns = models.CharField(max_length=255, default="", blank=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES, unique=True, blank=True)
    picture = models.ImageField(upload_to=pic_path,
                                default="/img/committee_pics/vacant.png")
    discord_name = models.CharField(max_length=255, default="", blank=True)
    about_me = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class OtherMember(models.Model):
    POSITION_CHOICES = [
        ('campaigns', 'Campaigns Officer'),
        ('welfare', 'Welfare Officer'),
        ('events', 'Events Officer'),
        ('comtech', 'Communications & Technology Officer'),
        # Add the rest of the positions here
    ]

    name = models.CharField(max_length=255, default="Vacant")
    pronouns = models.CharField(max_length=255, default="", blank=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES, unique=True, blank=True)
    picture = models.ImageField(upload_to=pic_path,
                                default="/img/committee_pics/vacant.png")
    discord_name = models.CharField(max_length=255, default="", blank=True)
    about_me = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class AboutImage(models.Model):
    name = models.CharField(max_length=100)
    alt_text = models.TextField()
    image = models.ImageField(upload_to=about_image_path)

    def __str__(self):
        return self.name + ": " + str(self.image)
