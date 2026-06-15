import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from pathlib import Path

class ImageProcessor:
    """Основной класс для обработки изображений"""
    
    def __init__(self, quality='medium'):
        """
        Args:
            quality: 'fast', 'medium', 'high'
        """
        self.quality = quality
        self.iterations = {'fast': 1, 'medium': 2, 'high': 3}.get(quality, 2)
    
    def load_image(self, image_path: str) -> Image.Image:
        """Загрузить изображение"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл не найден: {image_path}")
        return Image.open(image_path).convert('RGB')
    
    def save_image(self, image: Image.Image, output_path: str, quality: int = 95):
        """Сохранить изображение"""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        image.save(output_path, 'JPEG', quality=quality)
    
    def remove_blur(self, image: Image.Image) -> Image.Image:
        """Удалить размытость с помощью фильтра резкости"""
        for _ in range(self.iterations):
            image = image.filter(ImageFilter.SHARPEN)
        return image
    
    def enhance_shadows(self, image: Image.Image) -> Image.Image:
        """Улучшить тёмные области (поднять тени)"""
        img_array = np.array(image, dtype=np.float32)
        
        # Применяем CLAHE-подобный алгоритм
        for channel in range(3):
            channel_data = img_array[:, :, channel]
            # Поднимаем тёмные пиксели
            mask = channel_data < 128
            channel_data[mask] = channel_data[mask] * 1.3
            img_array[:, :, channel] = np.clip(channel_data, 0, 255)
        
        return Image.fromarray(np.uint8(img_array))
    
    def reduce_noise(self, image: Image.Image) -> Image.Image:
        """Удалить шум (денойзинг)"""
        # Применяем медианный фильтр для удаления шума
        for _ in range(self.iterations):
            image = image.filter(ImageFilter.MedianFilter(size=3))
        return image
    
    def enhance_contrast(self, image: Image.Image, factor: float = 1.3) -> Image.Image:
        """Улучшить контраст"""
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)
    
    def enhance_brightness(self, image: Image.Image, factor: float = 1.1) -> Image.Image:
        """Улучшить яркость"""
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)
    
    def enhance_color(self, image: Image.Image, factor: float = 1.2) -> Image.Image:
        """Улучшить насыщенность цвета"""
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(factor)
    
    def upscale_image(self, image: Image.Image, scale: int = 2) -> Image.Image:
        """Увеличить разрешение изображения"""
        width, height = image.size
        new_size = (width * scale, height * scale)
        # Используем высококачественную интерполяцию
        return image.resize(new_size, Image.Resampling.LANCZOS)
    
    def process_full(self, image_path: str, output_path: str) -> bool:
        """Полная обработка изображения"""
        try:
            print(f"📷 Загрузка изображения: {image_path}")
            image = self.load_image(image_path)
            original_size = image.size
            
            print("🔧 Удаление размытости...")
            image = self.remove_blur(image)
            
            print("🌙 Улучшение тёмных областей...")
            image = self.enhance_shadows(image)
            
            print("🔊 Удаление шума...")
            image = self.reduce_noise(image)
            
            print("📊 Улучшение контраста...")
            image = self.enhance_contrast(image, factor=1.4)
            
            print("☀️ Улучшение яркости...")
            image = self.enhance_brightness(image, factor=1.15)
            
            print("🎨 Улучшение цвета...")
            image = self.enhance_color(image, factor=1.25)
            
            if self.quality == 'high':
                print("⬆️ Увеличение разрешения (2x)...")
                image = self.upscale_image(image, scale=2)
            
            print(f"💾 Сохранение: {output_path}")
            self.save_image(image, output_path)
            
            final_size = image.size
            print(f"✅ Готово! Размер: {original_size} → {final_size}")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            return False
