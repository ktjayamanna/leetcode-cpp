/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SZ 1000030

typedef struct
{
    int *vals;
    int *used;
} Map;

typedef enum
{
    NOT_FOUND,
    FOUND
} Status;

Map *create()
{
    Map *m = malloc(sizeof(Map));
    m->vals = malloc(SZ * sizeof(int));
    m->used = calloc(SZ, sizeof(int));
    return m;
}

unsigned hash(char *s)
{
    unsigned h = 5381;
    while (*s)
        h = h * 33 + *s++;
    return h % SZ;
}

void put(Map *m, char *k, int v)
{
    int i = hash(k);
    m->vals[i] = v;
    m->used[i] = 1;
}

Status get(Map *m, char *k, int *v)
{
    int i = hash(k);
    if (m->used[i])
    {
        *v = m->vals[i];
        return FOUND;
    }
    return NOT_FOUND;
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    // b = target - a
    *returnSize = 2;
    int b_idx, b;
    int *result = malloc((*returnSize) * sizeof(int));
    Map *seen = create();
    char key[12];

    for (int i = 0; i < numsSize; i++)
    {
        b = target - nums[i];
        sprintf(key, "%d", b);
        Status status = get(seen, key, &b_idx);
        if (status == FOUND && b_idx != i)
        {
            result[0] = i;
            result[1] = b_idx;
            return result;
        }
        else
        {
            sprintf(key, "%d", nums[i]);
            put(seen, key, i);
        }
    }
    free(seen);
    return result;
}