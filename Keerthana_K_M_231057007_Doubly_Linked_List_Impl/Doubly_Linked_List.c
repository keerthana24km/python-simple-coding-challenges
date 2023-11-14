#include<stdio.h>  
#include<stdlib.h> 
 
struct node  
{  
    struct node *prev;  
    struct node *next;  
    int data;  
};  
struct node *head;  
void insertion_beginning();  
void insertion_last();  
void insertion_specified();  
void deletion_beginning();  
void deletion_last();  
void deletion_specified();  
void display();
 
void main()  
{  
int choice = 0;  
    while(choice != 8)  
    {  
        printf("*****Menu*****\n");  
        printf("Enter the choice\n");  
        printf("------------------\n");  
        printf("1.Insert in begining\n2.Insert at last\n3.Insert at a given index\n4.Delete from Beginning\n5.Delete from last\n6.Delete the node at given index\n7.Display\n8.Quit\n");  
        printf("Enter your choice?\n");  
        scanf("%d",&choice);  
        switch(choice)  
        {  
            case 1:  
            	insert_at_beginning();  
            	break;  
            case 2:  
            	insert_at_last();  
            	break;  
            case 3:  
            	insert_at_index();  
            	break;  
            case 4:  
            	delete_at_beginning();  
            	break;  
            case 5:  
            	delete_at_last();  
            	break;  
            case 6:  
            	delete_at_index();  
            	break;  
            case 7:  
            	display();  
            	break;  
            case 8:  
            	exit(0);  
            	break;  
            default:  
            	printf("Please enter valid choice..");  
        }  
    }  
}  
void insert_at_beginning()  
{  
   struct node *ptr;   
   int val;  
   ptr = (struct node *)malloc(sizeof(struct node));  
   if(ptr == NULL)  
   {  
       printf("Overflow\n");  
   }  
   else  
   {  
    printf("\nEnter the value : ");  
    scanf("%d",&val);  
      
   	if(head==NULL)  
   	{  
       		ptr->next = NULL;  
       		ptr->prev=NULL;  
       		ptr->data=val;  
       		head=ptr;  
   	}  
   	else   
   	{  
       		ptr->data=val;  
       		ptr->prev=NULL;  
       		ptr->next = head;  
       		head->prev=ptr;  
       		head=ptr;  
   	}  
   printf("Node inserted\n");  
   }    
} 
 
void insert_at_last()  
{  
   struct node *ptr,*temp;  
   int val;  
   ptr = (struct node *) malloc(sizeof(struct node));  
   if(ptr == NULL)  
   {  
       printf("Overflow\n");  
   }  
   else  
   {  
       printf("\nEnter value : ");  
       scanf("%d",&val);  
        ptr->data=val;  
       if(head == NULL)  
       {  
           ptr->next = NULL;  
           ptr->prev = NULL;  
           head = ptr;  
       }  
       else  
       {  
          temp = head;  
          while(temp->next!=NULL)  
          {  
              temp = temp->next;  
          }  
          temp->next = ptr;  
          ptr ->prev=temp;  
          ptr->next = NULL;  
          }  
             
       }  
     printf("Node inserted\n");  
} 
 
void insert_at_index()  
{  
   struct node *ptr,*temp;  
   int val,loc,i;  
   ptr = (struct node *)malloc(sizeof(struct node));  
   if(ptr == NULL)  
   {  
       printf("Overflow\n");  
   }  
   else  
   {  
       temp=head;  
       printf("Enter the location");  
       scanf("%d",&loc);  
       for(i=0;i<loc;i++)  
       {  
           temp = temp->next;  
           if(temp == NULL)  
           {  
               printf("There are less than %d elements", loc);  
               return;  
           }  
       }  
       printf("Enter value : ");  
       scanf("%d",&val);  
       ptr->data = val;  
       ptr->next = temp->next;  
       ptr -> prev = temp;  
       temp->next = ptr;  
       temp->next->prev=ptr;  
       printf("Node inserted\n");  
   }  
}  

void delete_at_beginning()  
{  
    struct node *ptr;  
    if(head == NULL)  
    {  
        printf("Underflow\n");  
    }  
    else if(head->next == NULL)  
    {  
        head = NULL;   
        free(head);  
        printf("Node deleted\n");  
    }  
    else  
    {  
        ptr = head;  
        head = head -> next;  
        head -> prev = NULL;  
        free(ptr);  
        printf("Node deleted\n");  
    }  
  
}  

void delete_at_last()  
{  
    struct node *ptr;  
    if(head == NULL)  
    {  
        printf("Underflow\n");  
    }  
    else if(head->next == NULL)  
    {  
        head = NULL;   
        free(head);   
        printf("Node deleted\n");  
    }  
    else   
    {  
        ptr = head;   
        if(ptr->next != NULL)  
        {  
            ptr = ptr -> next;   
        }  
        ptr -> prev -> next = NULL;   
        free(ptr);  
        free(ptr->next);
        printf("Node deleted\n");  
    }  
} 
 
void delete_at_index()  
{  
    struct node *ptr, *temp;  
    int val;  
    printf("Enter the data after which the node is to be deleted : ");  
    scanf("%d", &val);  
    ptr = head;  
    while(ptr -> data != val)  
    ptr = ptr -> next;  
    if(ptr -> next == NULL)  
    {  
        printf("\nCannot delete the node\n");  
    }  
    else if(ptr -> next -> next == NULL)  
    {  
        ptr ->next = NULL;  
        printf("\nNode deleted\n");
    }  
    else  
    {   
        temp = ptr -> next;  
        ptr -> next = temp -> next;  
        temp -> next -> prev = ptr;  
        free(temp);  
        printf("\nNode deleted\n");  
    }     
}  

void display()  
{  
    struct node *ptr;  
    printf("Printing values...\n");  
    ptr = head;  
    while(ptr != NULL)  
    {  
        printf("%d\n",ptr->data);  
        ptr = ptr->next;  
    }  
}  