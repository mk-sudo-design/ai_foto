import PySimpleGUI as sg
import os
from pathlib import Path
from core.image_processor import ImageProcessor
from core.enhancement import EnhancementEngine
from PIL import Image
import threading

class PhotoEnhancerGUI:
    """GUI приложение для улучшения фото"""
    
    def __init__(self):
        sg.theme('DarkBlue3')
        self.processor = None
        self.current_image = None
        self.current_path = None
        self.processing = False
    
    def create_window(self):
        """Создать главное окно"""
        layout = [
            [sg.Text('🎨 AI Foto - Улучшение фотографий', font=('Arial', 16, 'bold'))],
            [sg.Text('')],
            
            # Блок выбора файла
            [sg.Text('Выберите фото:', font=('Arial', 11, 'bold'))],
            [sg.Input(key='file_path', size=(40, 1)), 
             sg.FileBrowse('Обзор', file_types=(("Images", "*.jpg *.jpeg *.png"),))],
            [sg.Text('')],
            
            # Блок качества
            [sg.Text('Качество обработки:', font=('Arial', 11, 'bold'))],
            [sg.Radio('⚡ Быстро (1-2 мин)', 'quality', default=False, key='fast'),
             sg.Radio('⚖️ Среднее (2-3 мин)', 'quality', default=True, key='medium'),
             sg.Radio('🎯 Высокое (3-5 мин)', 'quality', default=False, key='high')],
            [sg.Text('')],
            
            # Блок опций обработки
            [sg.Text('Опции обработки:', font=('Arial', 11, 'bold'))],
            [sg.Checkbox('✓ Удалить размытость', default=True, key='deblur'),
             sg.Checkbox('✓ Поднять тени', default=True, key='enhance_shadows')],
            [sg.Checkbox('✓ Удалить шум', default=True, key='denoise'),
             sg.Checkbox('✓ Улучшить контраст', default=True, key='contrast')],
            [sg.Checkbox('✓ Улучшить яркость', default=True, key='brightness'),
             sg.Checkbox('✓ Улучшить цвет', default=True, key='color')],
            [sg.Text('')],
            
            # Блок сохранения
            [sg.Text('Сохранить как:', font=('Arial', 11, 'bold'))],
            [sg.Input(key='output_path', size=(40, 1), default_text='output/result.jpg'), 
             sg.FolderBrowse('Папка')],
            [sg.Text('')],
            
            # Кнопки
            [sg.Button('🚀 Обработать фото', size=(20, 2), font=('Arial', 11, 'bold'), button_color=('white', 'green')),
             sg.Button('❌ Выход', size=(20, 2), font=('Arial', 11, 'bold'))],
            
            # Статус
            [sg.Text(key='status', text='Готов к обработке', font=('Arial', 10), text_color='white')],
        ]
        
        return sg.Window('AI Foto - Улучшение фотографий', layout, size=(700, 700))
    
    def process_image(self, values):
        """Обработать изображение"""
        file_path = values['file_path']
        output_path = values['output_path']
        
        if not file_path:
            sg.popup_error('Выберите файл!')
            return
        
        if not output_path:
            output_path = 'output/result.jpg'
        
        # Определить качество
        quality = 'medium'
        if values['fast']:
            quality = 'fast'
        elif values['high']:
            quality = 'high'
        
        # Создать процессор
        self.processor = ImageProcessor(quality=quality)
        
        try:
            # Загрузить и обработать
            image = self.processor.load_image(file_path)
            engine = EnhancementEngine()
            
            # Применить выбранные опции
            if values['deblur']:
                image = self.processor.remove_blur(image)
            
            if values['enhance_shadows']:
                image = engine.fix_dark_image(image)
            
            if values['denoise']:
                image = self.processor.reduce_noise(image)
            
            if values['contrast']:
                image = self.processor.enhance_contrast(image, factor=1.4)
            
            if values['brightness']:
                image = self.processor.enhance_brightness(image, factor=1.15)
            
            if values['color']:
                image = self.processor.enhance_color(image, factor=1.25)
            
            # Сохранить
            os.makedirs(os.path.dirname(output_path) or 'output', exist_ok=True)
            self.processor.save_image(image, output_path)
            
            sg.popup_ok(f'✅ Готово!\n\nФото сохранено в:\n{output_path}')
            
        except Exception as e:
            sg.popup_error(f'Ошибка: {str(e)}')
    
    def run(self):
        """Запустить приложение"""
        window = self.create_window()
        
        while True:
            event, values = window.read()
            
            if event == sg.WINDOW_CLOSED or event == '❌ Выход':
                break
            
            if event == '🚀 Обработать фото':
                window['status'].update('⏳ Обработка... пожалуйста ждите...', text_color='yellow')
                window.refresh()
                
                try:
                    self.process_image(values)
                    window['status'].update('✅ Готов к обработке', text_color='lightgreen')
                except Exception as e:
                    window['status'].update(f'❌ Ошибка: {str(e)}', text_color='red')
        
        window.close()

if __name__ == '__main__':
    app = PhotoEnhancerGUI()
    app.run()
