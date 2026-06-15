#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI версия AI Foto для обработки фотографий из командной строки
"""

import argparse
import sys
from pathlib import Path
from core.image_processor import ImageProcessor
from core.enhancement import EnhancementEngine

def main():
    parser = argparse.ArgumentParser(
        description='AI Foto - Улучшение качества фотографий',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python process_image.py --input photo.jpg --output result.jpg --quality high
  python process_image.py -i dark_photo.jpg -o output.jpg -q fast
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Путь к входному файлу (jpg, jpeg, png)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output/result.jpg',
        help='Путь к выходному файлу (по умолчанию: output/result.jpg)'
    )
    
    parser.add_argument(
        '-q', '--quality',
        choices=['fast', 'medium', 'high'],
        default='medium',
        help='Качество обработки (по умолчанию: medium)'
    )
    
    parser.add_argument(
        '--no-deblur',
        action='store_true',
        help='Пропустить удаление размытости'
    )
    
    parser.add_argument(
        '--no-denoise',
        action='store_true',
        help='Пропустить удаление шума'
    )
    
    parser.add_argument(
        '--no-shadow',
        action='store_true',
        help='Пропустить улучшение теней'
    )
    
    args = parser.parse_args()
    
    # Проверка входного файла
    if not Path(args.input).exists():
        print(f"❌ Файл не найден: {args.input}")
        sys.exit(1)
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           🎨 AI Foto - Обработка фотографии 🎨           ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    try:
        processor = ImageProcessor(quality=args.quality)
        engine = EnhancementEngine()
        
        print(f"📷 Загрузка изображения: {args.input}")
        image = processor.load_image(args.input)
        print(f"✓ Размер: {image.size}")
        
        print(f"\n🔧 Обработка (качество: {args.quality})...\n")
        
        if not args.no_deblur:
            print("🔨 Удаление размытости...")
            image = processor.remove_blur(image)
        
        if not args.no_shadow:
            print("🌙 Улучшение тёмных областей...")
            image = engine.fix_dark_image(image)
        
        if not args.no_denoise:
            print("🔊 Удаление шума...")
            image = processor.reduce_noise(image)
        
        print("📊 Улучшение контраста...")
        image = processor.enhance_contrast(image, factor=1.4)
        
        print("☀️ Улучшение яркости...")
        image = processor.enhance_brightness(image, factor=1.15)
        
        print("🎨 Улучшение цвета...")
        image = processor.enhance_color(image, factor=1.25)
        
        if args.quality == 'high':
            print("⬆️ Увеличение разрешения (2x)...")
            image = processor.upscale_image(image, scale=2)
        
        print(f"\n💾 Сохранение результата: {args.output}")
        processor.save_image(image, args.output)
        
        print(f"✅ Готово! Результат сохранён в: {args.output}")
        print(f"📏 Итоговый размер: {image.size}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
