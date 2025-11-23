#include <string.h>
#include <stdbool.h>

#define UNUSED -1

bool startswith(char *s, char *target, int idx)
{
    int offset = 0;
    while (s[idx + offset] && target[offset] && s[idx + offset] == target[offset])
    {
        offset++;
    };
    return target[offset] == '\0';
}

bool _wordBreak(char *s, char **wordDict, int wordDictSize, int j, int *memo)
{
    if (memo[j] != UNUSED)
    {
        return memo[j];
    }
    if (j >= strlen(s))
    {
        return true;
    }
    for (int i = 0; i < wordDictSize; i++)
    {
        if (startswith(s, wordDict[i], j))
        {
            if (_wordBreak(s, wordDict, wordDictSize, j + strlen(wordDict[i]), memo))
            {
                memo[j] = true;
                return true;
            }
        }
    }
    memo[j] = false;
    return false;
}

bool wordBreak(char *s, char **wordDict, int wordDictSize)
{
    const int SIZE_S = 300;
    int *memo = (int *)malloc(SIZE_S * sizeof(int));
    // initialize as unused
    for (int i = 0; i < SIZE_S; i++)
    {
        memo[i] = UNUSED;
    }

    return _wordBreak(s, wordDict, wordDictSize, 0, memo);
}
