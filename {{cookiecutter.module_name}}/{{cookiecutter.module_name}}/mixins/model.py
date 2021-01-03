import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelMixin(models.Model):
    class Meta:
        abstract = True

    external_id = models.UUIDField(
        verbose_name=_("External Id"),
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        null=False,
        blank=False,
        help_text=_("Creation datetime"),
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        null=True,
        blank=False,
        help_text=_("Update datetime"),
    )

    def __str__(self):  # pragma: no cover
        # TODO: Implement test after another model creation
        return f"{self.__class__.__name__}<{self.pk}>"

    def __repr__(self):
        return f"{self.__class__.__name__}<{self}>"
