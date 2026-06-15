from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

class EnhancementEngine:
    """Продвинутый движок для улучшения качества фото"""
    
    @staticmethod
    def auto_enhance(image: Image.Image) -> Image.Image:
        """Автоматическое улучшение изображения"""
        # Автоконтраст
        image = ImageOps.autocontrast(image, cutoff=5)
        
        # Автоуровни
        image = ImageOps.equalize(image)
        
        return image
    
    @staticmethod
    def enhance_details(image: Image.Image, strength: float = 1.5) -> Image.Image:
        """Восстановление деталей (детализация)"""
        img_array = np.array(image, dtype=np.float32) / 255.0
        
        # Применяем неразрушающее маскирование (Unsharp Mask)
        from PIL import ImageFilter
        blurred = np.array(image.filter(ImageFilter.GaussianBlur(radius=2)), dtype=np.float32) / 255.0
        
        mask = img_array - blurred
        enhanced = img_array + mask * strength
        enhanced = np.clip(enhanced, 0, 1)
        
        return Image.fromarray((enhanced * 255).astype(np.uint8))
    
    @staticmethod
    def denoise_advanced(image: Image.Image) -> Image.Image:
        """Продвинутое удаление шума"""
        # Применяем несколько фильтров для лучшего удаления шума
        image = image.filter(ImageFilter.MedianFilter(size=3))
        image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        image = image.filter(ImageFilter.MedianFilter(size=3))
        return image
    
    @staticmethod
    def fix_dark_image(image: Image.Image) -> Image.Image:
        """Исправить тёмное изображение (поднять экспозицию)"""
        img_array = np.array(image, dtype=np.float32)
        
        # Анализируем среднюю яркость
        brightness = np.mean(img_array)
        
        # Если изображение очень тёмное, поднимаем его
        if brightness < 100:
            factor = 150 / brightness
            img_array = img_array * factor
        elif brightness < 130:
            factor = 1.4
            img_array = img_array * factor
        
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(np.uint8(img_array))
    
    @staticmethod
    def enhance_saturation(image: Image.Image, factor: float = 1.3) -> Image.Image:
        """Улучшить насыщенность"""
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(factor)
    
    @staticmethod
    def enhance_sharpness(image: Image.Image, factor: float = 2.0) -> Image.Image:
        """Улучшить резкость"""
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(factor)
