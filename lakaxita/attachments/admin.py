from django.contrib import admin
from django.shortcuts import redirect

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from lakaxita.attachments.models import (Attachment,
                                        ExternalAttachment, 
                                        InternalAttachment,
                                        )


class ExternalAttachmentAdminChild(PolymorphicChildModelAdmin):
    base_model = ExternalAttachment


class InternalAttachmentAdminChild(PolymorphicChildModelAdmin):
    base_model = InternalAttachment
    exclude = ['oembed']

    def add_view(self, request, *args, **kwargs):
        return redirect('filebrowser:fb_upload', permanent=True)

    def change_view(self, request, object_id, *args, **kwargs):
        return redirect('filebrowser:fb_detail', args=(object_id,), 
                permanent=True)
        
    def delete_view(self, request, object_id, *args, **kwargs):
        return redirect('filebrowser:fb_delete', args=(object_id,), 
                permanent=True)


class AttachmentAdmin(PolymorphicParentModelAdmin):
    base_model = Attachment
    child_models = (
            (ExternalAttachment, ExternalAttachmentAdminChild),
            (InternalAttachment, InternalAttachmentAdminChild),
            )


class ExternalAttachmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(ExternalAttachment, ExternalAttachmentAdmin)
