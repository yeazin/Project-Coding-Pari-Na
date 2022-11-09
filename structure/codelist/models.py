import uuid
from django.db import models
from mainConfig.models.mixin import TimeStampMixin



class ListInput(TimeStampMixin):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(
        "accounts.Profile",on_delete=models.CASCADE,null=True,
        related_name = "profile_input"
    )
    input_values = models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return str(self.profile)

    class Meta:
        verbose_name_plural = "List Input By Profile"