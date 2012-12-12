from os import path

from filebrowser import signals
from filebrowser.fields import FileObject

from lakaxita.attachments.models import InternalAttachment


def create_attachment(sender, **kwargs):
    fileobj = kwargs['file']
    if InternalAttachment.objects.filter(file=fileobj).count() == 0:
        attachment = InternalAttachment(file=fileobj)
        attachment.save()
signals.filebrowser_post_upload.connect(create_attachment)


def rename_attachment_file(sender, **kwargs):
    old_file = FileObject(kwargs['path'])
    new_file = FileObject(path.join(path.dirname(old_file.path), kwargs['new_name']))
    try:
        attachment = InternalAttachment.objects.get(file=old_file)
    except InternalAttachment.DoesNotExist:
        attachment = InternalAttachment(file=new_file)
    else:
        attachment.file = new_file
    finally:
        attachment.save()
signals.filebrowser_post_rename.connect(rename_attachment_file)


def delete_attachment(sender, **kwargs):
    fileobj = FileObject(kwargs['path'])
    try:
        attachment = InternalAttachment.objects.get(file=fileobj)
    except InternalAttachment.DoesNotExist:
        pass
    else:
        attachment.delete()
signals.filebrowser_pre_delete.connect(delete_attachment)
