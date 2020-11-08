import os
import uuid

from gm.utils.datetime_ import now
from gm.utils.repo_path import repoPathManager


def _mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def _a_fname(fn, suffix):
    repo_path = repoPathManager()
    data_store_path = repo_path.output
    dn = now()
    _mkdir(os.path.join(data_store_path, dn))
    id = uuid.uuid4()
    print("this io stream session has id: {}".format(id))
    return os.path.join(
        data_store_path,
        dn,
        "{fn}_{id}.{suffix}".format(fn=fn, id=id, suffix=suffix),
    )


def write_txt(lines, filename):
    with open(_a_fname(filename, "txt"), "w", encoding="utf-8") as txt_file:
        for line in lines:
            txt_file.write(line + os.linesep)


def read_txt(filename):
    with open(filename, "r", encoding="utf-8") as txt_file:
        lines = txt_file.readlines()
        return [line.replace("\n", "") for line in lines]


def read_graph_from_txt_files(vertices_txt, edges_txt):
    from gm.graph import Edge, Graph, Vertex

    vertices = [
        Vertex(line.split(" ")[0], line.split(" ")[1])
        for line in read_txt(vertices_txt)
    ]
    edges = [
        Edge((line.split(" ")[0], line.split(" ")[1]), line.split(" ")[2])
        for line in read_txt(edges_txt)
    ]
    g = Graph()
    g.vertices = vertices
    g.edges = edges
    return g