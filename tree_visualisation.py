from ete3 import Tree, TreeStyle, NodeStyle, CircleFace, faces, re

chromosome_list = ["1","2","3","4","5", "6","7","8"] #lists for colouring by chomosome
chrcolours = ["blue","red","orange","purple","yellow","cyan","DeepPink","navy"] #colours by which nodes are annotated based on chromosome

capsella = ["capsella160","capsella175"] #list of capsella sequences used as root for mega-tree in Figure x

def multiple_replace(string, rep_dict): #function for replacing strings with other strings, necessary for processing node names
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

#set colour of node by what chromosome the sequence is from
def chromosome(n):
    if n.support >= 95 and not n.is_leaf(): #show support only for non-leaves
        C = CircleFace(radius=200000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind") #add circular face to node if branch support is >95%
    tokens = n.name
    if n.is_leaf() and tokens not in capsella:
        tokens1 = multiple_replace(tokens, {"cen180_":"","_scafNT1":"","t2t_":"","_8chr":""}) #clean up the node name
        tokens2 = (tokens1).split("_") #split up the information in the node name
        accname = tokens2[0] #accession name is first item in list
        fullchromosome = tokens2[1] #chromosome is the second item in the list
        chromosome = fullchromosome.replace("Chr", "") #remove 'chr' so only has the number
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000


        #make lyratas black
        lyratas = ["MN47Hifi","SiberianAly"] #list of Arabidopsis lyrata accessions used
        style2 = NodeStyle() #create style used for annotating lyrata nodes
        style2["shape"] = "square"
        style2["size"] = 70000
        style2["fgcolor"] = "black"
        style2["vt_line_color"] = "black"
        style2["hz_line_color"] = "black"
        if accname in lyratas:
            n.set_style(style2) #set lyrata nodes to black colour

        if accname not in lyratas:
            for i in chromosome_list: #loop through list of chromosomes
                if chromosome == i: #if the chr in the name matches the chromosome type in the list
                    style["fgcolor"] = chrcolours[chromosome_list.index(i)]
                    style["vt_line_color"] = chrcolours[chromosome_list.index(i)]
                    style["hz_line_color"] = chrcolours[chromosome_list.index(i)]
                    n.set_style(style)  # set style of node to that colour



byacc = [["at6137.scaffolds.bionano.final"],["at9336.scaffolds.bionano.final"],
            ["at9830.scaffolds.bionano.final"], ["at9578.scaffolds.bionano.final"],
         ["MONTM-B-7.ragtag"], ["PREI-A-14.ragtag"]] #list of Arabidopsis accessions to be coloured
discolours = ["Magenta","MediumBlue","turquoise","Saddlebrown", "red", "yellow"] #colours which accessions are annotated with

#set colour of node by the accession it is
def byaccession(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")
    tokens = n.name
    tokens = tokens.replace("t2t_", "")
    tokens2 = (tokens).split("_")
    style = NodeStyle()

    for i in byacc: #loop through accession list
        if len(i) == 1:
            if i[0] in tokens2: #if accession name matches one of list items from separated node name
                style["fgcolor"] = discolours[byacc.index(i)]
                style["vt_line_color"] = discolours[byacc.index(i)]
                style["hz_line_color"] = discolours[byacc.index(i)]
                style["size"] = 70000
                n.set_style(style)




grcolours = ["black","red","yellow","blue"] #colours to set groups

group = [["SiberianAly", "MN47Hifi"], #lyratas
        [ "Tanz-1.patch.scaffold.Chr.fa", "22005.patch.scaffold.Chr.fa"], #african
        ["at6137.scaffolds.bionano.final", "at9578.scaffolds.bionano.final","at9336.scaffolds.bionano.final",  "at9830.scaffolds.bionano.final"], #eurasian
        ["Alo-19.ragtag", "Cas-6.ragtag" ]]#relict
#list of which accessions are in which group, groups being lyratas, african thalianas, eurasian thalianas and relict thalianas

#set colour of node by what group the sequence is from
def bygroup(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")
    tokens = n.name
    tokens1 = multiple_replace(tokens,{"cen180_": "", "_scafNT1": "", "t2t_": "", "_8chr": ""})  # clean up the node name
    tokens2 = (tokens1).split("_")  # split up the information in the node name
    style = NodeStyle()
    style["fgcolor"] = "black"
    style["vt_line_color"] = "black"
    style["hz_line_color"] = "black"
    style["size"]= 70000
    for i in group:
        if tokens2[0] in i:
            style["fgcolor"] = grcolours[group.index(i)]
            style["vt_line_color"] = grcolours[group.index(i)]
            style["hz_line_color"] = grcolours[group.index(i)]
            style["size"] = 70000
            n.set_style(style)


lencolours = ["navy","cyan","yellow","red"]

#set colour of node by the repeat type it is, i.e AtCEN160/ AtCEN178/ AlCEN170/ AlCEN180. Done by the length of the sequence.
def bylen(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=300000, color="DimGray", style="sphere") #250000 for most #200000 for t2t all
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")
    tokens = n.name
    tokens1 = multiple_replace(tokens,
                               {"cen180_": "", "_scafNT1": "", "t2t_": "", "_8chr": ""})  # clean up the node name
    tokens2 = (tokens1).split("_")  # split up the information in the node name
    accname = tokens2[0]
    lyratas = ["MN47Hifi", "SiberianAly"]

    style = NodeStyle()

    if tokens not in capsella:
        if n.is_leaf and len(tokens2[-1]) > 1 and accname not in lyratas: #set colours of thaliana sequences
            leng = tokens2[-1].replace(" ","") #find length of sequence
            if 155 <= int(leng) <= 160:
                style["fgcolor"] = "yellow"
                style["vt_line_color"] = "yellow"
                style["hz_line_color"] = "yellow"
                style["size"] = 70000
                n.set_style(style)
            elif 175 <= int(leng) <= 180:
                style["fgcolor"] = "red"
                style["vt_line_color"] = "red"
                style["hz_line_color"] = "red"
                style["size"] = 70000
                n.set_style(style)

        if n.is_leaf and len(tokens2[-1]) > 1 and accname in lyratas: #set colour of lyrata sequences
            leng = tokens2[-1].replace(" ","")
            if 165 <= int(leng) <= 170:
                style["fgcolor"] = "navy"
                style["vt_line_color"] = "navy"
                style["hz_line_color"] = "navy"
                style["size"] = 70000
                n.set_style(style)
            elif 175 <= int(leng) <= 180:
                style["fgcolor"] = "cyan"
                style["vt_line_color"] = "cyan"
                style["hz_line_color"] = "cyan"
                style["size"] = 70000
                n.set_style(style)





heatmap = ["#0e2ff7","#232be3","#3827cf","#4d23bc",
            "#621fa8","#771b94","#8c1680","#961476",
            "#ab1062","#c00c4e","#d5083b","#ea0427",
            "#ff0013"]
#list of colours for heatmap gradient style colouring


#set colour of node based on CHG context DNA methylation value
def chgmeth(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")

    tokens = n.name
    tokens1 = tokens.replace("t2t_", "")
    tokens2 = (tokens1).split("_")
    accname = tokens2[0]

    # make lyratas black
    lyratas = ["MN47Hifi", "SiberianAly"]
    style2 = NodeStyle()
    style2["shape"] = "square"
    style2["size"] = 70000
    style2["fgcolor"] = "black"
    style2["vt_line_color"] = "black"
    style2["hz_line_color"] = "black"
    if accname in lyratas:
        n.set_style(style2)

    if n.is_leaf() and accname not in lyratas:
        new = (n.name).replace("t2t_", "")
        listinfo = (new).split("_")
        #CHG
        chg = float(listinfo[-2])
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000

        cenh3range = 0.4
        array = [0, cenh3range/12, 2*cenh3range/12, 3*cenh3range/12, 4*cenh3range/12,
                  5*cenh3range/12, 6*cenh3range/12, 7*cenh3range/12, 8*cenh3range/12,
                  9*cenh3range/12, 10*cenh3range/12, 11*cenh3range/12, cenh3range, 1] #list of values to be used for interval sizes
        #interval sizes based on distribution of methylation values

        x = range(len(array)-1)
        for i in x:
            if array[i] < chg < array[i + 1]: #colour based on value
                style["vt_line_color"] = heatmap[i]
                style["hz_line_color"] = heatmap[i]
                n.set_style(style)


#set colour of node based on CG context DNA methylation value
def cgmeth(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")

    tokens = n.name
    tokens1 = tokens.replace("t2t_", "")
    tokens2 = (tokens1).split("_")
    accname = tokens2[0]
    # make lyratas black
    lyratas = ["MN47Hifi", "SiberianAly"]
    style2 = NodeStyle()
    style2["shape"] = "square"
    style2["size"] = 70000
    style2["fgcolor"] = "black"
    style2["vt_line_color"] = "black"
    style2["hz_line_color"] = "black"
    if accname in lyratas:
        n.set_style(style2)

    if n.is_leaf() and accname not in lyratas:
        new = (n.name).replace("t2t_", "")
        listinfo = (new).split("_")
        # CG
        cg = float(listinfo[-3])
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000
        cenh3range = 0.10
        step = 0.75
        interval = cenh3range/12
        array = [0, interval+step, 2*interval+step, 3*interval+step, 4*interval+step,
                 5*interval+step, 6*interval+step, 7*interval+step, 8*interval+step,
                 9*interval+step, 10*interval+step, 11*interval+step, 12*interval+step, 1]
        x = range(len(array)-1)
        for i in x:
            if array[i] < cg < array[i + 1]:
                style["vt_line_color"] = heatmap[i]
                style["hz_line_color"] = heatmap[i]
                n.set_style(style)


#set colour of node based on CHH context DNA methylation value
def chhmeth(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")
    tokens = n.name
    tokens1 = tokens.replace("t2t_", "")
    tokens2 = (tokens1).split("_")
    accname = tokens2[0]
    # make lyratas black
    lyratas = ["MN47Hifi", "SiberianAly"]
    style2 = NodeStyle()
    style2["shape"] = "square"
    style2["size"] = 70000
    style2["fgcolor"] = "black"
    style2["vt_line_color"] = "black"
    style2["hz_line_color"] = "black"
    if accname in lyratas:
        n.set_style(style2)

    if n.is_leaf() and accname not in lyratas:
        new = (n.name).replace("t2t_", "")
        listinfo = (new).split("_")
        #CHH
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000

        if len(listinfo[-1]) > 2: #some errors in data file, found value of "0."
            chh = float(listinfo[-1])

        cenh3range = 0.04

        step = 0.04
        interval = cenh3range/12
        array = [0, interval+step, 2*interval+step, 3*interval+step, 4*interval+step,
                 5*interval+step, 6*interval+step, 7*interval+step, 8*interval+step,
                 9*interval+step, 10*interval+step, 11*interval+step, 12*interval+step, 1]

        x = range(len(array)-1)
        for i in x:
            if array[i] < chh < array[i + 1]:
                style["vt_line_color"] = heatmap[i]
                style["hz_line_color"] = heatmap[i]
                n.set_style(style)


#annotate nodes based on CENH3 ChIP values
def chipcen(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")

    tokens = n.name
    tokens1 = tokens.replace("t2t_", "")
    tokens2 = (tokens1).split("_")
    accname = tokens2[0]
    # make lyratas black
    lyratas = ["MN47Hifi", "SiberianAly"]
    style2 = NodeStyle()
    style2["shape"] = "square"
    style2["size"] = 70000
    style2["fgcolor"] = "black"
    style2["vt_line_color"] = "black"
    style2["hz_line_color"] = "black"
    if accname in lyratas:
        n.set_style(style2)

    if n.is_leaf() and accname not in lyratas:
        new = (n.name).replace("t2t_", "")
        listinfo = (new).split("_")
        chip = float(listinfo[-5])
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000
        cenh3range = 1
        step = -0.05
        interval = cenh3range/12
        array = [-2, interval+step, 2*interval+step, 3*interval+step, 4*interval+step,
                 5*interval+step, 6*interval+step, 7*interval+step, 8*interval+step,
                 9*interval+step, 10*interval+step, 11*interval+step, 12*interval+step, 100000]

        x = range(len(array)-1)
        for i in x:
            if array[i] < chip < array[i + 1]:
                style["vt_line_color"] = heatmap[i]
                style["hz_line_color"] = heatmap[i]
                n.set_style(style)



#annotate nodes based on HOR values
def horcount(n):
    if n.support >= 95 and not n.is_leaf():
        C = CircleFace(radius=250000, color="DimGray", style="sphere")
        C.opacity = 1
        faces.add_face_to_node(C, n, 0, position="float-behind")
    tokens = n.name
    tokens1 = tokens.replace("t2t_", "")
    tokens2 = (tokens1).split("_")
    accname = tokens2[0]
    # make lyratas black
    lyratas = ["MN47Hifi", "SiberianAly"]
    style2 = NodeStyle()
    style2["shape"] = "square"
    style2["size"] = 70000
    style2["fgcolor"] = "black"
    style2["vt_line_color"] = "black"
    style2["hz_line_color"] = "black"
    if accname in lyratas:
        n.set_style(style2)

    if n.is_leaf() and accname not in lyratas:
        new = (n.name).replace("t2t_", "")
        listinfo = (new).split("_")
        hor = float(listinfo[-7])
        style = NodeStyle()
        style["shape"] = "sphere"
        style["size"] = 70000
        cenh3range = 50
        step = 0
        interval = cenh3range/12
        array = [-1, interval+step, 2*interval+step, 3*interval+step, 4*interval+step,
                 5*interval+step, 6*interval+step, 7*interval+step, 8*interval+step,
                 9*interval+step, 10*interval+step, 11*interval+step, 12*interval+step, 10000]

        x = range(len(array)-1)
        for i in x:
            if array[i] < hor < array[i + 1]:
                style["vt_line_color"] = heatmap[i]
                style["hz_line_color"] = heatmap[i]
                n.set_style(style)

##for single tree visualisation
t = Tree("t2t_rootly.Fasta.contree") #load in tree file
ts = TreeStyle() #create treestyle
ts.layout_fn = chromosome #annotate nodes based on the 'chromosome' function
ts.show_leaf_name = False #don't show leaf name
ts.rotation = 180 #rotate tree
ts.mode = "c" #use circular view
ts.scale_length = 0.15
ts.show_scale = True #show scale bar


for n in t.traverse():
    if n.dist > 0.22:
        n.delete() #delete very long branches, over 0.22, to preserve look


t.render("t2t160_cap_bylen.png",w=1500,units="px", tree_style = ts) #create png
t.render("t2t_rootly.pdf",w=1500,units="px", tree_style = ts) #create pdf
t.show(tree_style = ts) #show tree in interactive viewer


##code below for looping through trees and making multiple, comment when not using!
t = Tree("t2t_rootly.Fasta.contree") #tree file to be looped through
cenh3 = [chromosome, chgmeth, chhmeth, cgmeth, chipcen, horcount] #different functions to loop through
names = ["chromosome","chg","chh","cg","chip","hor"] #names of functions to add into file name

for i in cenh3:
    ts = TreeStyle()
    ts.layout_fn = i
    ts.show_leaf_name = False
    ts.rotation = 180
    ts.mode = "c"
    #ts.optimal_scale_level = True
    ts.scale_length = 0.15
    ts.show_scale = True
    for n in t.traverse():
        if n.dist > 0.22:
            n.delete()

    t.render("t2t_rootly"+names[cenh3.index(i)]+".png",w=1500,units="px", tree_style = ts)
    print("done "+names[cenh3.index(i)]) #tells you it's done


##code for looping through multiple tree files and multiple functions, specifically for trees by geography, comment when not using!
trees = ["_groupa_all.Fasta.contree","_groupc_all.Fasta.contree","_groupb_all.Fasta.treefile"] #tree files to loop through
names = ["groupa","groupc","groupb"] #names of trees being visualised
functions = [chromosome,byaccession] #functions to visualise with
funnames = ["chromosome","accession"] #names of functions

for i in trees:
    t=Tree(i)
    for j in functions:
        ts = TreeStyle()
        ts.layout_fn = j
        ts.show_leaf_name = False
        ts.rotation = 180
        ts.mode = "c"
        #ts.optimal_scale_level = True
        ts.scale_length = 0.15
        ts.show_scale = True
        for n in t.traverse():
            if n.dist > 0.22:
                n.delete()

        t.render("_"+names[trees.index(i)]+"_"+funnames[functions.index(j)]+".png",w=1500,units="px", tree_style = ts)


## code for looping through multiple tree files and multiple functions, specifically for mega-trees, comment when not using!

mtrees = ["megatree_1a.Fasta.contree", "megatree_2a.Fasta.contree","megatree_3a.Fasta.contree",
          "megatree_4a.Fasta.contree","megatree_5a.Fasta.contree"]

mfunctions = [chromosome,bygroup,bylen]
mfunnames = ["chromosome","group","length"]
mnames = ["megatree1a","megatree2a","megatree3a","megatree4a","megatree5a"]

for i in mtrees:
    t=Tree(i)
    for j in mfunctions:
        ts = TreeStyle()
        ts.layout_fn = j
        ts.show_leaf_name = False
        ts.rotation = 180
        ts.mode = "c"
        #ts.optimal_scale_level = "full"
        ts.scale_length = 0.15
        ts.show_scale = True
        for n in t.traverse():
            if n.dist > 0.22:
                n.delete()

        t.render("_" + mnames[mtrees.index(i)] + mfunnames[mfunctions.index(j)] + ".png",w=1500,units="px", tree_style = ts)
