from django.db import models
from mainConfig.models.mixin import TimeStampMixin


class ListInput(TimeStampMixin):
    profile = models.ForeignKey(
        "accounts.Profile",on_delete=models.CASCADE,null=True
    )
    input_values = models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return str(self.profile)

    class Meta:
        verbose_name_plural = "List Input By Profile"