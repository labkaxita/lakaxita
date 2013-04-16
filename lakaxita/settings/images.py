from imagekit.processors import ResizeToFill, ResizeToFit


stretched_options = {
        'processors': [ResizeToFill(width=300, height=200)],
        'format': 'JPEG',
        'options': {'quality': 60},
        }

scaled_options = {
        'processors': [ResizeToFit(width=300)],
        'format': 'JPEG',
        'options': {'quality': 60},
        }
