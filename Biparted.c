#include <stdio.h>

#define MAX_NODES 100

int adj_matrix[MAX_NODES][MAX_NODES];

void initialize_graph(int num_nodes1, int num_nodes2) {
    
    for (int i = 0; i < num_nodes1 + num_nodes2; i++) {
        for (int j = 0; j < num_nodes1 + num_nodes2; j++) {
            adj_matrix[i][j] = 0;
        }
    }
}

void add_edge(int u, int v) {

    adj_matrix[u][v] = 1;
    adj_matrix[v][u] = 1; 
}

void print_adj_matrix(int num_nodes1, int num_nodes2) {
   
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < num_nodes1 + num_nodes2; i++) {
        for (int j = 0; j < num_nodes1 + num_nodes2; j++) {
            printf("%d ", adj_matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int num_nodes1 = 3; 
    int num_nodes2 = 3; 

    initialize_graph(num_nodes1, num_nodes2);
    add_edge(0, 3);
    add_edge(0, 4);
    add_edge(1, 4);
    add_edge(1, 5);
    add_edge(2, 5);

    print_adj_matrix(num_nodes1, num_nodes2);

    return 0;
}
