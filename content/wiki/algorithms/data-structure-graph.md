---
title: "Data Structure: Graph"
summary: "mind the data structure: here comes the graph"
date: 2018-03-27
category:
- 'Algorithms'
tags:
- 'Graph'
- 'Data Structure'
- 'Basics'
links:
  - wiki/algorithms/data-structure.md
weight: 4
---

Complex systems such as social networks are easier to manipulate in computers if we model them as graphs.

The follow code is an example of people connected by interests. Given the nodes and edges, we can find who share the same interests.


```python
from itertools import combinations


class Graph(object):
    """A graph object
    """

    def __init__(self, source_nodes, target_nodes, weights=None):

        if not isinstance(source_nodes, list):
            raise TypeError('source_nodes should be a list')

        if not isinstance(target_nodes, list):
            raise TypeError('target_nodes should be a list')

        if not (weights is None):
            if not isinstance(weights, list):
                raise TypeError('weights should be a list if exists otherwise should be None')

        self.source_nodes = source_nodes
        self.target_nodes = target_nodes
        self.weights = weights

        # calculate all possible nodes in the Graph
        self._nodes = self.__calculate_nodes(source_nodes, target_nodes)
        # calculate edges
        self._edges = self.__calculate_edges(source_nodes, target_nodes, weights)

    def __calculate_nodes(self, source_nodes, target_nodes):
        """calculate all the nodes from source list and target list
        """
        return list(set(self.source_nodes + self.target_nodes))

    def __calculate_edges(self, source_nodes, target_nodes, weights):
        """calculate all the nodes from source list and target list and weights if exists
        """
        edges = None
        if weights:
            edges = list(zip(source_nodes, target_nodes, weights))
        else:
            edges = list(zip(source_nodes, target_nodes))
        return edges

    @property
    def nodes(self):
        self._nodes = self.__calculate_nodes(self.source_nodes, self.target_nodes)
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        if not isinstance(nodes, (list, set)):
            raise TypeError('nodes are represented by a list')
        else:
            self._nodes = nodes

    @nodes.deleter
    def nodes(self):
        del self._nodes

    @property
    def edges(self):
        self._edges = self.__calculate_edges(self.source_nodes, self.target_nodes, self.weights)
        return self._edges

    @edges.setter
    def edges(self, edges):
        if not isinstance(edges, (list, set)):
            raise TypeError('edges are represented by a list')
        else:
            self._edges = edges

    @edges.deleter
    def edges(self):
        del self._edges

    def add_edges(self, new_sources, new_targets, new_weights):
        """add new edges to the graph
        """
        self.source_nodes = self.source_nodes + new_sources
        self.target_nodes = self.target_nodes + new_targets
        if self.weights is None:
            raise Exception('This graph has no weights assigned')
        else:
            self.weights = self.weights + new_weights

    def nodes_by_weight(self):
        """Find all nodes for each weight
        """

        weight_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = i[:2]

            i_weight_nodes = weight_dict.get(i_weight, [])

            for i_node in i_edge:
                if i_node not in i_weight_nodes:
                    i_weight_nodes.append(i_node)

            weight_dict[i_weight] = i_weight_nodes

        return weight_dict

    def edges_by_weight(self):
        """Find all edges for each weight
        """

        weight_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = tuple(sorted(i[:2]))

            i_weight_edges = weight_dict.get(i_weight, [])

            if i_edge not in i_weight_edges:
                i_weight_edges.append(i_edge)

            weight_dict[i_weight] = i_weight_edges

        return weight_dict

    def weigts_by_node_comb(self):
        """Find all the weights for each combination of nodes
        """
        edge_dict = {}
        for i in self.edges:
            i_weight = i[-1]
            i_edge = tuple(sorted(i[:2]))

            i_edge_weights = edge_dict.get(i_edge, [])

            if i_weight not in i_edge_weights:
                i_edge_weights.append(i_weight)

            edge_dict[i_edge] = i_edge_weights

        return edge_dict

    def __str__(self):
        return f"nodes: {self.nodes}\nedges: {self.edges}"




class Interests():
    """An object for a group of people connected by interests
    """

    def __init__(self, users_1, users_2, interests):
        # super().__init__(users_1, users_2, interests)
        self.interest_graph = Graph(users_1, users_2, interests)

    @staticmethod
    def _reconstruct_edges_from_nodes(nodes):
        """Given a list of nodes, construct all possible edges
        """
        return list(combinations(sorted(nodes), 2))

    def construct_full_interest_graph(self):
        """Calculates the full interest graph
        If 1 and 2 share interest A and 2 and 3 share interest A too,
        we will connect 1 and 3 with interest A.
        """

        nodes_by_interests = self.interest_graph.nodes_by_weight()

        full_interest_graph = Graph([], [], [])

        for interest, nodes in nodes_by_interests.items():
            for edge in self._reconstruct_edges_from_nodes(nodes):
                full_interest_graph.add_edges([edge[0]], [edge[1]], [interest])

        self.full_interest_graph = full_interest_graph

        return full_interest_graph


if __name__ == '__main__':
    source_nodes = [1, 1, 2, 3, 2]
    target_nodes = [2, 3, 4, 5, 4]
    interests = ['A', 'B', 'A', 'C', 'B']

    it = Interests(source_nodes, target_nodes, interests)
    print(it.interest_graph)

    print(it._reconstruct_edges_from_nodes([1,2,3, 5,4]))

    print('full graph\n', it.construct_full_interest_graph())

    print('full graph weight by node combinations:\n',it.full_interest_graph.weigts_by_node_comb())

    print('full graph nodes_by_weight:\n', it.full_interest_graph.nodes_by_weight())

    print('full graph edges_by_weight:\n', it.full_interest_graph.edges_by_weight())
```