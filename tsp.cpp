// C++ program for the above approach
#include <bits/stdc++.h>
using namespace std;
// Function to find the minimum
// cost path for all the paths
bool isUsableForTSP(const vector<vector<int>> &graph)
{
    int n = graph.size(); // Number of vertices

    // Check for completeness and non-negative weights
    for (int i = 0; i < n; ++i)
    {
        if (graph[i].size() != n)
        {
            return false; // Graph is not complete
        }

        for (int j = 0; j < n; ++j)
        {
            if (i != j && graph[i][j] == -1)
            {
                return false; // Missing edge, so not complete
            }
            if (graph[i][j] < 0)
            {
                return false; // Negative weight found
            }
        }
    }
    return true; // Graph is complete and has non-negative weights
}
// given a matrix and start from position 0
vector<vector<int>> getInput()
{
    freopen("input.in", "r", stdin);
    vector<vector<int>> out;
    string line;
    string value;
    while (getline(cin, line))
    {
        stringstream ss(line);
        vector<int> vnum;
        while (ss >> value)
        {
            vnum.push_back(stoi(value));
        }
        out.push_back(vnum);
    }
    return out;
}
void getOutput(string message)
{
    freopen("output.out", "w", stdout);
    cout << message;
}
void findMinRoute(vector<vector<int>> tsp)
{
    int sum = 0;
    int counter = 0;
    int j = 0, i = 0;
    int min = INT_MAX;
    map<int, int> visitedRouteList;

    // Starting from the 0th indexed
    // city i.e., the first city
    visitedRouteList[0] = 1;
    int route[10000];

    // Traverse the adjacency
    // matrix tsp[][]
    while (i < tsp.size() && j < tsp[i].size())
    {

        // Corner of the Matrix
        if (counter >= tsp[i].size() - 1)
        {
            break;
        }

        // If this path is unvisited then
        // and if the cost is less then
        // update the cost
        if (j != i && (visitedRouteList[j] == 0))
        {
            if (tsp[i][j] < min)
            {
                min = tsp[i][j];
                route[counter] = j + 1;
            }
        }
        j++;

        // Check all paths from the
        // ith indexed city
        if (j == tsp[i].size())
        {
            sum += min;
            min = INT_MAX;
            visitedRouteList[route[counter] - 1] = 1;
            j = 0;
            i = route[counter] - 1;
            counter++;
        }
    }

    // Update the ending city in array
    // from city which was last visited
    i = route[counter - 1] - 1;

    for (j = 0; j < tsp.size(); j++)
    {

        if ((i != j) && tsp[i][j] < min)
        {
            min = tsp[i][j];
            route[counter] = j + 1;
        }
    }
    sum += min;

    // Started from the node where
    // we finished as well.
    stringstream message;
    message << sum << " ";
    message << "\n";

    for (int i = 0; i < tsp.size(); ++i)
    {
        message << route[i];
        message << " ";
    }

    getOutput(message.str());
}
// Function to check if graph is complete and has non-negative weights

int main()
{
    decltype(getInput()) g = getInput();
    // Example graph represented as an adjacency matrix

    if (isUsableForTSP(g))
    {
        cout << "The graph can be used for TSP." << endl;
        findMinRoute(g);
    }
    else
    {
        getOutput("The graph is not suitable for TSP.");
    }

    return 0;
}
