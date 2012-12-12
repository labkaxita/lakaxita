from django.contrib import admin
from django.shortcuts import redirect

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from lakaxita.attachments.models import (Attachment,
                                        ExternalAttachment, 
                                        InternalAttachment,
                                        )

class ExternalAttachmentAdmin(PolymorphicChildModelAdmin):
    base_model = ExternalAttachment


class InternalAttachmentAdmin(PolymorphicChildModelAdmin):
    base_model = InternalAttachment
    exclude = ['oembed']

    def add_view(self, request, *args, **kwargs):
        return redirect('/admin/filebrowser/upload/', permanent=True)

    def change_view(self, request, object_id, *args, **kwargs):
        return redirect('/admin/filebrowser/detail/', permanent=True)
        
    def delete_view(self, request, object_id, *args, **kwargs):
        return redirect('/admin/filebrowser/delete/', permanent=True)


class AttachmentAdmin(PolymorphicParentModelAdmin):
    base_model = Attachment
    child_models = (
            (ExternalAttachment, ExternalAttachmentAdmin),
            (InternalAttachment, InternalAttachmentAdmin),
            )

admin.site.register(Attachment, AttachmentAdmin)
