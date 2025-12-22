from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.db import models

EXCLUDED_APPS = {"auth", "contenttypes", "sessions", "admin"}
EXCLUDED_FIELD_TYPES = (models.TextField, models.JSONField, models.BinaryField)
MAX_LIST_DISPLAY = 6


class BaseAutoAdmin(admin.ModelAdmin):
    pass


def get_list_display(model):
    fields = [
        f.name for f in model._meta.fields
        if not isinstance(f, EXCLUDED_FIELD_TYPES)
    ]

    return fields[:MAX_LIST_DISPLAY]


def auto_register_admin_models():
    for model in apps.get_models():
        try:
            if model._meta.abstract or model._meta.proxy:
                continue

            if model._meta.app_label in EXCLUDED_APPS:
                continue

            if hasattr(model, "Admin"):  # manual admin bor bo‘lsa
                continue

            admin_class = type(
                f"{model.__name__}AutoAdmin",
                (BaseAutoAdmin,),
                {
                    "list_display": get_list_display(model),
                    "search_fields": get_list_display(model),
                },
            )

            admin.site.register(model, admin_class)

        except AlreadyRegistered:
            pass
