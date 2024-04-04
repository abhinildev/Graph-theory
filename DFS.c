#include<stdio.h>
#include<stdlib.h>

#define MAX_NODES 100

int visited[MAX_NODES];
int adjacency_matrix[MAX_NODES][MAX_NODES];
int num_nodes;

void dfs(int node) {
    visited[node] = 1;
    printf("%d ", node);

    for (int i = 0; i < num_nodes; i++) {
        if (adjacency_matrix[node][i] && !visited[i]) {
            dfs(i);
        }
    }
}

int main() {
    printf("Enter the number of nodes: ");
    scanf("%d", &num_nodes);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < num_nodes; j++) {
            scanf("%d", &adjacency_matrix[i][j]);
        }
    }

    printf("DFS Traversal: ");
    for (int i = 0; i < num_nodes; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    printf("\n");

    return 0;
}
