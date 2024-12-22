# Steganography
## Least Significant Bit, LSB
Для встраивания секретное сообщение необходимо преобразовать в двоичную последовательность. Метод LSB предполагает замену одного или нескольких младших битов пикселей битами секретного сообщения при встраивании информации. Чтобы извлечь встроенную информацию, необходимо последовательно обойти пиксели изображения и сформировать последовательность из нужного количества младших битов каждого пикселя. При необходимости извлечённая битовая последовательность преобразуется в текст, изображение и т.д.

Программа обладает следующей функциональностью:

1) При встраивании:
+ Принимает на вход цветное (RGB) изображение-контейнер;
+ Принимает на вход информацию (например, текст, изображение
или битовую последовательность) для встраивания;
+ Принимает на вход желаемое кол-во последних бит пикселей, которые будут использованы для встраивания информации (чем меньше пикселей задействовано, тем менее заметно встраивание) 
+ Рассчитывает показатели качества встраивания;
2) При извлечении:
+ Принимает на вход цветное стегоизображение;