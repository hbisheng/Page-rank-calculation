# Process graph and Initialize paramaters
N_TOTAL = len(open('node.map.utf8','rU').readlines())
MAX_NODE = 30000000
N_INGRAPH = 0
isolate_node = 0
ALPHA = 0.15
ITER = 30   
PR = []
I = []
term_ingraph = [] # end nodes in the graph
S = 0
for i in range(0, MAX_NODE):
    PR.append(0)
    I.append(0)
    
# Figure out the number of end nodes
f = open('wiki.graph','r')
text = f.readlines()
f.close()
for line in text:
    i = line.find(':')
    link_from = int(line[:i],10)
    PR[link_from] = 1.0 / N_TOTAL
    I[link_from] = ALPHA / N_TOTAL
    if len(line[i+1:].strip()) > 0:
        link_to_list = line[i+1:].strip().split(',')
        for item in link_to_list:
            link_to = int(item,10)
            I[link_to] = ALPHA / N_TOTAL            
for i in range(0, MAX_NODE):
    if I[i] != 0:
        N_INGRAPH += 1
        if PR[i] == 0:
            term_ingraph.append(i)
for term in term_ingraph:
    PR[term] = 1.0 / N_TOTAL

# Main loop
loop = 0
while loop < ITER:
    loop += 1
    print "LOOP:", loop
    for line in text:
        i = line.find(':')
        link_from = int(line[:i],10)
        if PR[link_from] == 0: # duplicate start page
            continue
        if len(line[i+1:].strip()) > 0:
            link_to_list = line[i+1:].strip().split(',')
            for item in link_to_list:
                link_to = int(item,10)
                I[link_to] += (1.0 - ALPHA) * PR[link_from] / len(link_to_list)
        PR[link_from] = 0
    for term in term_ingraph: # for terminal nodes
        S += PR[term]
    for n in range(0, MAX_NODE):
        if I[n] != 0:
            PR[n] = I[n] + (1.0 - ALPHA) * S / N_TOTAL
            I[n] = ALPHA / N_TOTAL
    S = 0
del I
        
# Get In and Out degree for each node
in_deg = []
out_deg = []
for n in range(0, MAX_NODE):
    in_deg.append(0)
    out_deg.append(0)
for line in text:
    i = line.find(':')
    link_from = int(line[:i],10)
    out_deg[link_from] = len(line[i+1:].strip())
    if len(line[i+1:].strip()) > 0:
        link_to_list = line[i+1:].strip().split(',')
        for item in link_to_list:
            link_to = int(item,10)
            in_deg[link_to] += 1
del text   
ans_list = []
for n in range(0, MAX_NODE):
    if PR[n] != 0:
        ans_list.append((n, PR[n]))
ans_list.sort(key = lambda x:x[1]) 
del PR

# Load entry name
f_node = open('node.map.utf8','r')
t_node = f_node.readlines()
f_node.close()
entry_map = {}
for t in t_node:
    name = t[:t.find('-')]
    id = int(t[t.find('>')+1:],10)
    entry_map[id] = name
del t_node

# Write out answers
f = open('result.csv','w')
f.write('Entry, PageRank, Indegree, Outdegree\n')
for ans in ans_list:
    f.write(str(entry_map[ans[0]]).replace(',',' ')+','+str(ans[1])+','+ str(in_deg[ans[0]]) + ',' + str(out_deg[ans[0]])+'\n')
f.close()