# Задачи Яндекс.Контест

В данном репозитории собрана моя коллекция задач, которые я решал на платформе Яндекс.Контест.<br />
**Направление: backend (python)**<br />
Ввиду особенностей работы системы тестирования (нельзя проверить решение по истечению отведённого времени) задачи будут разделены по разным статусам:

* ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen) – задача решена, все тесты Яндекс.Контеста пройдены
* ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B0%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D0%BE-yellow) – пройдена только часть тестов Яндекс.Контеста (получена ошибка или превышено
  ограничение по времени на одном из тестов)
* ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9D%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0%D1%81%D1%8C-orange) – задача решена и успешно работает с примерами из условия задачи, но тесты
  Яндекс.Контеста недоступны для прогона

**Содержание**

+ [Intern week offer 2022 — бэкенд](#internWeekendOffer2022)
    + [Достопримечательности](#attractions) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B0%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D0%BE-yellow)
        + [Описание](#attractions)
        + [Решение](/internWeekOffer2022/a_attractions.py)
    + [Четный подотрезок](#evenSubsequence) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#evenSubsequence)
        + [Решение](/internWeekOffer2022/b_even_sub_list.py)
+ [Algorithms intensive 2022](#AlgorithmsIntensive2022)
    + [Строительство лесенок](#stairs) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#stairs)
        + [Решение](/AlgorithmsIntensive/day_1/stairs.py)
    + [Купить и продать](#buySell) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#buySell)
        + [Решение](/AlgorithmsIntensive/day_1/buy_sell.py)
    + [Разница во времени](#trains) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#trains)
        + [Решение](/AlgorithmsIntensive/day_1/trains.py)
    + [Сломай палиндром](#palindrome) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#palindrome)
        + [Решение](/AlgorithmsIntensive/day_1/break_the_palindrome.py)
    + [Два из трех](#2outOf3) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#2outOf3)
        + [Решение](/AlgorithmsIntensive/day_2/two_out_of_three.py)
    + [Повторяющееся число](#repeatingNumber) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#repeatingNumber)
        + [Решение](/AlgorithmsIntensive/day_2/repeating_number.py)
    + [Замена слов](#wordsReplacement) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#wordsReplacement)
        + [Решение](/AlgorithmsIntensive/day_2/words_replacement.py)
    + [Majority](#majority) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#majority)
        + [Решение](/AlgorithmsIntensive/day_2/majority.py)
    + [Отбраковка](#rejectedSamples) ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)
        + [Описание](#rejectedSamples)
        + [Решение](/AlgorithmsIntensive/day_2/rejected_samples.py)

<a name="internWeekendOffer2022"><h2>Intern week offer 2022 — бэкенд</h2></a>

<a name="attractions"><h3>Достопримечательности ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%A0%D0%B5%D1%88%D0%B5%D0%BD%D0%B0%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D0%BE-yellow)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>256Mb</td>
 </tr>
</table>

Тур по городу N для Кати, Маши и Наташи будет удачным, если они посмотрят самые ожидаемые достопримечательности в нужном порядке.<br />
Составьте кратчайшую последовательность достопримечательностей для посещения, чтобы пожелания были выполнены.<br />
Даны три последовательности чисел. В любой из последовательностей числа могут повторяться.<br />
Вам нужно найти супер-последовательность.<br />
Супер-последовательность – это последовательность минимальной длины, чтобы в ней были все три последовательности непрерывными фрагментами.

#### Формат ввода

Ввод состоит из трех строк. Первый элемент каждой строки n<sub>i</sub> (1 ≤ n<sub>i</sub> ≤ 100) – число элементов в i-й последовательности.<br />
Далее идут n<sub>i</sub> положительных чисел, не превосходящих 100, – элементы последовательности.<br />
Все числа в строках разделены пробелами.

#### Формат вывода

Первая строка вывода содержит одно число k – длина супер-последовательности.<br />
Вторая строка содержит k разделенных пробелами чисел – элементы супер-последовательности.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>2 1 2<br />2 2 3<br />2 3 1</td>
    <td>4<br />1 2 3 1</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>1 2<br />2 1 2<br />3 3 1 2</td>
    <td>3<br />3 1 2</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">3</b></td>
    <td>5 1 2 3 4 5<br />4 9 10 11 12<br />5 5 6 7 8 9</td>
    <td>12<br />1 2 3 4 5 6 7 8 9 10 11 12</td>
 </tr>
</table>

#### Примечания

Заметим, что в первом примере сначала можно удовлетворить потребность Кати (посетить достопримечательности 1 и 2).<br />
Затем удовлетворить потребность Маши (2 и 3 достопримечательности).<br />
При этом, так как 2-ая достопримечательность была посещена последней, то
мы можем продолжить осмотр и посетить только 3 достопримечательность).<br />
Аналогично для Наташи.<br />
Во втором примере можно пойти по плану Наташи, тогда Маша и Катя автоматически пройдут предполагаемый маршрут.

<a name="evenSubsequence"><h3>Четный подотрезок ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>4 seconds</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>256Mb</td>
 </tr>
</table>

Красотой массива назовем наибольшее количество подряд идущих в нем четных чисел.<br />
Дан массив a, состоящий из n целых чисел. Разрешается не более k раз выбрать любые два элемента этого массива и поменять их местами.<br />
Найдите наибольшую возможную красоту массива после применения указанных операций.

#### Формат ввода

В первой строке записаны числа n и k (1 ≤ k ≤ n ≤ 10<sup>6</sup>).<br />
Во второй строке записаны числа a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub> (10<sup>-9</sup> ≤ a<sub>i</sub> ≤ 10<sup>9</sup>).

#### Формат вывода

Выведите единственное число — ответ на задачу.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>5 1<br />-1 2 4 3 0</td>
    <td>3</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>4 1<br />2 4 6 8</td>
    <td>4</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">3</b></td>
    <td>5 1<br />0 1 2 3 4</td>
    <td>3</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">4</b></td>
    <td>6 2<br />0 2 1 -1 -2 4</td>
    <td>4</td>
 </tr>
</table>

#### Примечания

В первом тесте можно поменять местами пару чисел − 1 и 0.<br />
Тогда в результате получим четный подотрезок 0, 2, 4 длины 3.<br />
Подотрезок длины больше 3, очевидно, получить нельзя.

<a name="AlgorithmsIntensive2022"><h2>Интенсив по алгоритмам</h2></a>

<a name="stairs"><h3>Строительство лесенок ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Вася занимается строительством лесенок из блоков. Лесенка состоит из ступенек, при этом i-ая ступенька должна состоять ровно из i блоков.<br />
По заданному числу блоков n определите максимальное количество ступенек в лесенке, которую можно построить из этих блоков.

#### Формат ввода

Вводится одно число n (1 ≤ n ≤ 2<sup>31</sup> - 1).

#### Формат вывода

Выведите одно число — количество ступенек в лесенке.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>5</td>
    <td>2</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>8</td>
    <td>3</td>
 </tr>
</table>

#### Примечания

Рисунок соответствует примерам.<br />
На рисунке черным показаны блоки, использованные при строительстве лестницы, а красным — оставшиеся лишними блоки, которых недостаточно для строительства очередной ступеньки.<br />
![](https://contest.yandex.ru/testsys/statement-image?imageId=c8fb05419c659d4b6a43dbb5dbcd17f048be9c282682c35ee60fe47670f4789e)

<a name="buySell"><h3>Купить и продать ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней.<br />Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.<br />
Определите номера дней для покупки и продажи газа для получения максимальной прибыли.

#### Формат ввода

В первой строке вводится число дней n (1 ≤ n ≤ 100000).<br />
Во второй строке вводится n чисел — цены за 1000 кубометров газа в каждый из дней.<br />
Цена — целое число от 1 до 5000. Дни нумеруются с единицы.

#### Формат вывода

Выведите два числа i и j — номера дней для покупки и продажи газа. Если прибыль получить невозможно, выведите два нуля.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>6<br />10 3 5 3 11 9</td>
    <td>2 5</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>4<br />5 5 5 5</td>
    <td>0 0</td>
 </tr>
</table>



<a name="trains"><h3>Разница во времени ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Каждые сутки на вокзал прибывает n электричек.<br />
По заданному расписанию прибытия электричек определите минимальное время между прибытием двух разных электричек.

#### Формат ввода

В первой строке задано число n (1 ≤ n ≤ 2 × 10<sup>4</sup>) — количество электричек.<br />
Во второй строке задано n моментов времени в формате HH:MM (0 ≤ HH ≤ 23, 0 ≤ MM ≤ 59) через пробел.

#### Формат вывода

Выведите одно число — минимальное время в минутах между прибытием двух электричек.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>2<br />23:59 00:00</td>
    <td>1</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>3<br />00:00 23:59 00:00</td>
    <td>0</td>
 </tr>
</table>


<a name="palindrome"><h3>Сломай палиндром ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Палиндромом называется строка, которая читается одинаково слева-направо и справа-налево.<br />
В заданной строке-палиндроме необходимо заменить один символ, чтобы она перестала быть палиндромом.<br />
При этом полученная строка должна быть лексикографически минимальной.

Строка A лексикографически меньше строки B (той же длины), если на первой различающейся позиции в строке A стоит меньший символ, чем в B.<br />
Например, строка adbc меньше строки adca, т.к. первые два символа в строках совпадают, а на третьем месте в строке adbc стоит символ b, который меньше символа c, стоящего на третьей позиции в строке adca.

#### Формат ввода

Вводится строка-палиндром, состоящая из маленьких букв латинского алфавита.<br />
Длина строки не превосходит 1000.

#### Формат вывода

Выведите лексикографически минимальную строку, не являющуюся палиндромом, полученную из исходной строки заменой одного символа.<br />
Если получить такую строку невозможно - выведите пустую строку.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>abba</td>
    <td>aaba</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>a</td>
    <td></td>
 </tr>
</table>


<a name="2outOf3"><h3>Два из трех ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

#### Формат ввода

Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины списка n (1 ≤ n ≤ 1000).<br />
Вторая строка описания содержит список натуральных чисел, записанных через пробел. Числа не превосходят 10<sup>9</sup>.

#### Формат вывода

Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание, что каждое число необходимо выводить только один раз.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>2<br />3 1<br />2<br />1 3<br />2<br />1 2</td>
    <td>1 3</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>3<br />1 2 2<br />3<br />3 4 3<br />1<br />5</td>
    <td></td>
 </tr>
</table>


<a name="repeatingNumber"><h3>Повторяющееся число ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число, причём расстояние между повторами не превосходило k.

#### Формат ввода

В первой строке задаются два числа n и k (1 ≤ n, k ≤ 10<sup>5</sup>).<br />
Во второй строке задаются n чисел, по модулю не превосходящих 10<sup>9</sup>.

#### Формат вывода

Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит k и NO в противном случае.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>4 2<br />1 2 3 1</td>
    <td>NO</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>4 1<br />1 0 1 1</td>
    <td>YES</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">3</b></td>
    <td>6 2<br />1 2 3 1 2 3</td>
    <td>NO</td>
 </tr>
</table>


<a name="wordsReplacement"><h3>Замена слов ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте.<br />
Для этого был составлен словарь слов, до которых можно сокращать более длинные слова.<br />
Слово из текста можно сократить, если в словаре найдется слово, являющееся началом слова из текста.<br />
Например, если в списке есть слово "лом", то слова из текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".<br />
Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.

#### Формат ввода

В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв.<br />
Гарантируется, что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.<br />
Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв).<br />
Количество слов в тексте не превосходит 10<sup>5</sup>, а суммарное количество букв в них — 10<sup>6</sup>.

#### Формат вывода

Выведите текст, в котором осуществлены замены.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>a b<br />abdafb basrt casds dsasa a</td>
    <td>a b casds dsasa a</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>aa bc aaa<br />a aa aaa bcd abcd</td>
    <td>a aa aa bc abcd</td>
 </tr>
</table>


<a name="majority"><h3>Majority ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

Majority (в дословном переводе "большинство") — это значение элемента, который в массиве длиной n встречается более чем n / 2 раз.<br />
Определите majority массива, если гарантируется, что такой элемент существует.

#### Формат ввода

В первой строке вводится число n (1 ≤ n ≤ 5 × 10<sup>4</sup>).<br />
Во второй строке вводится n чисел через пробел, числа не превосходят 10<sup>9</sup> по модулю.

#### Формат вывода

Выведите majority массива.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>3<br />1 2 1</td>
    <td>1</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>7<br />7 5 5 5 5 4 5</td>
    <td>5</td>
 </tr>
</table>


<a name="rejectedSamples"><h3>Отбраковка ![](https://img.shields.io/badge/%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%9F%D1%80%D0%BE%D0%B9%D0%B4%D0%B5%D0%BD%D1%8B%20%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D1%8B-brightgreen)</h3></a>

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 second</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
 </tr>
</table>

На заводе по производству химических соединений есть реактор, в результате работы которого получаются химические вещества, формула которых записывается в виде строки состоящей из заглавных и строчных латинских букв.<br />
Также у завода есть список желательных веществ (веществ первого сорта), которые хотелось бы получить.<br />
Кроме того заводу также интересны вещества второго и третьего сорта.<br />
Вещество называется веществом первого сорта, если его формула в точности совпадает с формулой из списка желательных веществ.<br />
Вещество называется веществом второго сорта, если из него можно получить вещество из списка желательных в разультате замены некоторых заглавных букв на строчные и наоборот.<br />
Вещество называется веществом третьего сорта, если в нем возможны как замены букв с заглавных на строчные и наоборот, так и замены любых гласных букв (aeiou) на другие гласные буквы, таким образом чтобы получилось вещество из списка желательных.<br />
В связи со сложной экономической ситуацией было принято решение не выбрасывать вещества второго и третьего сорта и для каждого из них найти похожее вещество из списка желательных, причем, если преобразованиями из вещества второго или третьего сорта можно
получить несколько веществ из списка желательных, то его следует преобразовывать к тому веществу, которое находится раньше в списке желательных.

#### Формат ввода

В первой строке вводится число n (1 ≤ n ≤ 5000) — количество веществ в списке желательных.<br />
Во второй строке вводится n слов через пробел — список желательных веществ.<br />
В третьей строке вводится число k (1 ≤ k ≤ 5000) — количество веществ, полученных в реакторе.<br />
Во второй строке вводится k слов через пробел — список веществ, полученных в реакторе.<br />
Длина всех слов не превосходит 7.

#### Формат вывода

Для каждого вещества выведите:<br />
Если оно является веществом первого сорта — название этого вещества.<br />
Если оно не является веществом первого сорта, но является веществом второго сорта — первое из списка желательных веществ, к которому можно преобразовать это вещество.<br />
Если оно не является веществом первого или второго сорта, но является веществом третьего сорта — первое из списка желательных веществ, к которому можно преобразовать это вещество.<br />
В противном случае выведите пустую строку.<br />
Все слова в вывод должны быть разделены одним пробелом.

#### Примеры

<table>
 <tr>
    <td><b style="font-size:30px">#</b></td>
    <td><b style="font-size:30px">Входные данные</b></td>
    <td><b style="font-size:30px">Ожидаемый ответ</b></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">1</b></td>
    <td>4<br />LiTe lite bare Bare<br />10<br />Bare BARE Bear bear lite Lite LiTe leti leet leto</td>
    <td>Bare bare   lite LiTe LiTe LiTe  LiTe</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">2</b></td>
    <td>1<br />DeLay<br />1<br />delOy</td>
    <td>DeLay
</td>
 </tr>
</table>

