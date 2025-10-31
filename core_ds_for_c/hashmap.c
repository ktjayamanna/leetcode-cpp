#include <stdlib.h>
#include <string.h>

#define SZ 1000030

typedef struct
{
    int *vals;
    int *used;
} Map;

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

int get(Map *m, char *k)
{
    int i = hash(k);
    return m->used[i] ? m->vals[i] : -1;
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