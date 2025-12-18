#include <stdbool.h>
#include <stdlib.h>
#define SIZE 200003

typedef struct Node
{
    int key;
    struct Node *next;
} Node;

Node *set[SIZE];

int hash(int x)
{
    return ((x % SIZE) + SIZE) % SIZE;
}

int add(int x)
{
    int h = hash(x);
    for (Node *p = set[h]; p; p = p->next)
    {
        if (p->key == x)
            return 1;
    }
    Node *n = malloc(sizeof *n);
    n->key = x;
    n->next = set[h];
    set[h] = n;
    return 0;
}

bool containsDuplicate(int *nums, int numsSize)
{
    memset(set, 0, sizeof(set));
    for (int i = 0; i < numsSize; i++)
    {
        if (add(nums[i]) == 1)
            return 1;
    }
    return 0;
}