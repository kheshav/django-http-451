from django.db import models


class http451_URLS(models.Model):

    id = models.AutoField(primary_key=True)
    urls_to_block = models.CharField(max_length=300, null=False, unique=True)
    url_of_authority = models.CharField(max_length=100, null=False)
    censorship_reason = models.TextField(max_length=300, null=False)
    censorship_title = models.CharField(max_length=100, null=False)
    block_by_country = models.BooleanField(default=False)
    country_code = models.TextField(null=True, blank=True)
