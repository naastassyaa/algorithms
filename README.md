Виконала Глушко Анастасія Олегівна (ІР-24)   
Лабораторна робота №1 (Варіант 1 Рівень 2)  
Зеник подарував Марічці ділянку городу розміром n на m, поділену на клітинки розміром 1 на 1 метр. У кожній клітинці Марічка посадила гарбузи, щоб дарувати їх залицальникам. Марічка почала садити гарбузи починаючи із верхньої лівої, і при досягненні правої межі - розверталась і рухалась справа наліво, як вказано в прикладі для m x n, де m - кількість рядків, а n - кількість стовпців:

1 2 3 4 
8 7 6 5 
9 10 11 12 
16 15 14 13

Для садіння Марічка вирішила використати робота-садівника, який садить в кожну клітинку задану кількість зернят, які слід вказати як одномірний масив m x n. Якщо Марічка хоче посадити таку кількість гарбузів

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Тоді роботу необхідно подати на всід таку послідовність (маршрут робота не незмінним): 

1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

 
Реалізуйте алгоритм, який отримає на вхід масив розміром m та n, в кожній клітинці якого знаходиться бажана кількість гарбузів та поверне одномірний масив, скільки зернин має висаджувати робот при руху згідно маршруту, вказаного в цій задчі (маршрут є незмінним)

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6



Лабораторна робота №2 (Варіант 1 Рівень 2)  
Love

Андрій закоханий у Ілону. Вони вирішили провести День святого Валентина разом в Ашані, але Андрій, як ми всі знаємо, дуже зайнятий на роботі, тому він не зміг прийти. Тепер якраз Ілона знову наповнена гнівом і готова його вбити. Але є щось, що ви можете зробити.

Андрій розповідає Ілоні, що він програміст-початківець і, як правило, зайнятий вирішенням важливих проблем на проекті. Тож Ілона вирішує перевірити його алгоритмічні навички. Вона пише масив N цілих чисел. Вона дає йому число P і запитує, чи може він знайти три ( тільки три) цілих числа Ai Aj Ak (i ≠ j ≠ k) в масиві, сума якого дорівнює числу P, тобто

Ai + Aj + Ak  = P

Отже, чим швидше Андрій скаже відповідь “Такі числа є” або “Таких чисел немає” тим швидше він отримає поцілунок

Вхідні дані:
Масив цілих чисел A1, A2 A3 ……………. AN 
Р - Шукане число 

Обмеження
3<= N <= 1000
1<= Ai <= 10^9 де 1<= i <=N
1<= P <= 3*10^9

Приклад

Input
1 2 3
6

Output
True

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище


Лабораторна робота №3 (Варіант 1 Рівень 3)  
Для заданого бінарного дерева та конкретної вершини в цьому дереві реалізуйте функцію пошуку наступного елемента під час серединного проходу (in-order traversal). Наступник - це вузол, який має значення більше за заданий вузол і знаходиться найближче до нього при серединному обході.

Нехай у вас задане бінарне дерево такого вигляду:
```
    10
   /  \
  5    15
 / \     \
3   7    20
         /
        12

```
Для вершини зі значенням 7, наступник - це вузол зі значенням 10.

Функція отримує на вхід корінь бінарного дерева та вершину, для якої потрібно знайти наступника.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
```
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
```

Ваша функція має мати такий вигляд:

```
def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
```

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `BinaryTree` наступним чином:

```
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)


Лабораторна робота №4 (Варіант 4 Рівень 3)
Знайдіть найкоротший безпечний маршрут у полі з датчиками  

Нехай у вас задане прямокутне поле, на якому встановлені датчики в певних місцях. Перетніть його найкоротшим безпечним шляхом, не активуючи датчики.  

Прямокутне поле має форму матриці M × N, і нам потрібно знайти найкоротший шлях від будь-якої клітинки в першому стовпці до будь-якої клітинки в останньому стовпці матриці. Датчики позначаються в матриці значенням 0, і всі її вісім суміжних осередків також можуть активувати датчики. Шлях можна побудувати лише з комірок зі значенням 1, і в будь-який момент ми можемо рухатися лише на один крок в одному з чотирьох напрямків. Допустимі ходи:  

Вгору: (x, y) -> (x – 1, y)  
Ліворуч: (x, y) -> (x, y – 1)  
Перейти вниз: (x, y) -> (x + 1, y)  
Праворуч: (x, y) -> (x, y + 1)  
Наприклад, розглянемо таку матрицю:  

![image](https://github.com/naastassyaa/algorithms/assets/119229968/44336c4e-54dd-478b-bfe4-5c878ca7868e)  



Найкоротший безпечний шлях має довжину 11. Безпечний маршрут позначений зеленим кольором:  

![image](https://github.com/naastassyaa/algorithms/assets/119229968/99d04b78-75d6-4b83-8fb5-67d91a6bc367)  


Для представлення графу слід використати матрицю, який зчитується з файлу input.txt  
Алгоритм має вивести довжину найкоротшого шляху, або -1 якщо такого не існує  
Результат слід вивести у файл output.txt  
 
Лабораторна робота №5 (Варіант 1 Рівень 3)
Iгровий сервер 88889  
Код задачi: GAMSRV  
Важливим фактором для багатокористувацької онлайн-гри є низька мережева затримка вiд користувача до сервера. При цьому, пристрої в Iнтернетi спiлкуються один з одним, використовуючи мережевi маршрути, якi проходять через низку промiжних вузлiв-маршрутизаторiв. Кожна ланка цього маршруту має власну ненульову затримку.
Кожен вузол мережi може виконувати одну з трьох ролей: Client, Router або Server.  
• Server може бути лише один на всю мережу.  
• Усi комунiкацiї двостороннi: якщо вузол A може спiлкуватися з вузлом B, вузол B може спiлкуватися з вузлом A з такою ж затримкою.  
• Якщо iснує кiлька шляхiв вiд клiєнта до сервера, клiєнт гарантовано пiде шляхом з найменшою сумарною затримкою (навiть якщо цей шлях пролягає через iншого клiєнта).  
• Усi затримки — сталi додатнi числа.  
Для прикладу вище, затримки до клiєнтiв становлять:   
• Client 1: 10 + 80 + 50 = 140 ms  
• Client 2: 100 + 50 = 150 ms  
• Client 3: 20 ms  
Максимальною затримкою в такому випадку є 150 ms. Однак, якщо ми помiняємо ролями вузли “Router 2” i “Server”, затримки скоротяться до 90 ms, 100 ms i 70 ms вiдповiдно, тодi максимальна затримка буде становити 100 ms.
Ви розробляєте онлайн-гру для користувачiв зi всiєї країни, i бажаєте розмiстити центральний iгровий сервер таким чином, щоб максимальна затримка мiж сервером i кожним клiєнтом була мiнiмальною. В якостi сервера можна вибрати будь-який вузол мережi, який не є клiєнтом. Маючи iнформацiю про топологiю мережi (якi вузли з’єднанi з якими, i яка затримка кожного з’єднання), знайдiть таке розташування сервера, яке мiнiмiзує найбiльше значення затримки до клiєнта. Виведiть це значення затримки.  
Вхiднi данi  
Вхiдний файл gamsrv .in складається з M + 2 рядкiв.  
• Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно. 3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000  
• Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N.  
• Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency — номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання. 1 ≤ latency ≤ 109.  

Вихiднi данi  
Вихiдний файл gamsrv .out повинен мiстити одне число — мiнiмальне значення найбiльшої затримки до клiєнта (яке ми отримаємо при оптимальному розташуваннi сервера).


Лабораторна робота №6 (Варант 1 Рівень 3)
Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод скінченних автоматів для пошуку підстрічки у стрічці  
