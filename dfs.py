from stack import Stack

result = Stack()
g = Stack()

def dfs(edges, vertex):
    result.push(vertex)
    g.push(vertex)
    p = g.get_item()
    while g.show_stack() != []:
        if p in edges.keys():
            if edges[p] != []:
                while edges[p] != []:
                    result.push(min(edges[p]))
                    g.push(min(edges[p]))
                    edges[p].remove(g.get_item())
                    p = g.get_item()
                    if p not in edges.keys():
                        edges[p] = []
            else:
                g.pop_value()
                p = g.get_item()
        else:
            g.pop_value()
            p = g.get_item()
                
def read_file():
    ed = {}
    with open('dfs-bfs-test.txt','r+') as ofs:
        str = ofs.readlines()
        for arc in str:
            temp = arc.split("->")
            f_element = temp[0].strip()
            s_element = temp[-1].strip()
            if f_element in ed:
                temp_list = ed[f_element]
                temp_list.append(s_element)
                ed[f_element] = temp_list
            else:
                ed[f_element] = [s_element]
    print (ed)
    # Start point
    dfs(ed, "S")
    print (result.show_stack())
    

def main():
    read_file()

if __name__ == "__main__":
    main()





#import sys

  #  file_name = sys.argv[1]
  #  f = open(file_name)
  #  data = f.read()
  #  f.close()


#import sys

 #   dfs-bfs-test = sys.argv[1]                 get the input file name 'dfs-bfs-text'
  #  dfs-test = open(dfs-bfs-test)              open the element in the file name 'dfs-bfs-text.txt'
  #  //g = test.read()                          read file and get into g, g is a data that contain vertex
  #  f.close() 