#include <limits.h>
#include <stdlib.h>
#include <string.h>

#define min(a, b) ((a) < (b) ? (a) : (b))
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

int _coinChange(int *coins, int coinsSize, int amount, Map *memo)
{
    char key[12];
    sprintf(key, "%d", amount);

    if (get(memo, key) != -1)
    {
        return get(memo, key);
    }

    if (amount == 0)
    {
        return 0;
    }
    if (amount < 0)
    {
        return INT_MAX;
    }
    unsigned int coinsNeeded = INT_MAX;
    int tmp;
    for (int i = 0; i < coinsSize; i++)
    {
        tmp = _coinChange(coins, coinsSize, amount - coins[i], memo);
        coinsNeeded = min(
            tmp,
            coinsNeeded);
    }
    if (coinsNeeded != INT_MAX)
    {
        coinsNeeded++;
    }
    put(memo, key, coinsNeeded);
    return coinsNeeded;
}

int coinChange(int *coins, int coinsSize, int amount)
{
    Map *memo = create();
    int result = _coinChange(coins, coinsSize, amount, memo);
    free(memo);
    return result == INT_MAX ? -1 : result;
}