#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестирование модулей AI Foto
"""

import sys
from pathlib import Path

def test_imports():
    """Тестировать импорты всех модулей"""
    print("🧪 Тестирование импортов...\n")
    
    try:
        print("  ✓ Pillow...", end='')
        from PIL import Image, ImageEnhance, ImageFilter
        print(" OK")
        
        print("  ✓ NumPy...", end='')
        import numpy as np
        print(" OK")
        
        print("  ✓ PySimpleGUI...", end='')
        import PySimpleGUI as sg
        print(" OK")
        
        print("  ✓ core.image_processor...", end='')
        from core.image_processor import ImageProcessor
        print(" OK")
        
        print("  ✓ core.enhancement...", end='')
        from core.enhancement import EnhancementEngine
        print(" OK")
        
        print("  ✓ ui.gui...", end='')
        from ui.gui import PhotoEnhancerGUI
        print(" OK")
        
        print("\n✅ Все модули загружены успешно!\n")
        return True
        
    except ImportError as e:
        print(f"\n❌ Ошибка импорта: {e}")
        return False

def test_processor():
    """Тестировать обработчик изображений"""
    print("🧪 Тестирование ImageProcessor...\n")
    
    try:
        from core.image_processor import ImageProcessor
        
        processor = ImageProcessor(quality='fast')
        print("  ✓ ImageProcessor создан")
        
        # Создать тестовое изображение
        from PIL import Image
        test_img = Image.new('RGB', (100, 100), color='red')
        
        print("  ✓ Тестовое изображение создано")
        
        # Тестировать фильтры
        result = processor.remove_blur(test_img)
        print("  ✓ remove_blur() работает")
        
        result = processor.reduce_noise(test_img)
        print("  ✓ reduce_noise() работает")
        
        result = processor.enhance_contrast(test_img)
        print("  ✓ enhance_contrast() работает")
        
        result = processor.enhance_brightness(test_img)
        print("  ✓ enhance_brightness() работает")
        
        result = processor.enhance_color(test_img)
        print("  ✓ enhance_color() работает")
        
        result = processor.upscale_image(test_img)
        print("  ✓ upscale_image() работает")
        
        print("\n✅ ImageProcessor работает корректно!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        return False

def test_enhancement():
    """Тестировать движок улучшения"""
    print("🧪 Тестирование EnhancementEngine...\n")
    
    try:
        from core.enhancement import EnhancementEngine
        from PIL import Image
        
        engine = EnhancementEngine()
        test_img = Image.new('RGB', (100, 100), color='blue')
        
        print("  ✓ EnhancementEngine создан")
        
        result = engine.auto_enhance(test_img)
        print("  ✓ auto_enhance() работает")
        
        result = engine.enhance_details(test_img)
        print("  ✓ enhance_details() работает")
        
        result = engine.denoise_advanced(test_img)
        print("  ✓ denoise_advanced() работает")
        
        result = engine.fix_dark_image(test_img)
        print("  ✓ fix_dark_image() работает")
        
        result = engine.enhance_saturation(test_img)
        print("  ✓ enhance_saturation() работает")
        
        result = engine.enhance_sharpness(test_img)
        print("  ✓ enhance_sharpness() работает")
        
        print("\n✅ EnhancementEngine работает корректно!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        return False

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║              🧪 AI Foto - Тестирование                       ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    results.append(("Импорты", test_imports()))
    results.append(("ImageProcessor", test_processor()))
    results.append(("EnhancementEngine", test_enhancement()))
    
    print("\n" + "="*50)
    print("📊 Результаты тестирования:")
    print("="*50)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name:.<40} {status}")
        if not passed:
            all_passed = False
    
    print("="*50)
    
    if all_passed:
        print("\n✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Готово к использованию.\n")
        return 0
    else:
        print("\n❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ. Установите зависимости.\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
