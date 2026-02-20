#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    void* data;
    struct Node* next;
} Node;


typedef struct {
    Node* head;
    size_t size;
} LinkedList;    

Node* create_node(void* data) {
    Node* node = malloc(sizeof(void*));
    if (!node) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    node->data = data;
    node->next = NULL;
    return node;
}


void init_list(LinkedList* list) {
    list->head = NULL;
    list->size = 0;
}

int empty(LinkedList* list) {
    return list->size == 0;
}

void push_front(LinkedList* list, void* data) {
    Node* node = create_node(data); 
    node->next = list->head;
    list->head = node;
    list->size++;
}

void push_back(LinkedList* list, void* data) {
    Node* node = create_node(data);
    if (empty(list)) {
        list->head = node;
    } else {
        Node* current = list->head;
        while (current->next) {
            current = current->next;
        }
        current->next = node;
    }

    list->size++;
}


void* pop_front(LinkedList* list) {
    if (!list->head) {
        return NULL;
    }

    Node* temp = list->head;
    void* data = temp->data;

    list->head = temp->next;
    free(temp);
    list->size--;
    return data;
}

void free_list(LinkedList* list) {
    Node* current = list->head;

    while (current) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }

    list->head = NULL;
    list->size = 0;
}

   



