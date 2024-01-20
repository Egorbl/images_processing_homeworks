# images_processing_homeworks

ФИО: Беляков Егор Алексеевич

Предмет: Обработка и генерация изображений

Задача: Многоклассовая классификация на датасете CIFAR10

Архитектура: Resnet34, адаптированный для изображений 32x32

Классы:

1. Airplane
2. Automobile
3. bird
4. cat
5. deer
6. dog
7. frog
8. horse
9. ship
10. truck

Архитектура: Resnet

На всем датасете был предобучен backbone сети resnet18 на задаче восстановления изображения (Encoder - Decoder)

В целом, на небольшой части датасета предобучение позволило получить лучшие метрики. При обучении на всем датасете CIFAR10 предобучение на задаче восстановление изображения скорее вредило.

Эксперимент 1 (100% датасета)

Лоссы

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/18430748-40fe-49f4-ba02-c7e2550afd95)

Реколл

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/2aa89eaf-7842-46d2-ba4a-adefaf99aa4f)

Пресижн

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/f93e9914-ddcd-46e8-909d-5eed84c3caa9)

F1 мера

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/a021b2c9-590a-4b2f-8654-0baf5c104935)

Эксперимент 2 (50% датасета)

Лоссы

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/7065fa8b-0d13-47e0-904f-57cceb2b2c57)

Реколл

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/c3c85c70-69d3-48fe-b2f2-24dcc3bc10da)

Пресижн

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/d663c3a5-69d7-411f-99de-b8c4ab94b8bd)

F1 мера

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/d21fe60e-0c7c-4c03-9af9-5938d781e47d)

Эксперимент 3 (10% датасета)

Лоссы

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/3413da25-ba57-4130-b438-dd6b6ebcdd5c)

Реколл

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/26f12592-aefb-471d-8002-e55413f00431)

Пресижн

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/47b10222-8e45-4184-9f1a-24ad825fc212)

F1 мера

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/3eb1c4c2-124d-42d6-9f65-da1532126189)


