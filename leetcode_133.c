#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

struct Node
{
    int val;
    int numNeighbors;
    struct Node **neighbors;
};

// Your cloneGraph solution
struct Node *_cloneGraph(struct Node *s, struct Node **visited)
{
    if (s == NULL)
    {
        return NULL;
    }
    if (visited[s->val] != NULL)
    {
        return visited[s->val];
    }
    struct Node *current_node = malloc(sizeof(struct Node));
    current_node->val = s->val;
    current_node->numNeighbors = s->numNeighbors;
    current_node->neighbors = malloc(s->numNeighbors * sizeof(struct Node *));
    visited[s->val] = current_node;
    for (int i = 0; i < s->numNeighbors; i++)
    {
        current_node->neighbors[i] = _cloneGraph(s->neighbors[i], visited);
    }
    return current_node;
}

struct Node *cloneGraph(struct Node *s)
{
    if (s == NULL)
    {
        return NULL;
    }
    struct Node *result = malloc(sizeof(struct Node));
    result->val = s->val;
    result->numNeighbors = s->numNeighbors;
    result->neighbors = malloc(s->numNeighbors * sizeof(struct Node *));
    struct Node *visited[101] = {NULL};
    visited[s->val] = result;

    for (int i = 0; i < s->numNeighbors; i++)
    {
        result->neighbors[i] = _cloneGraph(s->neighbors[i], visited);
    }
    return result;
}

// Leetcode's hidden test runner code below

// Build graph from adjacency list
struct Node *buildGraphFromAdjList(int adjList[][2], int numNodes)
{
    if (numNodes == 0)
        return NULL;

    struct Node **nodes = malloc((numNodes + 1) * sizeof(struct Node *));
    for (int i = 0; i <= numNodes; i++)
    {
        nodes[i] = NULL;
    }

    for (int i = 0; i < numNodes; i++)
    {
        int nodeVal = i + 1;
        nodes[nodeVal] = malloc(sizeof(struct Node));
        nodes[nodeVal]->val = nodeVal;
        nodes[nodeVal]->numNeighbors = 2;
        nodes[nodeVal]->neighbors = malloc(2 * sizeof(struct Node *));
    }

    for (int i = 0; i < numNodes; i++)
    {
        int nodeVal = i + 1;
        for (int j = 0; j < 2; j++)
        {
            int neighborVal = adjList[i][j];
            nodes[nodeVal]->neighbors[j] = nodes[neighborVal];
        }
    }

    return nodes[1];
}

// Graph comparison function
int isSameGraph(struct Node *original, struct Node *clone)
{
    if (original == NULL && clone == NULL)
        return 1;
    if (original == NULL || clone == NULL)
        return 0;

    struct Node *visited_orig[101] = {NULL};
    struct Node *visited_clone[101] = {NULL};
    struct Node *queue_orig[100];
    struct Node *queue_clone[100];
    int front = 0, rear = 0;

    queue_orig[rear] = original;
    queue_clone[rear] = clone;
    rear++;

    visited_orig[original->val] = original;
    visited_clone[clone->val] = clone;

    while (front < rear)
    {
        struct Node *curr_orig = queue_orig[front];
        struct Node *curr_clone = queue_clone[front];
        front++;

        if (curr_orig == curr_clone)
        {
            printf("ERROR: Same object found! Not a deep copy.\n");
            return 0;
        }
        if (curr_orig->val != curr_clone->val)
        {
            printf("ERROR: Value mismatch: %d vs %d\n", curr_orig->val, curr_clone->val);
            return 0;
        }
        if (curr_orig->numNeighbors != curr_clone->numNeighbors)
        {
            printf("ERROR: Neighbor count mismatch for node %d: %d vs %d\n",
                   curr_orig->val, curr_orig->numNeighbors, curr_clone->numNeighbors);
            return 0;
        }

        for (int i = 0; i < curr_orig->numNeighbors; i++)
        {
            struct Node *orig_neighbor = curr_orig->neighbors[i];
            struct Node *clone_neighbor = curr_clone->neighbors[i];

            if (orig_neighbor->val != clone_neighbor->val)
            {
                printf("ERROR: Neighbor value mismatch: %d vs %d\n",
                       orig_neighbor->val, clone_neighbor->val);
                return 0;
            }

            if (visited_orig[orig_neighbor->val] == NULL)
            {
                visited_orig[orig_neighbor->val] = orig_neighbor;
                visited_clone[clone_neighbor->val] = clone_neighbor;
                queue_orig[rear] = orig_neighbor;
                queue_clone[rear] = clone_neighbor;
                rear++;
            }
        }
    }

    return 1;
}

// Print graph for debugging
void printGraph(struct Node *node, const char *name)
{
    if (!node)
        return;

    printf("%s:\n", name);
    struct Node *visited[101] = {NULL};
    struct Node *queue[100];
    int front = 0, rear = 0;

    queue[rear++] = node;
    visited[node->val] = node;

    while (front < rear)
    {
        struct Node *current = queue[front++];
        printf("  Node %d: [", current->val);
        for (int i = 0; i < current->numNeighbors; i++)
        {
            printf("%d", current->neighbors[i]->val);
            if (i < current->numNeighbors - 1)
                printf(", ");

            if (visited[current->neighbors[i]->val] == NULL)
            {
                visited[current->neighbors[i]->val] = current->neighbors[i];
                queue[rear++] = current->neighbors[i];
            }
        }
        printf("]\n");
    }
}

// FIXED: Safer free graph function
void freeGraph(struct Node *node)
{
    if (!node)
        return;

    // First pass: collect all unique nodes
    struct Node *allNodes[101] = {NULL};
    struct Node *queue[100];
    int front = 0, rear = 0;
    int nodeCount = 0;

    queue[rear++] = node;
    allNodes[node->val] = node;
    nodeCount++;

    while (front < rear)
    {
        struct Node *current = queue[front++];

        for (int i = 0; i < current->numNeighbors; i++)
        {
            if (allNodes[current->neighbors[i]->val] == NULL)
            {
                allNodes[current->neighbors[i]->val] = current->neighbors[i];
                queue[rear++] = current->neighbors[i];
                nodeCount++;
            }
        }
    }

    // Second pass: free all nodes safely
    for (int i = 1; i <= 100; i++)
    {
        if (allNodes[i] != NULL)
        {
            free(allNodes[i]->neighbors);
            free(allNodes[i]);
        }
    }
}

// LeetCode's hidden test runner code
int main()
{
    printf("=== LeetCode Test Runner Simulation ===\n");

    // 1. Parse test case: [[2,4],[1,3],[2,4],[1,3]]
    int adjList[4][2] = {{2, 4}, {1, 3}, {2, 4}, {1, 3}};
    printf("1. Parsed adjacency list: [[2,4],[1,3],[2,4],[1,3]]\n");

    // 2. Build actual graph structure
    struct Node *originalGraph = buildGraphFromAdjList(adjList, 4);
    printf("2. Built original graph structure\n");
    printGraph(originalGraph, "Original Graph");

    // 3. Call YOUR function
    printf("3. Calling cloneGraph()...\n");
    struct Node *clonedGraph = cloneGraph(originalGraph);
    printf("   Clone completed\n");
    printGraph(clonedGraph, "Cloned Graph");

    // 4. Validate result
    printf("4. Validating result...\n");
    int isValid = isSameGraph(originalGraph, clonedGraph);
    assert(isValid);
    printf("Validation PASSED: Graphs are identical in structure but different objects!\n");

    // 5. Memory cleanup
    printf("5. Cleaning up memory...\n");
    freeGraph(originalGraph);
    freeGraph(clonedGraph);
    printf("Test case completed successfully!\n");

    return 0;
}