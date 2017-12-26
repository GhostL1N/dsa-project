from queue import Queue

result = Queue()
g = Queue()

def bfs(edges, vertex):
    result.queue(vertex)
    g.queue(vertex)
    while g.show_queue() != []:
        p = g.get_item()
        if p in edges.keys():
            while edges[p] != []:
                g.queue(min(edges[p]))
                result.queue(min(edges[p]))
                edges[p].remove((min(edges[p])))
        g.dequeue()

def read_file():
    ed = {}
    with open('dfs-bfs-test.txt','r+') as ofs:
        str1 = ofs.readlines()
        for arc in str1:
            temp = arc.split("->")
            f_element = temp[0].strip()
            s_element = temp[-1].strip()
            if f_element in ed:
                temp_list = ed[f_element]
                temp_list.append(s_element)
                ed[f_element] = temp_list
            else:
                ed[f_element] = [s_element]
    bfs(ed, "S")
    print (result.show_queue()[::1])
    

def main():
    read_file()

if __name__ == "__main__":
    main()