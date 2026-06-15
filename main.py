#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Foto - главное приложение
Программа для восстановления и улучшения качества фотографий
"""

from ui.gui import PhotoEnhancerGUI
import sys

def main():
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           🎨 AI Foto - Улучшение фотографий 🎨          ║
    ║         Восстановление размытых, тёмных и шумных фото   ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    try:
        app = PhotoEnhancerGUI()
        app.run()
    except Exception as e:
        print(f"❌ Ошибка при запуске приложения: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
