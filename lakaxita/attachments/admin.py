from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from lakaxita.attachments.models import MetaAttachment, Attachment, File


class AttachmentAdmin(PolymorphicChildModelAdmin):
    base_model = Attachment


class FileAdmin(AttachmentAdmin):
    exclude = ['oembed']


class AttachmentAdmin(PolymorphicParentModelAdmin):
    base_model = MetaAttachment
    child_models = (
            (Attachment, AttachmentAdmin),
            (File, FileAdmin),
            )

admin.site.register(Attachment, AttachmentAdmin)
