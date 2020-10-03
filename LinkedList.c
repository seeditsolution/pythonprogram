//Linked List Implementation code
#include <stdio.h>
#include <stdlib.h>
//stdlib is included because we will be using  ‘malloc’

// creating a node in linked list
struct Node { 
    int data; 
    struct Node* next; 
    // Pointer pointing towards next node
};

//function to print the linked list
void display(struct Node* node) 
{ 
    while (node != NULL) { 
        printf(" %d ", node->data); 
        node = node->next; 
    } 
}

// main function
int main() 
{ 
    //creating 4 pointers of type struct Node
    //So these can point to address of struct type variable
    struct Node* head = NULL; 
    struct Node* node2 = NULL; 
    struct Node* node3 = NULL; 
    struct Node* node4 = NULL; 

    // allocate 3 nodes in the heap 
    head =  (struct Node*)malloc(sizeof(struct Node)); 
    node2 = (struct Node*)malloc(sizeof(struct Node)); 
    node3 = (struct Node*)malloc(sizeof(struct Node)); 
    node4 = (struct Node*)malloc(sizeof(struct Node)); 

   
    head->data = 10; // data set for head node 
    head->next = node2; // next pointer assigned to address of node2 

    node2->data = 20; 
    node2->next = node3; 

    node3->data = 30;
    node3->next = node4; 

    node4->data = 40;
    node4->next = NULL; 
   

    display(head);

    return 0; 
}
