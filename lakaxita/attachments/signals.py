from os import path

from filebrowser import signals

from lakaxita.attachments import models


def create_attachment(sender, **kwargs):
    path = kwargs['path']
    if File.objects.filter(file=path).count() == 0:
        attachment = File(file=path)
        attachment.save()
signals.filebrowser_post_upload.connect(create_attachment)


def rename_attachment_file(sender, **kwargs):
    old_path = kwargs['path']
    new_path = path.join(path.dirname(old_path), kwargs['new_name'])
    try:
        attachment = File.objects.get(file=path)
    except File.DoesNotExist:
        attachment = File(file=new_path)
    else:
        attachment.file = new_path
    finally:
        attachment.save()
signals.filebrowser_post_rename.connect(rename_attachment_file)


def delete_attachment(sender, **kwargs):
    path = kwargs['path']
    try:
        attachment = File.objects.get(file=path)
    except File.DoesNotExist:
        pass
    else:
        attachment.delete()
signals.filebrowser_pre_delete.connect(delete_attachment)
