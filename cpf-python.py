x1='000.000.000-00';x2='111.111.111-11';x3='222.222.222-22';x4='333.333.333-33';x5='444.444.44-44';x6='555.555.555-55'
x7='666.666.666-66';x8='777.777.777-77';x9='888.888.888-88';x10='999.999.999-99'
y1='.';y2='-'
print("Digite no formato:xxx.xxx.xxx-xx")
cpf=input("Informe seu CPF:")
tamanho=len(cpf)
if tamanho!=14:
    print("Digite um CPF válido!")
elif cpf[3:4]!=y1 or cpf[7:8]!=y1 or cpf[11:12]!=y2:
    print("Digite no formato correto!")
elif cpf[:]==x1 or cpf[:]==x2 or cpf[:]==x3 or cpf[:]==x4 or cpf[:]==x5 or cpf[:]==x6 or cpf[:]==x7 or cpf[:]==x8 or cpf[:]==x9 or cpf[:]==x10:
    print("Digite um CPF válido!")
else:
    a=cpf[:1] 
    b = float(a)

    c=cpf[1:2] 
    d = float(c)
    
    e=cpf[2:3]
    f = float(e)
    
    g=cpf[4:5]
    h = float(g)
    
    i=cpf[5:6]
    j = float(i)
    
    k=cpf[6:7]
    l = float(k)
    
    m=cpf[8:9]
    n = float(m)
    
    o=cpf[9:10]
    p = float(o)
    
    q=cpf[10:11]
    r = float(q)
    
    mult=b*10+d*9+f*8+h*7+j*6+l*5+n*4+p*3+r*2
    n1=mult*10
    n2=11
    resto=n1%n2
    
    s=cpf[12:13]#1 digito verificador
    t=float(s)
    
    if t!=resto:
        print("Digite um CPF válido!")
    else:
        mult2=b*11+d*10+f*9+h*8+j*7+l*6+n*5+p*4+r*3+resto*2
        n3=mult2*10
        resto2=n3%n2
        
        u=cpf[13:14]#2 digito verificador
        v=float(u)
        
        if v!=resto2:
            print("Digite um CPF válido!")
        else:
            print("Seu CPF é válido!")
    
    
