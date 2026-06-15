# AI Foto - Расширенное руководство

## 🎯 Быстрый старт

### Активация виртуального окружения

```bash
# macOS/Linux
source venv_ai_foto/bin/activate

# Windows
venv_ai_foto\Scripts\activate
```

### Запуск GUI приложения

```bash
python main.py
```

## 📖 Использование

### 1️⃣ GUI Интерфейс (Графический)

**Самый простой способ:**

```bash
python main.py
```

**Возможности:**
- 📁 Выбрать файл через окно выбора
- ⚙️ Выбрать уровень качества обработки
- ✅ Выбрать какие фильтры применять
- 💾 Сохранить в нужную папку

**Уровни качества:**
- **⚡ Быстро** (1-2 мин): базовая обработка
- **⚖️ Среднее** (2-3 мин): сбалансированная обработка (рекомендуется)
- **🏆 Высокое** (3-5 мин): максимальное качество + увеличение в 2x

### 2️⃣ Командная строка (CLI)

**Базовое использование:**

```bash
python process_image.py --input photo.jpg --output result.jpg
```

**С указанием качества:**

```bash
python process_image.py -i dark_photo.jpg -o output.jpg -q high
```

**Без определённых фильтров:**

```bash
python process_image.py -i photo.jpg -o result.jpg --no-denoise
python process_image.py -i photo.jpg -o result.jpg --no-deblur
python process_image.py -i photo.jpg -o result.jpg --no-shadow
```

**Все параметры:**

```
-i, --input        Входной файл (обязательно) [jpg, jpeg, png]
-o, --output       Выходной файл (по умолчанию: output/result.jpg)
-q, --quality      Качество: fast, medium, high (по умолчанию: medium)
--no-deblur        Пропустить удаление размытости
--no-denoise       Пропустить удаление шума
--no-shadow        Пропустить улучшение теней
```

### 3️⃣ Пакетная обработка (Batch)

**Обработать все фото в папке:**

```bash
python batch_process.py --input ./photos --output ./results
```

**С указанием качества:**

```bash
python batch_process.py -i ./photos -o ./results -q high
```

**Пример:**
```bash
# Создаём папку с фото
mkdir input_photos
cp *.jpg input_photos/

# Обработка всех фото
python batch_process.py -i input_photos -o output_photos -q medium
```

## 🔧 Что делает каждый фильтр

| Фильтр | Что исправляет | Время |
|--------|-----------------|-------|
| **Удаление размытости** | Размытые фото, движение камеры | 15-20% |
| **Поднятие теней** | Тёмные области, подземелья | 20-25% |
| **Удаление шума** | Зёрна, помехи на ISO | 20-25% |
| **Контраст** | Плоские фото, серо-буро | 10-15% |
| **Яркость** | Тёмные фото, недодержка | 10-15% |
| **Цвет** | Мёртвые краски, серость | 10-15% |
| **Upscaling (High)** | Низкое разрешение | 30-40% |

## 📊 Примеры использования

### Пример 1: Тёмное фото из подземелья
```bash
python process_image.py -i dark_dungeon.jpg -o bright_dungeon.jpg -q high
```

### Пример 2: Размытое фото со смартфона
```bash
python process_image.py -i blurry_phone.jpg -o sharp_phone.jpg -q medium
```

### Пример 3: Шумное фото с высокого ISO
```bash
python process_image.py -i noisy_night.jpg -o clean_night.jpg --no-deblur
```

### Пример 4: Быстрая обработка 100 фото
```bash
python batch_process.py -i raw_photos -o enhanced -q fast
```

## ⚙️ Структура проекта

```
ai_foto/
├── main.py                    # GUI приложение
├── process_image.py           # CLI обработка одного файла
├── batch_process.py           # Пакетная обработка
├── test_app.py                # Тесты приложения
├── requirements.txt           # Зависимости
├── config.py                  # Конфигурация
├── README.md                  # Краткое описание
├── GUIDE.md                   # Детальное руководство
│
├── core/                      # Основные модули
│   ├── __init__.py
│   ├── image_processor.py     # Основной класс обработки
│   └── enhancement.py         # Продвинутые фильтры
│
├── ui/                        # Графический интерфейс
│   ├── __init__.py
│   └── gui.py                 # PySimpleGUI интерфейс
│
├── output/                    # Сохранённые фото (создаётся автоматически)
└── venv_ai_foto/              # Виртуальное окружение
```

## 💡 Советы

1. **Для очень тёмных фото** - используйте `high` качество
2. **Для размытых фото** - используйте `medium` или `high`
3. **Для шумных фото (высокий ISO)** - используйте `high`
4. **Для быстрого просмотра** - используйте `fast`
5. **Пакетная обработка** - запускайте ночью для больших объёмов

---

**Версия:** 1.0.0  
**Последнее обновление:** 2026-06-15  
**Лицензия:** MIT
