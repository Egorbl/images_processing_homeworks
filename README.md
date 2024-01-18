# ДЗ номер 2. Беляков Егор

Задача: Детекция аномалий

Цель: найди проливы среди изображений

Loss: MSE

Архитектура: кастомный AutoEncoder, реализованный с помощью сверток и ConvTranspose

Оптимизитор: AdamW, lr=0.0003

Основная проблема задачи - изображения в тесте сильно отличаются от изображений в train

Возможное решение - аугментации

Ход решения:

График лоссов при обучении автоенкодера

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/068a2877-b1dc-40dc-ab33-7e51387ae338)

Лоссы на валидации спустя 10 эпох

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/a1b1713a-7079-40a1-a039-f782491eb405)

Гистограмма MSE на валидации:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/13656e01-f504-4799-be16-ef70e2893fcf)

Гистограмма MSE на проливах:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/f1fa4e6f-f1a4-43d5-8a21-5bb6a6edff83)


