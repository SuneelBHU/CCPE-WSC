// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
  // [0,10,0,30,100],
    // [10,0,50,0,0],
    // [0,50,0,20,10],
    // [30,0,20,0,60],
    // [100,0,10,60,0]
contract SolutionPath {
    uint constant m = 5;
    uint constant n=m; //15;
    uint[n][n] public M;

    uint[m][m] public G;
    uint[n][n] public RG;
    uint entry = 0;
    uint[n][n] public cost; 
    bool[n] public visited;
    uint[n] public distance;
    uint[n] public pred;
    uint count;
    uint min_distance;
    uint next_node;
    uint[n][n] public path;
    uint[n] public desti;
    uint[n] public path_cost;
    uint constant dim=m;
    uint[dim][dim] AdjMx;
    // Function to input graph edges

    function GraphMatrix() public  returns (uint [5][5] memory ) {         
 
          uint256[5][5] memory predefinedValues = [
            [uint256(0), uint256(10), uint256(0), uint256(30), uint256(100)],
            [uint256(10), uint256(0), uint256(50), uint256(0), uint256(0)],
            [uint256(0), uint256(50), uint256(0), uint256(20), uint256(10)],
            [uint256(30), uint256(0), uint256(20), uint256(0), uint256(60)],
            [uint256(100), uint256(0), uint256(10), uint256(60), uint256(0)]  ];
        
            for (uint i = 0; i < m; i++) {
                for (uint j = 0; j < m; j++) {
                     G[i][j] = predefinedValues[i][j];
                   }
                }        
           return G;
  
           }

function Dijkstra_function(uint[n][n] memory graph) public returns (uint[n] memory, uint[n][n] memory) {
        uint start = 0;
        // Initialize the cost matrix
        for (uint p = 0; p < n; p++) {
            for (uint q = 0; q < n; q++) {
                if (G[p][q] == 0) {
                    cost[p][q] = 9999;
                } else {
                    cost[p][q] = graph[p][q];
                }
            }
        }
        // Initialize distance, pred, and visited arrays
        for (uint p = 0; p < n; p++) {
            distance[p] = cost[start][p];
            pred[p] = start;
            visited[p] = false;
        }

        distance[start] = 0;
        visited[start] = true;
        //visited[2]==true;

        count = 1;

        // Main loop of Dijkstra's algorithm
        while (count < n - 1 ) {

            min_distance = 9999;
            for (uint p = 0; p < n; p++) {
                if (distance[p] < min_distance && !visited[p]) {
                    min_distance = distance[p];
                    next_node = p;
                }
            }

            visited[next_node] = true;
            for (uint p = 0; p < n; p++) {
                if (!visited[p]) {
                    if (min_distance + cost[next_node][p] < distance[p]) {
                        distance[p] = min_distance + cost[next_node][p];
                        pred[p] = next_node;
                    }
                }
            }
            count++;
        }
        // Calculate the path and path costs
        for (uint i = 0; i < n; i++) {
            if (i != start) {
                desti[i] = i;
                path_cost[i] = distance[i];

                uint j = i;
                uint red = 0;
                while (j != start) {
                    path[i][red] = j;
                    j = pred[j];
                    red++;
                }
                path[i][red] = start;
            }
        }

        return (distance, path);
    }
    function main_function() public returns (uint[dim] memory, uint[dim][dim] memory){
     uint[dim][dim] memory cm=GraphMatrix();
      uint [dim] memory dist;
      uint [dim][dim] memory PATH;
      (dist,PATH)=Dijkstra_function(cm);


  return (dist,PATH);
    }
 }
