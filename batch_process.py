#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пакетная обработка фотографий
"""

import argparse
import sys
from pathlib import Path
from core.image_processor import ImageProcessor
from core.enhancement import EnhancementEngine
import time

def batch_process(input_dir, output_dir, quality='medium'):
    """
    Обработать все фото в папке
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"❌ Папка не найдена: {input_dir}")
        return
    
    # Создать папку для результатов
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Найти все изображения
    image_files = list(input_path.glob('*.jpg')) + \
                  list(input_path.glob('*.jpeg')) + \
                  list(input_path.glob('*.png'))
    
    if not image_files:
        print(f"❌ Нет изображений в папке: {input_dir}")
        return
    
    print(f"\n📁 Найдено изображений: {len(image_files)}")
    print(f"📊 Качество обработки: {quality}")
    print(f"💾 Результаты сохранятся в: {output_dir}\n")
    
    processor = ImageProcessor(quality=quality)
    engine = EnhancementEngine()
    
    start_time = time.time()
    successful = 0
    
    for idx, image_file in enumerate(image_files, 1):
        try:
            print(f"[{idx}/{len(image_files)}] Обработка: {image_file.name}... ", end='', flush=True)
            
            # Загрузить и обработать
            image = processor.load_image(str(image_file))
            
            image = processor.remove_blur(image)
            image = engine.fix_dark_image(image)
            image = processor.reduce_noise(image)
            image = processor.enhance_contrast(image, factor=1.4)
            image = processor.enhance_brightness(image, factor=1.15)
            image = processor.enhance_color(image, factor=1.25)
            
            # Сохранить
            output_file = output_path / f"enhanced_{image_file.stem}.jpg"
            processor.save_image(image, str(output_file))
            
            print("✅ Готово")
            successful += 1
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    elapsed_time = time.time() - start_time
    
    print(f"\n{'='*50}")
    print(f"✅ Успешно обработано: {successful}/{len(image_files)}")
    print(f"⏱️ Время обработки: {elapsed_time:.2f} сек")
    print(f"💾 Результаты в: {output_dir}")

def main():
    parser = argparse.ArgumentParser(
        description='Пакетная обработка фотографий',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python batch_process.py --input ./photos --output ./results
  python batch_process.py -i ./photos -o ./results -q high
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Папка с входными фото'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Папка для результатов'
    )
    
    parser.add_argument(
        '-q', '--quality',
        choices=['fast', 'medium', 'high'],
        default='medium',
        help='Качество обработки (по умолчанию: medium)'
    )
    
    args = parser.parse_args()
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     🎨 AI Foto - Пакетная обработка фотографий 🎨       ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    batch_process(args.input, args.output, args.quality)

if __name__ == '__main__':
    main()
