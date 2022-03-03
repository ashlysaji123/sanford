from django.contrib import messages
from django.utils.translation import ngettext


def mark_deleted(self, request, queryset):
    updated = queryset.update(is_deleted=True)
    self.message_user(
        request,
        ngettext(
            "%d item was successfully marked as deleted.",
            "%d items were successfully marked as deleted.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


def mark_active(self, request, queryset):
    updated = queryset.update(is_deleted=False)
    self.message_user(
        request,
        ngettext(
            "%d item was successfully recovered as active item.",
            "%d items were successfully recovered as active item.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )
