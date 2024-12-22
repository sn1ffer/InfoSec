#include <stdio.h>

//Функция построения max-heap - просеивание кучи 

void siftDown(int *numbers, int root, int bottom){
    int maxChild;
    int done = 0;
    // Условие пока не дошли до последнего ряда 
    while ((root * 2 <= bottom) && (!done)){
        if (root * 2 == bottom)  //условие нахождения в последнем ряду 
            maxChild = root * 2; //левый ребенок 
        else if (numbers[root * 2] > numbers[root * 2 + 1]) //запоминаем большего потомка 
            maxChild = root * 2;
        else
            maxChild = root * 2 + 1;
        if (numbers[root] < numbers[maxChild]){
            int temp = numbers[root];
            numbers[root] = numbers[maxChild];
            numbers[maxChild] = temp;
            root = maxChild;
        }
        else
            done = 1;
    }
}

void heapSort(int *numbers, int array_size){
    for (int i = (array_size / 2); i >= 0; i--)
        siftDown(numbers, i, array_size - 1);

    for (int i = array_size - 1; i >= 1; i--){
        int temp = numbers[0];
        numbers[0] = numbers[i];
        numbers[i] = temp;
        siftDown(numbers, 0, i - 1);
    }
}


int main(){

    int count;
    printf("Enter the size of the array: ");
    scanf("%d", &count);
    printf("Enter the array elements: ");
    int arr[count];
    for (int i=0; i < count;i++) {
        scanf("%d", &arr[i]);
    }
    heapSort(arr, count);
    printf("Result: ");
    for(int i=0;i<count;i++) {
        printf(" %d", arr[i], " ");
    }
};
