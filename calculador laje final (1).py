from tkinter import *
import math
janela_principal= Tk()

 #listas com valores e entradas, todas as listas possuem a mesma quantidade de itens
quantidade=[]
tamanho=[]
metro_linear=[]
reforco_cinco=[]
reforco_seis=[]
reforco_oito=[]
reforco_dez=[]
reforco_doze=[]
reforco_dezesseis=[]

#função apenas pra mostras as vigas no listbox do tkinter
def vigas_visual():
    #calculo da quantidade de vigas, checkbox para retirar 1 viga da conta caso seja preciso
    quantidade_vg=float(vigas_entry.get())
    
    if (varvg.get() == 1):
        q_vg=math.floor(quantidade_vg / 0.43)
        quantidade.append(q_vg)#salva esse valor na lista 
    else:
        q_vg=int(quantidade_vg / 0.43)+1
        quantidade.append(q_vg)#salva esse valor na lista 

    tamanho_vg=float(tamanho_entry.get())
    tamanho.append(tamanho_vg)#salva esse valor na lista 
    #calculo do metro linear de acordo com a quantidade de viga resultante da conta vezes o tamanho das vigas informado no entry
    ml=float(q_vg*tamanho_vg)
    metro_linear.append(ml)#salva esse valor na lista 

    #obtenção dos valores dos reforços adicionados nos entrys
    reforco_cinco_vg=int(cinco_mm_entry.get())
    reforco_seis_vg=int(seis_mm_entry.get())
    reforco_oito_vg=int(oito_mm_entry.get())
    reforco_dez_vg=int(dez_mm_entry.get())
    reforco_doze_vg=int(doze_mm_entry.get())
    reforco_dezesseis_vg=int(dezesseis_mm_entry.get())

    #soma de todos os reforços, se a soma for 0 nao precis adicionar nenhum reforço no listbox
    zero=reforco_cinco_vg+reforco_seis_vg+reforco_oito_vg+reforco_dez_vg+reforco_doze_vg+reforco_dezesseis_vg

    if zero==0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} m ')
        varvg.set(0)

    #se entry do reforço de 5mm for diferente de 0 executa esse if
    if reforco_cinco_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} m  {reforco_cinco_vg:.0f}br 5mm')#adiciona um item a listbox
        ml_cinco=(q_vg*tamanho_vg)*reforco_cinco_vg #faz a conta do metro linear do reforço(quantidade de barras adicionadas na entry vezes metro linear viga(quantidade X tamanho)
        reforco_cinco.append(ml_cinco) #adiciona esse metro linear de reforço na lista do reforço
        cinco_mm_entry.delete(0,END) #reseta entry para 0
        cinco_mm_entry.insert(0,'0') #reseta entry para 0
        varvg.set(0) #desmarca o checkbox
    else :
        reforco_cinco.append(0)
        
    
    if reforco_seis_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} m  {reforco_seis_vg:.0f}br 6mm')
        ml_seis=(q_vg*tamanho_vg)*reforco_seis_vg
        reforco_seis.append(ml_seis)
        seis_mm_entry.delete(0,END)
        seis_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_seis.append(0)

    
    if reforco_oito_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_oito_vg:.0f}br 8mm')
        ml_oito=(q_vg*tamanho_vg)*reforco_oito_vg
        reforco_oito.append(ml_oito)
        oito_mm_entry.delete(0,END)
        oito_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_oito.append(0)
    
    
    if reforco_dez_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_dez_vg:.0f}br 10mm')
        ml_dez=(q_vg*tamanho_vg)*reforco_dez_vg
        reforco_dez.append(ml_dez)
        dez_mm_entry.delete(0,END)
        dez_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_dez.append(0)
    
    
    if reforco_doze_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_doze_vg:.0f}br 12,5mm')
        ml_doze=(q_vg*tamanho_vg)*reforco_doze_vg
        reforco_doze.append(ml_doze)
        doze_mm_entry.delete(0,END)
        doze_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_doze.append(0)

    
    if reforco_dezesseis_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_dezesseis_vg:.0f}br 16mm')
        ml_dezesseis=(q_vg*tamanho_vg)*reforco_dezesseis_vg
        reforco_dezesseis.append(ml_dezesseis)
        dezesseis_mm_entry.delete(0,END)
        dezesseis_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_dezesseis.append(0)


def calcular():
    ml_total=sum(metro_linear)
    area=ml_total * 0.43
    malha=int(area/5)
    tavela=int(area*12)
    r_cinco=sum(reforco_cinco)
    r_seis=sum(reforco_seis)
    r_oito=sum(reforco_oito)
    r_dez=sum(reforco_dez)
    r_doze=sum(reforco_doze)
    r_dezesseis=sum(reforco_dezesseis)
    
    resultados.config(text=f'Metro quadrado total = {area:.2f}\nMetro linear total= {ml_total:.2f}\nQuantidade de EPS= {ml_total:.1f}\nQuantidade de TAVELA= {tavela}\nQuantidade de malhas: {malha:.0f}\n\nReforços:\n5mm={r_cinco:.2f}\n6mm(1/4)= {r_seis:.2f}\n8mm(5/16)= {r_oito:.2f}\n10mm(3/8)= {r_dez:.2f}\n12,5mm(1/2)= {r_doze:.2f} \
                    \n16mm= {r_dezesseis:.2f}')


def apagar_ultimo():
    apagar=lista_vigas.curselection()
    lista_vigas.delete(apagar[0])
    quantidade.pop(apagar[0])
    tamanho.pop(apagar[0])
    metro_linear.pop(apagar[0])
    reforco_cinco.pop(apagar[0])
    reforco_seis.pop(apagar[0])
    reforco_oito.pop(apagar[0])
    reforco_dez.pop(apagar[0])
    reforco_doze.pop(apagar[0])
    reforco_dezesseis.pop(apagar[0])


def salvar():
    ml_total=sum(metro_linear)
    area=ml_total * 0.43
    malha=int(area/5)
    tavela=int(area*12)
    r_cinco=sum(reforco_cinco)
    r_seis=sum(reforco_seis)
    r_oito=sum(reforco_oito)
    r_dez=sum(reforco_dez)
    r_doze=sum(reforco_doze)
    r_dezesseis=sum(reforco_dezesseis)
    
    resultados.config(text=f'Metro quadrado total = {area:.2f}\nMetro linear total= {ml_total:.2f}\nQuantidade de EPS= {ml_total:.1f}\nQuantidade de TAVELA= {tavela}\nQuantidade de malhas: {malha:.0f}\n\nReforços:\n5mm={r_cinco:.2f}\n6mm(1/4)= {r_seis:.2f}\n8mm(5/16)= {r_oito:.2f}\n10mm(3/8)= {r_dez:.2f}\n12,5mm(1/2)= {r_doze:.2f} \
                    \n16mm= {r_dezesseis:.2f}')
    
    with open(f'{nome_entry.get()}.txt','x') as salvar:
        salvar.write(f'Cliente: {nome_entry.get()}\nCPF: {cpf_entry.get()}\nContato: {telefone_entry}\nEndereço: {endereco_entry}\nMetro quadrado total = {area:.2f}\nMetro linear total= {ml_total:.2f}\nQuantidade de EPS= {ml_total:.1f}\nQuantidade de TAVELA= {tavela}\nQuantidade de malhas: {malha:.0f}\n\nReforços:\n5mm={r_cinco:.2f}\n6mm(1/4)= {r_seis:.2f}\n8mm(5/16)= {r_oito:.2f}\n10mm(3/8)= {r_dez:.2f}\n12,5mm(1/2)= {r_doze:.2f} \
                        \n16mm= {r_dezesseis:.2f}\n\nLISTA DE VIGAS:\n\n')
        lv=lista_vigas.get(0,END)
        lv_lista=list(lv)
        
        o=list(set(tamanho))
        o.sort(reverse=True)
        ordem=[]
        for i in o:
            for j in range(0,len(tamanho)):
                if (tamanho[j] == i):
                    ordem.append(lv_lista[j])

        print(ordem)           
    
        for l in ordem:
            
            salvar.write(f'{l}\n')

        

        
        
        
    
    

            
        
#----------------------------------

janela_principal.title('Calculadora de Lajes')
janela_principal.configure(background='#000080')
janela_principal.geometry('1200x800')
janela_principal.resizable(True,True)
janela_principal.maxsize(width=1920, height=1080)
janela_principal.minsize(width=500,height=500)

frame_titulo = Frame(janela_principal, bg='yellow', highlightbackground='white',highlightthickness=3)  
frame_titulo.place(relx=0.02,rely=0.022, relwidth=0.97, relheight=0.045)
frame_titulo.configure(background='yellow')
        
frame_cliente= Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
frame_cliente.place(relx=0.02,rely=0.1, relwidth=0.97, relheight=0.1)
frame_cliente.configure(background='white')

frame_vigas = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
frame_vigas.place(relx=0.02,rely=0.22, relwidth=0.3, relheight=0.6)
frame_vigas.configure(background='white')

frame_lista = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
frame_lista.place(relx=0.33,rely=0.22, relwidth=0.4, relheight=0.6)
frame_lista.configure(background='white')

frame_resultado = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
frame_resultado.place(relx=0.74,rely=0.22, relwidth=0.25, relheight=0.6)
frame_resultado.configure(background='white')
        
frame_botao= Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
frame_botao.place(relx=0.33,rely=0.83, relwidth=0.66, relheight=0.1)
frame_botao.configure(background='white')

bt_apaga_u=Button(frame_botao, text='Apagar', fg='black',relief=RAISED,command=apagar_ultimo)
bt_apaga_u.place(relx=0.015,rely=0.2,relwidth=0.1, relheight=0.6)


bt_calc=Button(frame_botao, text='Calcular',fg='black', relief=RAISED,command=calcular)
bt_calc.place(relx=0.43,rely=0.2,relwidth=0.25, relheight=0.6)

bt_save=Button(frame_botao, text='Salvar (Criar arquivo .txt)', fg='black',relief=RAISED,command=salvar)
bt_save.place(relx=0.72,rely=0.2,relwidth=0.25, relheight=0.6)
        
bt_adicionar=Button(frame_vigas, text='Adicionar viga',fg='black', relief=RAISED,command=vigas_visual)
bt_adicionar.place(relx=0.3,rely=0.89,relwidth=0.4, relheight=0.1)
 
titulo=Label(frame_titulo, text='CALCULADORA DE MATERIAS PARA LAJE PREMOLDADA',fg='black',font=('Helvetica',18))
titulo.pack(side=TOP)
titulo.configure(background='yellow')

        #  MEDIDAS E QUANTIDADES DE VIGAS MAIS REFORÇOS
vigas=Label(frame_vigas, text="Largura do comodo em METROS\n (calcula a quantidade de vigas)",fg='black')
vigas.place(relx=0.03,rely=0.010)
vigas.configure(background='white')

varvg=IntVar()
menos_viga_cb=Checkbutton(frame_vigas, text='menos 1 viga',variable=varvg,onvalue=1,offvalue=0)
menos_viga_cb.place(relx=0.06, rely=.1)

vigas_entry=Entry(frame_vigas,fg='black')
vigas_entry.place(relx=0.6,rely=0.06,relwidth=0.3,relheight=0.05)
vigas_entry.configure(background='lightgray')

dash=Label(frame_vigas, text="----------------------------------------------------------------",fg='black')
dash.place(relx=0.03,rely=0.15)
dash.configure(background='white')

tamanho_label=Label(frame_vigas, text='Tamanho das vigas em METROS',fg='black')
tamanho_label.place(relx=0.03, rely=0.2)
tamanho_label.configure(background='white')
        
tamanho_entry=Entry(frame_vigas, fg='black')
tamanho_entry.place(relx=0.6,rely=0.2,relwidth=0.3,relheight=0.05)
tamanho_entry.configure(background='lightgray')

dash2=Label(frame_vigas, text="----------------------------------------------------------------",fg='black')
dash2.place(relx=0.03,rely=0.25)
dash2.configure(background='white')

lista_reforco=Label(frame_vigas, text='Selecione a quantidade de barras de reforço adicional:',fg='black')
lista_reforco.place(relx=0.03,rely=0.3)
lista_reforco.configure(background='white')

cinco_mm=Label(frame_vigas, text='5mm ------------->',bg='white',fg='black')
cinco_mm.place(relx=0.1,rely=0.37)

cinco_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
cinco_mm_entry.place(relx=0.4,rely=0.37,relwidth=0.3,relheight=0.05)
cinco_mm_entry.insert(0,'0')

seis_mm=Label(frame_vigas, text='1/4 -- 6mm ------>',bg='white',fg='black')
seis_mm.place(relx=0.1, rely=0.44)

seis_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
seis_mm_entry.place(relx=0.4,rely=0.44,relwidth=0.3,relheight=0.05)
seis_mm_entry.insert(0,'0')

oito_mm=Label(frame_vigas, text='5/16 -- 8mm ----->',bg='white',fg='black')
oito_mm.place(relx=0.1,rely=0.51)

oito_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
oito_mm_entry.place(relx=0.4, rely=0.51, relwidth=0.3,relheight=0.05)
oito_mm_entry.insert(0,'0')

dez_mm=Label(frame_vigas, text='3/8 -- 10mm ----->',bg='white',fg='black')
dez_mm.place(relx=0.1,rely=0.58)

dez_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
dez_mm_entry.place(relx=0.4, rely=0.58, relwidth=0.3,relheight=0.05)
dez_mm_entry.insert(0,'0')

doze_mm=Label(frame_vigas, text='1/2 -- 12,5mm --->',bg='white',fg='black')
doze_mm.place(relx=0.1,rely=0.65)

doze_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
doze_mm_entry.place(relx=0.4, rely=0.65, relwidth=0.3,relheight=0.05)
doze_mm_entry.insert(0,'0')

dezesseis_mm=Label(frame_vigas, text='5/8 -- 16mm ----->',bg='white',fg='black')
dezesseis_mm.place(relx=0.1,rely=0.72)


dezesseis_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
dezesseis_mm_entry.place(relx=0.4, rely=0.72, relwidth=0.3,relheight=0.05)
dezesseis_mm_entry.insert(0,'0')
# DADOS DO CLIENTE
nome=Label(frame_cliente, text='Nome:', bg='white',fg='black')
nome.place(relx=0.12,rely=0.1)

nome_entry=Entry(frame_cliente, bg='lightgray')
nome_entry.place(relx=0.16,rely=0.11,relwidth=0.2)

cpf=Label(frame_cliente, text='CPF:', bg='white',fg='black')
cpf.place(relx=0.37,rely=0.1)

cpf_entry=Entry(frame_cliente, bg='lightgray')
cpf_entry.place(relx=0.4,rely=0.11,relwidth=0.2)

telefone=Label(frame_cliente, text='Contato:', bg='white',fg='black')
telefone.place(relx=0.6,rely=0.1)

telefone_entry=Entry(frame_cliente, bg='lightgray')
telefone_entry.place(relx=0.65,rely=0.11,relwidth=0.2)

endereco=Label(frame_cliente, text='Endereço:', bg='white',fg='black')
endereco.place(relx=0.05,rely=0.6)

endereco_entry=Entry(frame_cliente, bg='lightgray')
endereco_entry.place(relx=0.1,rely=0.6,relwidth=0.8)

#quadro de lista de viga
lista_vigas=Listbox(frame_lista, bg='lightgray',fg='black')
lista_vigas.place(relx=0.01,rely=0.08, relwidth=0.98, relheight=0.9)
lista_viga_titulo=Label(frame_lista, text='Lista de vigas',fg='black')
lista_viga_titulo.place(relx=0.4, rely=0.01)
barra_scroll=Scrollbar(lista_vigas)
barra_scroll.pack(side=RIGHT, fill=Y)

#espaço dos resultados

resultados_label=Label(frame_resultado, text='Resultados',fg='black')
resultados_label.place(relx=0.4,rely=0.01)

resultados=Label(frame_resultado, text='',fg='black',justify=LEFT,font=('arial black', 12))
resultados.place(relx=0.01,rely=0.08,relwidth=0.98,relheight=0.9)




janela_principal.mainloop()
