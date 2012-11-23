from markdown import markdown
from adminfiles.utils import render_uploads


def markup_filter(markup, **kwargs):
    return markdown(render_uploads(markup), **kwargs)
