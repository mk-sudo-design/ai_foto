# Config file for AI Foto

# Качество обработки по умолчанию
DEFAULT_QUALITY = 'medium'

# Параметры фильтров
FILTERS = {
    'fast': {
        'blur_iterations': 1,
        'noise_iterations': 1,
        'contrast_factor': 1.2,
        'brightness_factor': 1.1,
        'color_factor': 1.1,
        'upscale': False,
    },
    'medium': {
        'blur_iterations': 2,
        'noise_iterations': 2,
        'contrast_factor': 1.4,
        'brightness_factor': 1.15,
        'color_factor': 1.25,
        'upscale': False,
    },
    'high': {
        'blur_iterations': 3,
        'noise_iterations': 3,
        'contrast_factor': 1.5,
        'brightness_factor': 1.2,
        'color_factor': 1.3,
        'upscale': True,
        'upscale_factor': 2,
    }
}

# Качество сохранения JPEG
OUTPUT_QUALITY = 95

# Поддерживаемые форматы
SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png']

# Папка для результатов по умолчанию
DEFAULT_OUTPUT_DIR = 'output'
