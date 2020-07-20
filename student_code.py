import math
import heapq


def cal_dist(graph, point_a, point_b):
    """
    This function calculate the distance
    between two points.

    :param graph: A Map object
    :param point_a: Vertex represented as an Integer
    :param point_b: Vertex represented as an Integer
    :return: (float) Distance between two points.
    """
    a_coord = graph.intersections[point_a]
    b_coord = graph.intersections[point_b]
    x_a = a_coord[0]
    y_a = a_coord[1]

    x_b = b_coord[0]
    y_b = b_coord[1]

    return math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)


def _assemble_path(goal, vertices):
    """
    Assembles a route from destination vertex
    to goal vertex.

    :param goal: Vertex represented as an Integer
    :param vertices: Dict of destination vertices to origin vertices.
    :return: A list of integer vertices.
    """
    path = []
    curr_vertex = goal

    while curr_vertex is not None:
        path.append(curr_vertex)
        curr_vertex = vertices[curr_vertex]

    path.reverse()
    return path


def shortest_path(graph, start, goal):
    """
    Transverses the graph to find the shortest path
    using the A*.
    :param graph: A Map object
    :param start: Vertex represented as an Integer
    :param goal:  Vertex represented as an Integer
    :return: A list of vertices from start to goal
    """
    open_vertices = set()
    open_vertices.add(start)

    closed_vertices = set()
    min_list = []
    prev_vertex = {start: None}

    f_value = cal_dist(graph, start, goal)
    f_values = {start: f_value}
    g_values = {start: 0}

    curr_vertex = start
    while curr_vertex != goal:

        for next_vertex in graph.roads[curr_vertex]:
            if next_vertex not in closed_vertices:
                open_vertices.add(next_vertex)
                g = cal_dist(graph, curr_vertex, next_vertex) + g_values[curr_vertex]
                h = cal_dist(graph, next_vertex, goal)
                f_new = g + h

                if next_vertex not in f_values or f_new < f_values[next_vertex]:
                    g_values[next_vertex] = g
                    f_values[next_vertex] = f_new
                    heapq.heappush(min_list, (f_new, next_vertex))
                    prev_vertex[next_vertex] = curr_vertex

        open_vertices.remove(curr_vertex)
        closed_vertices.add(curr_vertex)
        curr_vertex = heapq.heappop(min_list)[1]

    path = _assemble_path(curr_vertex, prev_vertex)
    print("shortest path called")
    return path
