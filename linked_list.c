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


Node* create_node(void* data);
void init_list(LinkedList* list);
int size(LinkedList *list);
int empty(LinkedList* list); 
void push_front(LinkedList* list, void* data);
void push_back(LinkedList* list, void* data); 
void* pop_front(LinkedList* list); 
void* pop_back(LinkedList* list); 
void* front(LinkedList* list); 
void* back(LinkedList* list); 
void insert(LinkedList* list, size_t index, void* data); 
void* erase(LinkedList* list, size_t index);
void* value_n_from_end(LinkedList* list, size_t n);
void reverse(LinkedList* list);
void* remove_value(LinkedList* list, void* value);
void free_list(LinkedList* list); 



Node* create_node(void* data) {
    Node* node = malloc(sizeof(*node));
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


int size(LinkedList *list) {
    return list->size;
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


void* pop_back(LinkedList* list) {
    if (!list || !list->head) {
        return NULL;
    }

    Node* current = list->head; 

    if (current->next == NULL) {
        void* data = current->data;
        free(current);
        list->head = NULL;
        list->size--;
        return data;
    }

    while (current->next->next != NULL) {
        current = current->next;
    }

    Node* last = current->next;
    void* data = last->data;

    current->next = NULL;
    free(last);
    list->size--;

    return data;

}


void* front(LinkedList* list) {
    if (!list || !list->head) {
        return NULL;
    }

    return list->head->data;
}


void* back(LinkedList* list) {
    if (!list || !list->head){
        return NULL;
    }

    Node* current = list->head;
    while (current->next) {
        current = current->next;
    }
    return current->data;

}


void insert(LinkedList* list, size_t index, void* data) {
    if (!index || index > list->size) {
        printf("Index out of range");
        exit(1);
    }
    if (index == 0) {
       push_front(list, data);
       return;
    }
    Node* node = create_node(data);
    Node* current = list->head;

    for (size_t i = 0; i < index - 1; i++) {
        current = current->next;
    }

    node->next = current->next;
    current->next = node;
    list->size++;
}

     
void* erase(LinkedList* list, size_t index) {
    if (!list || index >= list->size) {
        printf("Index out of range");
        exit(1);
    }
    if (index == 0) {
        return pop_front(list);
    } 
    Node* current = list->head;

    for (size_t i = 0; i < index - 1; i++) {
        current = current->next;
    }

    Node* target = current->next;
    void* data = target->data;

    current->next = target->next;
    free(target);
    list->size--;

    return data;
}

        
void* value_n_from_end(LinkedList* list, size_t n) {
    if (empty(list)) {
        return NULL;
    }
    if (n >= list->size) {
        printf("n is too large\n");
        exit(1);
    }

    Node* fast = list->head;
    Node* slow = list->head;

    for (size_t i = 0; i < n; i++) {
        fast = fast->next;
    }

    while (fast->next) {
        slow = slow->next;
        fast = fast->next;
    }

    return slow->data;
}
        

void reverse(LinkedList* list) {
    if (empty(list)) {
        return;
    }

    Node* prev = NULL;
    Node* current = list->head;

    while (current) {
        Node* next_node = current->next;
        current->next = prev;
        prev = current;
        current = next_node;
    }

    list->head = prev;
}


void* remove_value(LinkedList* list, void* value) {
    if (!list || !list->head) {
        return NULL;
    }

    Node* current = list->head;
    Node* prev = NULL;

    while (current) {
        if (current->data == value) {
            void* data = current->data;

            if (prev == NULL) {
                list->head = current->next;
            } else {
                prev->next = current->next;
            }
            
            free(current);
            list->size--;
            return data;
        }

        prev = current;
        current = current->next;
    }

    return NULL; 
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

int main() {
    LinkedList list;
    init_list(&list);

    printf("=== Testing push_back ===\n");
    for (int i = 1; i <= 5; i++) {
        int* value = malloc(sizeof(int));
        *value = i;
        push_back(&list, value);
    }

    printf("Size after push_back: %lu\n", (unsigned long)list.size);

    printf("\n=== Testing insert at index 2 (value 99) ===\n");
    int* special = malloc(sizeof(int));
    *special = 99;
    insert(&list, 2, special);

    printf("Size after insert: %lu\n", (unsigned long)list.size);

    printf("\n=== Printing list ===\n");
    Node* current = list.head;
    while (current) {
        printf("%d ", *(int*)current->data);
        current = current->next;
    }
    printf("\n");

    printf("\n=== Testing erase at index 3 ===\n");
    int* erased = erase(&list, 3);
    printf("Erased value: %d\n", *erased);
    free(erased);

    printf("\n=== Testing pop_front ===\n");
    int* front_val = pop_front(&list);
    printf("Popped front: %d\n", *front_val);
    free(front_val);

    printf("\n=== Testing pop_back ===\n");
    int* back_val = pop_back(&list);
    printf("Popped back: %d\n", *back_val);
    free(back_val);

    printf("\n=== Testing value_n_from_end (n=1) ===\n");
    int* nth = value_n_from_end(&list, 1);
    printf("1 from end: %d\n", *nth);

    printf("\n=== Testing reverse ===\n");
    reverse(&list);

    printf("List after reverse:\n");
    current = list.head;
    while (current) {
        printf("%d ", *(int*)current->data);
        current = current->next;
    }
    printf("\n");

    printf("\n=== Testing remove_value (99) ===\n");
    remove_value(&list, special);
    free(special);

    printf("List after remove_value:\n");
    current = list.head;
    while (current) {
        printf("%d ", *(int*)current->data);
        current = current->next;
    }
    printf("\n");

    printf("\n=== Cleaning up remaining nodes ===\n");
    while (!empty(&list)) {
        int* val = pop_front(&list);
        free(val);
    }

    free_list(&list);

    printf("Final size: %lu\n", (unsigned long)list.size);
    printf("All tests completed successfully.\n");

    return 0;
}
