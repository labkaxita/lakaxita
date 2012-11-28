from django.views.generic import RedirectView, DetailView
from django.shortcuts import get_object_or_404

from lakaxita.attachments.models import Attachment, File


class AttachmentDetail(DetailView):
    model = Attachment
    template_name = 'attachments/attachment_detail.yammy'
    context_object_name = 'attachment'


class FileRedirect(RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        file_obj = get_object_or_404(File, pk=self.kwargs['pk'])
        return file_obj.file.url
