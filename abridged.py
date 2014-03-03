import re
import networkx as nx

def main():
	setup()

def setup():
        file = open('D:\CECS 328\mobysmall.txt', "r")
        G = nx.Graph()
        wordlist = []
        for line in file:
                line = line.lower()
                split = re.split('[. , ; : \' \n \" -- ?]', line)
                array = [x for x in split if x]
                for string in array:
                        if not string.isdigit():
                                wordlist.append(string)
        #for string in wordlist:
        #        print(string + "\n")
        for i in range(0, len(wordlist)-1):
                first = wordlist[i]
                second = wordlist[i+1]
                if not first in G:
                        G.add_node(first)
                        #print(first)
                if not second in G:
                        G.add_node(second)
                        #print(second)
                if first and second in G and not G.has_edge(first, second):
                        G.add_edge(first, second, weight = 1)
                        #print(G[first][second]['weight'])
                else:
                        G[first][second]['weight'] = G[first][second]['weight']+1
                        #print(G[first][second]['weight'])
        span = nx.minimum_spanning_tree(G)
        weight = 0
        #print(span.edges(data=True))
        for u,v,edata in span.edges(data=True):
                if 'weight' in edata:
                        weight += edata['weight']
        print(weight)
        
                
                        
                        
                
                
main()

