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

Гиперпараметры:

1. Optimizer SGD
2. Learning rate 0.01
3. Momentum 0.9
4. Weight_decay 0.0001
5. Batchsize 64
6. Image size 32x32

Train loss:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/befb41e1-c6a0-4bb9-8865-3360be606a4f)

Validation loss:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/18729c6b-9c73-400c-a328-5653e1bb8556)

Recall on validation:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/e39c071a-3f3a-4b92-bf34-af343af55db8)

Precision on validation:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/9c284f5b-138e-42a2-8a99-333ce22fe5d1)

F1 Score on validation:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/c3e53f0c-1b53-455a-8f15-4a33c9b4e9c6)

Метрики по классам: 

| Attempt | recall | precision | f1_score |
| :---:   | :---:  | :---:     | :---:    |
| Airplane| 0.82   | 0.88      |  0.83    |
| Automobile | 0.90   | 0.93      |  0.91    |
| Bird    | 0.79   | 0.76      |  0.77    |
| Cat     | 0.72   | 0.68      |  0.68    |
| Deer    | 0.86   | 0.76      |  0.79    |
| Dog     | 0.71   | 0.84      |  0.75    |
| Frog    | 0.81   | 0.90      |  0.84    |
| Horse   | 0.92   | 0.79      |  0.84    |
| Ship    | 0.94   | 0.85      |  0.89    |
| Truck   | 0.83   | 0.95      |  0.87    |

Example:

![image](https://github.com/Egorbl/images_processing_homeworks/assets/83879805/2e02d34d-7eff-465f-9ae8-617012a5992a)

