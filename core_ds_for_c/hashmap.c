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

void del(Map *m, char *k)
{
    m->used[hash(k)] = 0;
}

void drop(Map *m)
{
    free(m->vals);
    free(m->used);
    free(m);
}
