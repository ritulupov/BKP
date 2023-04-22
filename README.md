
<h1 align="center">Прогнозирование конечных свойств новых материалов</h1>
<h1 align="center"> (композиционных материалов)</h1>
<h3 align="center">Data Science 2022 4.0</h3>
<h3 align="center">Выпускная квалификационная работа</h3>

### Описание:

Композиционные материалы - это искусственно созданные материалы, состоящие из нескольких других с четкой границей между ними. Композиты обладают теми свойствами, которые не наблюдаются у компонентов по отдельности. При этом композиты являются монолитным материалом, т.е. компоненты материала неотделимы друг от друга без разрушения конструкции в целом. Яркий пример композита - железобетон. Бетон прекрасно сопротивляется сжатию, но плохо растяжению. Стальная арматура внутри бетона компенсирует его неспособность сопротивляться сжатию, формируя тем самым новые, уникальные свойства. Современные композиты изготавливаются из других материалов: полимеры, керамика, стеклянные и углеродные волокна, но данный принцип сохраняется. У такого подхода есть и недостаток: даже если мы знаем характеристики исходных компонентов, определить характеристики композита, состоящего из этих компонентов, достаточно проблематично. Для решения этой проблемы есть два пути: физические испытания образцов материалов, или прогнозирование характеристик. Суть прогнозирования заключается в симуляции представительного элемента объема композита, на основе данных о характеристиках входящих компонентов (связующего и армирующего компонента).

На входе имеются данные о начальных свойствах компонентов композиционных материалов (количество связующего, наполнителя, температурный режим отверждения и т.д.).

На выходе необходимо спрогнозировать ряд конечных свойств получаемых композиционных материалов.

Кейс основан на реальных производственных задачах Центра НТИ «Цифровое материаловедение: новые материалы и вещества» (структурное подразделение МГТУ им. Н.Э. Баумана).

Актуальность: Созданные прогнозные модели помогут сократить количество проводимых испытаний, а также пополнить базу данных материалов возможными новыми характеристиками материалов, и цифровыми двойниками новых композитов.

### Для решения проблемы, определенния характеристк композита путем прогнозироваия, на основе данных о характеристиках входящих компонентов (связующего и армирующего компонента) была проделана следующая работа:

1. Датасеты со свойствами композитов, расположенные в папке data были объеденены по индексу с типом объединения INNER
2. Проведен разведочный анализ данных. Произведена визуализация данных в виде тепловой карты корреляций, гистограмм распределения каждого признака, диаграмм ящика с усами, построены попарные графики рассеяния точек. Для каждой колонки получено среднее, медианное значение. Проведена проверека данных на отсутствие пропусков. Выбросы были исключены.
3. Проведена предобработка данных: из колонки 'Поверхностная плотность, г/м2' извлечен квадратный корень для смещения распределения вправо, удалены выбросы по правилу трех сигм. Для нормализации были опробованы MinMaxScaler, StandardScaler и Normalizer из библиотеки Scikit-Learn. В итоге использован StandardScaler.
4. Для выявления модели машинного обучения лучшей в прогнозе модуля упругости при растяжении и прочности при растяжении, били опробованы: Линейная регрессия, Метод опорных векторов, Случайный лес, Градиентный бустинг, Лассо регрессор. При построении моделей проведен поиск гиперпараметров с помощью случайного поиска и поиска по сетке с перекрестной проверкой, количество блоков равно 10.
5. Написана нейронная сеть, которая рекомендует соотношение матрица-наполнитель.
6. Разработано приложение с веб интерфейсом **composit.py** для выполнения прогноза модуля упругости при растяжении и прочности при растяжении.

### Приложение:

Приложение **composit.py** находится в папке **app**
Д

Автор: Тулупов Роман Иванович

Выпускная квалификационная работа по программе повышения квалификации «Data Science» в обущчающем центре МГТУ им. Н. Э. Баумана
2023 г. 
