void Topsort(Graph G)
{
    int Counter;
    Vertex V, W;

    for (Counter = 0; Counter < NumVertex; Counter++) {
        V = FindNewVertexOfIndegreeZero();
        if (V = NotAVertex) {
            Error("Graph has a cycle");
            break;
        }
        TopNum[V] = Counter;
        for each W adjancent to V
            Indegree[W]--;
    }
}
