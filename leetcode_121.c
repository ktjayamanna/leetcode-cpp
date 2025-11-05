int max(int a, int b)
{
    return a > b ? a : b;
}

int maxProfit(int *prices, int pricesSize)
{

    int left = 0, right = 0, current_profit = 0;
    while (right < pricesSize)
    {
        if (prices[right] < prices[left])
        {
            left = right;
        }
        else
        {
            current_profit = max(
                current_profit, prices[right] - prices[left]);
        }
        right++;
    }
    return current_profit;
}

int main()
{
    int prices[] = {7, 1, 5, 3, 6, 4};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    int result = maxProfit(prices, pricesSize);
    printf("%d\n", result);
    return 0;
}