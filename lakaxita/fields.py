from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class ThumbnailField(ImageSpecField):
    def __init__(self, processors=None, format=None, options=None,
            source=None, cachefile_storage=None, autoconvert=None,
            cachefile_backend=None, cachefile_strategy=None, spec=None,
            id=None):

        processors = [ResizeToFill(300, 200)]
        format = 'JPEG'
        options = {'quality': 60}

        super(ThumbnailField, self).__init__(processors=processors, 
                format=format, options=options, source=source, 
                cachefile_storage=cachefile_storage, autoconvert=autoconvert,
                cachefile_backend=cachefile_backend, 
                cachefile_strategy=cachefile_strategy, spec=spec, id=id)


class SquareThumbnailField(ThumbnailField):
    def __init__(self, processors=None, format=None, options=None,
            source=None, cachefile_storage=None, autoconvert=None,
            cachefile_backend=None, cachefile_strategy=None, spec=None,
            id=None):

        processors = [ResizeToFill(300, 300)]

        super(ThumbnailField, self).__init__(processors=processors, 
                format=format, options=options, source=source, 
                cachefile_storage=cachefile_storage, autoconvert=autoconvert,
                cachefile_backend=cachefile_backend, 
                cachefile_strategy=cachefile_strategy, spec=spec, id=id)
