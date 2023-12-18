# Pet-UAV

Pet-проект по разработке алгоритмов автономного управления БПЛА с созданием UI-интерфейса для более удобной и наглядной апробации данных алгоритмов на симуляторе квадрокоптера.

Udacity's FCND Simulator необходимо скачать [здесь]((https://github.com/udacity/FCND-Simulator-Releases/releases). Python-код использует [Udacidrone](https://udacity.github.io/udacidrone/) API для связи с симулятором. Этот API использует [MAVLink](http://qgroundcontrol.org/mavlink/start) протокол.

## Необходимые компоненты

Для запуска этого проекта вам необходимо установить следующее программное обеспечение:

- [Miniconda](https://conda.io/miniconda.html) with Python 3.6. 
- [Udacity FCND Simulator](https://github.com/udacity/FCND-Simulator-Releases/releases) желательно последней версии.
## Cтек

Python 3.6

Симулятор квадрокоптера **Udacity Flying Car Nanodegree (FCND)**

**Udacidrone API** для связи с симулятором

Дистрибутив **Miniconda**

Фреймворк **Qt** для создания UI

Сервер **Visdom** для отображения траектории движения БПЛА в виде графика в самом UI.


## Запуск приложения

Необходимо запустить симулятор FCND-Sim_Windows_64-bit.exe, затем main.py
