# AI Foto - Advanced Photo Enhancement Tool

Программа для восстановления и улучшения качества низкокачественных, размытых и тёмных фотографий с использованием нейросетей и компьютерного зрения.

## Функциональность

✅ **Удаление размытости** (Motion deblur, Gaussian blur removal)
✅ **Повышение разрешения** (Upscaling 4x через Real-ESRGAN)
✅ **Удаление шума** (Advanced denoising)
✅ **Улучшение тёмных областей** (Shadow enhancement)
✅ **Коррекция контраста и яркости** (CLAHE - Contrast Limited Adaptive Histogram Equalization)
✅ **Восстановление деталей** (Detail enhancement)
✅ **Пакетная обработка** (Batch processing)

## Требования

- Python 3.8+
- CUDA 11.8+ (опционально, для ускорения GPU)
- 4GB RAM минимум
- 2GB свободного места для моделей

## Установка

```bash
git clone https://github.com/mk-sudo-design/ai_foto.git
cd ai_foto
pip install -r requirements.txt
```

## Использование

### Через GUI

```bash
python main.py
```

### Через командную строку

```bash
python process_image.py --input input.jpg --output output.jpg --quality high
```

## Параметры качества

- `fast` - Быстрая обработка (~1-2 минуты)
- `medium` - Сбалансированная обработка (~3 минуты)
- `high` - Максимальное качество (~5 минут)

## Структура проекта

```
ai_foto/
├── main.py                 # GUI приложение
├── process_image.py        # CLI обработка
├── core/
│   ├── image_processor.py  # Основной класс обработки
│   ├── deblur.py          # Удаление размытости
│   ├── denoise.py         # Удаление шума
│   ├── upscaler.py        # Повышение разрешения
│   └── enhancement.py     # Улучшение качества
├── ui/
│   ├── main_window.py     # Главное окно
│   ├── worker.py          # Рабочий поток
│   └── styles.qss         # Стили Qt
└── models/                # Сохранённые модели
```

## Лицензия

MIT License
