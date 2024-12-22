#include <stdio.h>

void QuickSort(int *ar, int start, int end) {

    int left = start;
    int right = end;
    int pivot = ar[start]; //опорный элемент 

    while (start < end) {

        while ((ar[end] >= pivot)&&(start < end)) {
            end--; //Сдвигаем правую границу, пока элемент с индексом end больше pivot
        }
        if (start != end) {  //Если границы не сомкнулись 
            ar[start] = ar[end];
            start++;
        }
        while((ar[start]<=pivot)&&(start<end)){
            start++;
        }
        if (start != end){
            ar[end] = ar[start];
            end--;
        }
    }
    ar[start] = pivot;
    pivot = start;
    start = left;
    end = right;
    if(start < pivot){ 
        QuickSort(ar, start, pivot-1); //Рекурсивный вызов функции для левой и правой частей массива
    }
    if(end > pivot){
        QuickSort(ar, pivot+1, end);
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
    QuickSort(arr, 0, count-1);
    printf("Result: ");
    for(int i=0;i<count;i++) {
        printf(" %d", arr[i], " ");
    }
};
