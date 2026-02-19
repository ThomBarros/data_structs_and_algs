#include <stdio.h>
#include <stdlib.h>

typedef struct {
    void **data;
    int size;
    int capacity;
} DynamicArray;

void initArray(DynamicArray *arr);
void resize(DynamicArray *arr, int new_capacity);
void append(DynamicArray *arr, void *value);
void insert(DynamicArray *arr, int index, void *value);
void removeAt(DynamicArray *arr, int index);
void* pop(DynamicArray *arr);
void printIntArray(DynamicArray *arr);
void freeArray(DynamicArray *arr, int freeElements);

void initArray(DynamicArray *arr) {
    arr-> size = 0;
    arr->capacity = 1;
    arr->data = malloc(sizeof(void*) * arr->capacity);
    if (!arr->data) {
        printf("Memory allocation failed\n");
        exit(1);
    }
}

void resize(DynamicArray *arr, int new_capacity) {
    void **new_data = realloc(arr->data, sizeof(void*) * new_capacity);
    if (!new_data) {
        printf("Memory reallocation failed\n");
        exit(1);
    }

    arr->data = new_data;
    arr->capacity = new_capacity;
}

void append(DynamicArray *arr, void *value) {
    if (arr->size == arr->capacity) {
        resize(arr, arr->capacity * 2);
    }
    arr->data[arr->size++] = value;
}

void insert(DynamicArray *arr, int index, void *value) {
    if (index < 0 || index > arr->size) {
        printf("Index out of bounds\n");
        return;
    }

    if (arr->size == arr->capacity) {
        resize(arr, arr->capacity * 2);
    }

    for (int i = arr->size; i > index; i--) {
        arr->data[i] = arr->data[i - 1];
    }

    arr->data[index] = value;
    arr->size++;
}

void removeAt(DynamicArray *arr, int index) {
    if (index < 0 || index > arr->size) {
        printf("Index out of bounds\n");
        return;
    }

    for (int i = index; i < arr->size; i++) {
        arr->data[i] = arr->data[i + 1];
    }

    arr->size--;
}

void* pop(DynamicArray *arr) {
    if (arr->size == 0) {
        printf("Pop from empty array\n");
        return NULL;
    }
    
    return arr->data[--arr->size]; 
}

void freeArray(DynamicArray *arr, int freeElements) {
    if (freeElements) {
        for (int i = 0; i < arr->size; i++) {
            free(arr->data[i]);
        }
    }
    free(arr->data);
}

void printIntArray(DynamicArray *arr) {
    printf("[");
    for (int i = 0; i < arr->size; i++) {
        printf("%d", *(int*)arr->data[i]);
        if (i < arr->size - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

int main() {
    DynamicArray arr;
    initArray(&arr);

    for (int i = 1; i<= 3; i++) {
        int *value = malloc(sizeof(int));
        *value = i * 10;
        append(&arr, value);
    }

    printIntArray(&arr);

    int *newVal = malloc(sizeof(int));
    *newVal = 15;
    insert(&arr, 1, newVal);
    printIntArray(&arr);

    int *popped = (int*)pop(&arr);
    printf("Popped: %d\n", *popped);
    free(popped);

    printIntArray(&arr);
    removeAt(&arr, 1);
    printIntArray(&arr);

    printIntArray(&arr);
    freeArray(&arr, 1);
    return 0;
}



