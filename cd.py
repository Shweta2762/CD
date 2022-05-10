


























#start

















#Lexical
keywords = {"auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while","printf","scanf","%d","include","stdio.h","main"}

operators = {"+","-","*","/","<",">","=","<=",">=","==","!=","++","--","%"}

delimiters = {'(',')','{','}','[',']','"',"'",';','#',',',''}

def detect_keywords(text):
	arr = []
	for word in text:
		if word in keywords:
			arr.append(word)
	return list(set(arr))

def detect_operators(text):
	arr = []
	for word in text:
		if word in operators:
			arr.append(word)
	return list(set(arr))

def detect_delimiters(text):
	arr = []
	for word in text:
		if word in delimiters:
			arr.append(word)
	return list(set(arr))

def detect_num(text):
	arr = []
	for word in text:
		try:
			a = int(word)
			arr.append(word)
		except:
			pass
	return list(set(arr))
"""
this is original function for detecting identifier
def is_identifier(token):
    if token[0] in numbers or token in keywords:
        return False
    else:
        return identifier(token)
def identifier(token):
    if len(token)<2 and (token[0] in alphabets or token[0] in numbers or token[0] == "_"):
        return True
    elif token[0] in alphabets or token[0] in numbers or token[0] == "_":
        return identifier(token[1:])
    else:
        return False
"""
def detect_identifiers(text):
	k = detect_keywords(text)
	o = detect_operators(text)
	d = detect_delimiters(text)
	n = detect_num(text)
	not_ident = k + o + d + n
	arr = []
	for word in text:
		if word not in not_ident:
			arr.append(word)
	return arr

with open('e1-example.txt') as t:
	text = t.read().split()

print("Keywords: ",detect_keywords(text))
print("Operators: ",detect_operators(text))
print("Delimiters: ",detect_delimiters(text))
print("Identifiers: ",detect_identifiers(text))
print("Numbers: ",detect_num(text))



























#Regular Expression to NFA
rows, cols = (20, 3) 
q = [[0]*cols]*rows 

reg = input('Enter your regular expression : ')
len = len(reg)
i = 0
j = 1
while(i<len):
    if reg[i] == 'a':
        try:
            if reg[i+1] != '|' and reg[i+1] !='*':
                q[j][0] = j+1
                j += 1
        except:
            q[j][0] = j+1

    elif reg[i] == 'b':
        try:
            if reg[i+1] != '|' and reg[i+1] !='*':
                q[j][1] = j+1
                j += 1
        except:
            q[j][1] = j+1
        
    elif reg[i]=='e' and reg[i+1]!='|'and reg[i+1]!='*':
        q[j][2]=j+1
        j+=1

    elif reg[i] == 'a' and reg[i+1] == '|' and reg[i+2] =='b':
        q[j][2]=((j+1)*10)+(j+3)
        j+=1
        q[j][0]=j+1
        j+=1
        q[j][2]=j+3
        j+=1
        q[j][1]=j+1
        j+=1
        q[j][2]=j+1
        j+=1
        i=i+2

    elif reg[i]=='b'and reg[i+1]=='|' and reg[i+2]=='a':

        q[j][2]=((j+1)*10)+(j+3)
        j+=1
        q[j][1]=j+1
        j+=1
        q[j][2]=j+3
        j+=1
        q[j][0]=j+1
        j+=1
        q[j][2]=j+1
        j+=1
        i=i+2

    elif reg[i]=='a' and reg[i+1]=='*':

        q[j][2]=((j+1)*10)+(j+3)
        j+=1
        q[j][0]=j+1
        j+=1
        q[j][2]=((j+1)*10)+(j-1)
        j+=1

    elif reg[i]=='b' and reg[i+1]=='*':
        q[j][2]=((j+1)*10)+(j+3)
        j+=1
        q[j][1]=j+1
        j+=1
        q[j][2]=((j+1)*10)+(j-1)
        j+=1

    elif reg[i]==')' and reg[i+1]=='*':

        q[0][2]=((j+1)*10)+1
        q[j][2]=((j+1)*10)+1
        j+=1

    i +=1

print("Transition Function ==>")

for i in range(0,j):
    if q[i][0]!=0:

	    print(f"\n {q[i]},a --> {q[i][0]}")

    elif q[i][1]!=0:
	    print (f"\n {q[i]},b-->{q[i][1]}")

    elif q[i][2]!=0:
		
	    if q[i][2]<10:
		    print(f"\n {q[i]},e-->{q[i][2]}")
	    else:
		    print(f"\n {q[i]},e-->{q[i][2]}/10 and {q[i][2]}%10")
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    


#Left Recursion
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
	char a[10],b[50][10]={""},d[50][10]={""},ch;
	int i,n,c[10]={0},j,k,t,n1;
	printf("\nEnter the NON TERMINALS: ");
	scanf("%s",a);
	n=strlen(a);
	for(i=0;i<n;i++)
	{
		printf("\nEnter the number of productions for %c : ",a[i]);
		scanf("%d",&c[i]);
	}
	t=0;
	for(i=0;i<n;i++)
	{
		printf("\nEnter the productions for %c",a[i]);
		k=t;
		for(j=0;j<c[i];j++)
		{
			printf("\n%c->",a[i]);
			do
			{
				scanf("%s",b[k]);
				k++;
			}while(k<j);
		}
		t=t+10;
	}
	t=0;
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
		{
			n1=strlen(b[t]);
			for(k=1;k<n1;k++)
			{
				d[t][k-1]=b[t][k];
			}
		}
		t=t+10;
	}
	t=0;
	printf("\n\nThe resulting productions after eliminating Left Recursion are : \n");
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
		{
			for(j=1;j<c[i];j++)
			{
				printf("\n%c -> %s%c'",a[i],b[t+j],a[i]);
			}
		}
		t=t+10;
	}
	t=0;
	for(i=0;i<n;i++)
	{
		if(a[i]==b[t][0])
			printf("\n%c' -> %s%c'|%c",a[i],d[t],a[i],(char)238);
		else
			for(j=0;j<c[i];j++)
				printf("\n%c -> %s",a[i],b[t+j]);
		t=t+10;
	}
}































#Left Factoring
from itertools import takewhile
def groupby(ls):
    d = {}
    ls = [ y[0] for y in rules ]
    initial = list(set(ls))
    for y in initial:
        for i in rules:
            if i.startswith(y):
                if y not in d:
                    d[y] = []
                d[y].append(i)
    return d

def prefix(x):
    return len(set(x)) == 1


starting=""
rules=[]
common=[]
alphabetset=["A'","B'","C'","D'","E'","F'","G'","H'","I'","J'","K'","L'","M'","N'","O'","P'","Q'","R'","S'","T'","U'","V'","W'","X'","Y'","Z'"]


# s= "S->iEtS|iEtSeS|a"
s="S->aAB|aBC|aAC"
while(True):
    rules=[]
    common=[]
    split=s.split("->")
    starting=split[0]
    for i in split[1].split("|"):
        rules.append(i)

#logic for taking commons out
    for k, l in groupby(rules).items():
        r = [l[0] for l in takewhile(prefix, zip(*l))]
        common.append(''.join(r))
#end of taking commons
    for i in common:
        newalphabet=alphabetset.pop()
        print(starting+"->"+i+newalphabet)
        index=[]
        for k in rules:
            if(k.startswith(i)):
                index.append(k)
        print(newalphabet+"->",end="")
        for j in index[:-1]:
            stringtoprint=j.replace(i,"", 1)+"|"
            if stringtoprint=="|":
                print("\u03B5","|",end="")
            else:
                print(j.replace(i,"", 1)+"|",end="")
        stringtoprint=index[-1].replace(i,"", 1)+"|"
        if stringtoprint=="|":
            print("\u03B5","",end="")
        else:
            print(index[-1].replace(i,"", 1)+"",end="")
        print("")
    break






























#first and follow
# #example for direct left recursion
# gram = {"A":["Aa","Ab","c","d"]
# }
#example for indirect left recursion
gram = {
	"E":["E+T","T"],
	"T":["T*F","F"],
	"F":["(E)","i"]
}

def removeDirectLR(gramA, A):
	"""gramA is dictonary"""
	temp = gramA[A]
	tempCr = []
	tempInCr = []
	for i in temp:
		if i[0] == A:
			#tempInCr.append(i[1:])
			tempInCr.append(i[1:]+[A+"'"])
		else:
			#tempCr.append(i)
			tempCr.append(i+[A+"'"])
	tempInCr.append(["e"])
	gramA[A] = tempCr
	gramA[A+"'"] = tempInCr
	return gramA


def checkForIndirect(gramA, a, ai):
	if ai not in gramA:
		return False 
	if a == ai:
		return True
	for i in gramA[ai]:
		if i[0] == ai:
			return False
		if i[0] in gramA:
			return checkForIndirect(gramA, a, i[0])
	return False

def rep(gramA, A):
	temp = gramA[A]
	newTemp = []
	for i in temp:
		if checkForIndirect(gramA, A, i[0]):
			t = []
			for k in gramA[i[0]]:
				t=[]
				t+=k
				t+=i[1:]
				newTemp.append(t)

		else:
			newTemp.append(i)
	gramA[A] = newTemp
	return gramA

def rem(gram):
	c = 1
	conv = {}
	gramA = {}
	revconv = {}
	for j in gram:
		conv[j] = "A"+str(c)
		gramA["A"+str(c)] = []
		c+=1

	for i in gram:
		for j in gram[i]:
			temp = []	
			for k in j:
				if k in conv:
					temp.append(conv[k])
				else:
					temp.append(k)
			gramA[conv[i]].append(temp)


	#print(gramA)
	for i in range(c-1,0,-1):
		ai = "A"+str(i)
		for j in range(0,i):
			aj = gramA[ai][0][0]
			if ai!=aj :
				if aj in gramA and checkForIndirect(gramA,ai,aj):
					gramA = rep(gramA, ai)

	for i in range(1,c):
		ai = "A"+str(i)
		for j in gramA[ai]:
			if ai==j[0]:
				gramA = removeDirectLR(gramA, ai)
				break

	op = {}
	for i in gramA:
		a = str(i)
		for j in conv:
			a = a.replace(conv[j],j)
		revconv[i] = a

	for i in gramA:
		l = []
		for j in gramA[i]:
			k = []
			for m in j:
				if m in revconv:
					k.append(m.replace(m,revconv[m]))
				else:
					k.append(m)
			l.append(k)
		op[revconv[i]] = l

	return op

result = rem(gram)


def first(gram, term):
	a = []
	if term not in gram:
		return [term]
	for i in gram[term]:
		if i[0] not in gram:
			a.append(i[0])
		elif i[0] in gram:
			a += first(gram, i[0])
	return a

firsts = {}
for i in result:
	firsts[i] = first(result,i)
	print(f'First({i}):',firsts[i])
# 	temp = follow(result,i,i)
# 	temp = list(set(temp))
# 	temp = [x if x != "e" else "$" for x in temp]
# 	print(f'Follow({i}):',temp)

def follow(gram, term):
	a = []
	for rule in gram:
		for i in gram[rule]:
			if term in i:
				temp = i
				indx = i.index(term)
				if indx+1!=len(i):
					if i[-1] in firsts:
						a+=firsts[i[-1]]
					else:
						a+=[i[-1]]
				else:
					a+=["e"]
				if rule != term and "e" in a:
					a+= follow(gram,rule)
	return a

follows = {}
for i in result:
	follows[i] = list(set(follow(result,i)))
	if "e" in follows[i]:
		follows[i].pop(follows[i].index("e"))
	follows[i]+=["$"]
	print(f'Follow({i}):',follows[i])



























#Predictive Parsing Table
# #example for direct left recursion
# gram = {"A":["Aa","Ab","c","d"]
# }
#example for indirect left recursion
gram = {
	"E":["E+T","T"],
	"T":["T*F","F"],
	"F":["(E)","i"]
}

def removeDirectLR(gramA, A):
	"""gramA is dictonary"""
	temp = gramA[A]
	tempCr = []
	tempInCr = []
	for i in temp:
		if i[0] == A:
			#tempInCr.append(i[1:])
			tempInCr.append(i[1:]+[A+"'"])
		else:
			#tempCr.append(i)
			tempCr.append(i+[A+"'"])
	tempInCr.append(["e"])
	gramA[A] = tempCr
	gramA[A+"'"] = tempInCr
	return gramA


def checkForIndirect(gramA, a, ai):
	if ai not in gramA:
		return False 
	if a == ai:
		return True
	for i in gramA[ai]:
		if i[0] == ai:
			return False
		if i[0] in gramA:
			return checkForIndirect(gramA, a, i[0])
	return False

def rep(gramA, A):
	temp = gramA[A]
	newTemp = []
	for i in temp:
		if checkForIndirect(gramA, A, i[0]):
			t = []
			for k in gramA[i[0]]:
				t=[]
				t+=k
				t+=i[1:]
				newTemp.append(t)

		else:
			newTemp.append(i)
	gramA[A] = newTemp
	return gramA

def rem(gram):
	c = 1
	conv = {}
	gramA = {}
	revconv = {}
	for j in gram:
		conv[j] = "A"+str(c)
		gramA["A"+str(c)] = []
		c+=1

	for i in gram:
		for j in gram[i]:
			temp = []	
			for k in j:
				if k in conv:
					temp.append(conv[k])
				else:
					temp.append(k)
			gramA[conv[i]].append(temp)


	#print(gramA)
	for i in range(c-1,0,-1):
		ai = "A"+str(i)
		for j in range(0,i):
			aj = gramA[ai][0][0]
			if ai!=aj :
				if aj in gramA and checkForIndirect(gramA,ai,aj):
					gramA = rep(gramA, ai)

	for i in range(1,c):
		ai = "A"+str(i)
		for j in gramA[ai]:
			if ai==j[0]:
				gramA = removeDirectLR(gramA, ai)
				break

	op = {}
	for i in gramA:
		a = str(i)
		for j in conv:
			a = a.replace(conv[j],j)
		revconv[i] = a

	for i in gramA:
		l = []
		for j in gramA[i]:
			k = []
			for m in j:
				if m in revconv:
					k.append(m.replace(m,revconv[m]))
				else:
					k.append(m)
			l.append(k)
		op[revconv[i]] = l

	return op

result = rem(gram)
terminals = []
for i in result:
	for j in result[i]:
		for k in j:
			if k not in result:
				terminals+=[k]
terminals = list(set(terminals))
#print(terminals)

def first(gram, term):
	a = []
	if term not in gram:
		return [term]
	for i in gram[term]:
		if i[0] not in gram:
			a.append(i[0])
		elif i[0] in gram:
			a += first(gram, i[0])
	return a

firsts = {}
for i in result:
	firsts[i] = first(result,i)
#	print(f'First({i}):',firsts[i])

def follow(gram, term):
	a = []
	for rule in gram:
		for i in gram[rule]:
			if term in i:
				temp = i
				indx = i.index(term)
				if indx+1!=len(i):
					if i[-1] in firsts:
						a+=firsts[i[-1]]
					else:
						a+=[i[-1]]
				else:
					a+=["e"]
				if rule != term and "e" in a:
					a+= follow(gram,rule)
	return a

follows = {}
for i in result:
	follows[i] = list(set(follow(result,i)))
	if "e" in follows[i]:
		follows[i].pop(follows[i].index("e"))
	follows[i]+=["$"]
#	print(f'Follow({i}):',follows[i])

resMod = {}
for i in result:
	l = []
	for j in result[i]:
		temp = ""
		for k in j:
			temp+=k
		l.append(temp)
	resMod[i] = l

# create predictive parsing table
tterm = list(terminals)
tterm.pop(tterm.index("e"))
tterm+=["$"]
pptable = {}
for i in result:
	for j in tterm:
		if j in firsts[i]:
			pptable[(i,j)]=resMod[i[0]][0]
		else:
			pptable[(i,j)]=""
	if "e" in firsts[i]:
		for j in tterm:
			if j in follows[i]:
				pptable[(i,j)]="e" 	
pptable[("F","i")] = "i"
toprint = f'{"": <10}'
for i in tterm:
	toprint+= f'|{i: <10}'
print(toprint)
for i in result:
	toprint = f'{i: <10}'
	for j in tterm:
		if pptable[(i,j)]!="":
			toprint+=f'|{i+"->"+pptable[(i,j)]: <10}'
		else:
			toprint+=f'|{pptable[(i,j)]: <10}'
	print(f'{"-":-<76}')
	print(toprint)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#Shift Reduce parsing
# example 1
# gram = {
# 	"E":["2E2","3E3","4"]
# }
# starting_terminal = "E"
# inp = "2324232$"

# example 2
gram = {
	"S":["S+S","S*S","i"]
}
starting_terminal = "S"
inp = "i+i*i"

stack = "$"
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
		action = False

	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
		break






























a = ["E=E+T",
     "E=T",
     "T=T*F",
     "T=F",
     "F=(E)",
     "F=i"]

rules = {}
terms = []
for i in a:
    temp = i.split("=")
    terms.append(temp[0])
    try:
        rules[temp[0]] += [temp[1]]
    except:
        rules[temp[0]] = [temp[1]]

terms = list(set(terms))
print(rules,terms)

def leading(gram, rules, term, start):
    s = []
    if gram[0] not in terms:
        return gram[0]
    elif len(gram) == 1:
        return [0]
    elif gram[1] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= leading(i, rules, gram[-1], start)
            s+= [gram[1]]
        return s

leads = {}
for i in terms:
    s = [0]
    for j in rules[i]:
        s+=leading(j,rules,i,i)
    s = set(s)
    s.remove(0)
    leads[i] = s

for i in terms:
    print("LEADING("+i+"):",leads[i])
    






























a = ["E=E+T",
     "E=T",
     "T=T*F",
     "T=F",
     "F=(E)",
     "F=i"]

rules = {}
terms = []
for i in a:
    temp = i.split("=")
    terms.append(temp[0])
    try:
        rules[temp[0]] += [temp[1]]
    except:
        rules[temp[0]] = [temp[1]]

terms = list(set(terms))
print(rules,terms)
    
def trailing(gram, rules, term, start):
    s = []
    if gram[-1] not in terms:
        return gram[-1]
    elif len(gram) == 1:
        return [0]
    elif gram[-2] not in terms and gram[-1] is not start:

        for i in rules[gram[-1]]:
            s+= trailing(i, rules, gram[-1], start)
            s+= [gram[-2]]
        return s

trails = {}
for i in terms:
    s = [0]
    for j in rules[i]:
        s+=trailing(j,rules,i,i)
    s = set(s)
    s.remove(0)
    trails[i] = s

for i in terms:
    print("TRAILING("+i+"):",trails[i])



































#LR(0)
gram = {
	"S":["CC"],
	"C":["aC","d"]
}
start = "S"
terms = ["a","d","$"]

non_terms = []
for i in gram:
	non_terms.append(i)
gram["S'"]= [start]


new_row = {}
for i in terms+non_terms:
	new_row[i]=""


non_terms += ["S'"]
# each row in state table will be dictionary {nonterms ,term,$}
stateTable = []
# I = [(terminal, closure)]
# I = [("S","A.A")]

def Closure(term, I):
	if term in non_terms:
		for i in gram[term]:
			I+=[(term,"."+i)]
	I = list(set(I))
	for i in I:
		# print("." != i[1][-1],i[1][i[1].index(".")+1])
		if "." != i[1][-1] and i[1][i[1].index(".")+1] in non_terms and i[1][i[1].index(".")+1] != term:
			I += Closure(i[1][i[1].index(".")+1], [])
	return I

Is = []
Is+=set(Closure("S'", []))


countI = 0
omegaList = [set(Is)]
while countI<len(omegaList):
	newrow = dict(new_row)
	vars_in_I = []
	Is = omegaList[countI]
	countI+=1
	for i in Is:
		if i[1][-1]!=".":
			indx = i[1].index(".")
			vars_in_I+=[i[1][indx+1]]
	vars_in_I = list(set(vars_in_I))
	# print(vars_in_I)
	for i in vars_in_I:
		In = []
		for j in Is:
			if "."+i in j[1]:
				rep = j[1].replace("."+i,i+".")
				In+=[(j[0],rep)]
		if (In[0][1][-1]!="."):
			temp = set(Closure(i,In))
			if temp not in omegaList:
				omegaList.append(temp)
			if i in non_terms:
				newrow[i] = str(omegaList.index(temp))
			else:
				newrow[i] = "s"+str(omegaList.index(temp))
			print(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')
		else:
			temp = set(In)
			if temp not in omegaList:
				omegaList.append(temp)
			if i in non_terms:
				newrow[i] = str(omegaList.index(temp))
			else:
				newrow[i] = "s"+str(omegaList.index(temp))
			print(f'Goto(I{countI-1},{i}):{temp} That is I{omegaList.index(temp)}')

	stateTable.append(newrow)
print("\n\nList of I's\n")
for i in omegaList:
	print(f'I{omegaList.index(i)}: {i}')


#populate replace elements in state Table
I0 = []
for i in list(omegaList[0]):
	I0 += [i[1].replace(".","")]
print(I0)

for i in omegaList:
	for j in i:
		if "." in j[1][-1]:
			if j[1][-2]=="S":
				stateTable[omegaList.index(i)]["$"] = "Accept"
				break
			for k in terms:
				stateTable[omegaList.index(i)][k] = "r"+str(I0.index(j[1].replace(".","")))
print("\nStateTable")

print(f'{" ": <9}',end="")
for i in new_row:
	print(f'|{i: <11}',end="")

print(f'\n{"-":-<66}')
for i in stateTable:
	print(f'{"I("+str(stateTable.index(i))+")": <9}',end="")
	for j in i:
		print(f'|{i[j]: <10}',end=" ")
	print()































OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
    	output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

expres = input("INPUT THE EXPRESSION: ")
pos = infix_to_postfix(expres)





























OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if ch not in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)


























































#NFA to DFA
import pandas as pd

nfa = {}
n = int(input("No. of states : "))
t = int(input("No. of transitions : "))
for i in range(n):
    state = input("state name : ")
    nfa[state] = {}
    for j in range(t):
        path = input("path : ")
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reaching_state = [x for x in input().split()]
        nfa[state][path] = reaching_state

print("\nNFA :- \n")
print(nfa)
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]

new_states_list = []

#-------------------------------------------------

dfa = {}
keys_list = list(
    list(nfa.keys())[0])
path_list = list(nfa[keys_list[0]].keys())

dfa[keys_list[0]] = {}
for y in range(t):
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])
    dfa[keys_list[0]][path_list[y]] = var
    if var not in keys_list:
        new_states_list.append(var)
        keys_list.append(var)

while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]
            s = ""
            s = s.join(temp)
            if s not in keys_list:
                new_states_list.append(s)
                keys_list.append(s)
            dfa[new_states_list[0]][path_list[i]] = s

    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa)
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)






























#Three address quadruple
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
    	output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]

### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
	print("### THREE ADDRESS CODE GENERATION ###")
	exp_stack = []
	t = 1
	
	for i in pos:
		if i not in OPERATORS:
			exp_stack.append(i)
		else:
			print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
			exp_stack=exp_stack[:-2]
			exp_stack.append(f't{t}')
			t+=1

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)












































