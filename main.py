#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

def main():
    # Устанавливаем кодировку для stdout
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    
    print("Начало выполнения скрипта...")
    for i in range(5):
        print(f"Капибара {i + 1} из 5")
        time.sleep(1)
    print("Миша привет")

if __name__ == "__main__":
    main() 