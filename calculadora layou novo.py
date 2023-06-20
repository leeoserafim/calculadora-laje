from tkinter import *
from math import *
from pandas import *
from  xlsxwriter import *
import easygui
import openpyxl
from pathlib import Path
import os
from numpy import *

from pathlib import Path




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
reload=[]

#função apenas pra mostras as vigas no listbox do tkinter
def vigas_visual():
    #calculo da quantidade de vigas, checkbox para retirar 1 viga da conta caso seja preciso
    quantidade_float=vigas_entry.get()
    quantidade_vg=quantidade_float.replace(',','.')
    quantidade_vg=float(quantidade_vg)
    if (varvg.get() == 1):
        q_vg=floor(quantidade_vg / 0.43)
        quantidade.append(q_vg)#salva esse valor na lista 
    else:
        q_vg=int(quantidade_vg / 0.43)+1
        quantidade.append(q_vg)#salva esse valor na lista 

    tamanho_float=tamanho_entry.get()
    tamanho_vg=tamanho_float.replace(',','.')
    tamanho_vg=float(tamanho_vg)
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
        reload.append(f'{q_vg} VG = {tamanho_vg} m ')
        varvg.set(0)

    #se entry do reforço de 5mm for diferente de 0 executa esse if
    if reforco_cinco_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} m  {reforco_cinco_vg:.0f}br 5mm')#adiciona um item a listbox
        reload.append(f'{q_vg} VG = {tamanho_vg} m  {reforco_cinco_vg:.0f}br 5mm')
        ml_cinco=(q_vg*tamanho_vg)*reforco_cinco_vg #faz a conta do metro linear do reforço(quantidade de barras adicionadas na entry vezes metro linear viga(quantidade X tamanho)
        reforco_cinco.append(ml_cinco) #adiciona esse metro linear de reforço na lista do reforço
        cinco_mm_entry.delete(0,END) #reseta entry para 0
        cinco_mm_entry.insert(0,'0') #reseta entry para 0
        varvg.set(0) #desmarca o checkbox
    else :
        reforco_cinco.append(0)
        
    
    if reforco_seis_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} m  {reforco_seis_vg:.0f}br 6mm')
        reload.append(f'{q_vg} VG = {tamanho_vg} m  {reforco_seis_vg:.0f}br 6mm')
        ml_seis=(q_vg*tamanho_vg)*reforco_seis_vg
        reforco_seis.append(ml_seis)
        seis_mm_entry.delete(0,END)
        seis_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_seis.append(0)

    
    if reforco_oito_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_oito_vg:.0f}br 8mm')
        reload.append(f'{q_vg} VG = {tamanho_vg} metros {reforco_oito_vg:.0f}br 8mm')
        ml_oito=(q_vg*tamanho_vg)*reforco_oito_vg
        reforco_oito.append(ml_oito)
        oito_mm_entry.delete(0,END)
        oito_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_oito.append(0)
    
    
    if reforco_dez_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_dez_vg:.0f}br 10mm')
        reload.append(f'{q_vg} VG = {tamanho_vg} metros {reforco_dez_vg:.0f}br 10mm')
        ml_dez=(q_vg*tamanho_vg)*reforco_dez_vg
        reforco_dez.append(ml_dez)
        dez_mm_entry.delete(0,END)
        dez_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_dez.append(0)
    
    
    if reforco_doze_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_doze_vg:.0f}br 12,5mm')
        reload.append(f'{q_vg} VG = {tamanho_vg} metros {reforco_doze_vg:.0f}br 12,5mm')
        ml_doze=(q_vg*tamanho_vg)*reforco_doze_vg
        reforco_doze.append(ml_doze)
        doze_mm_entry.delete(0,END)
        doze_mm_entry.insert(0,'0')
        varvg.set(0)
    else :
        reforco_doze.append(0)

    
    if reforco_dezesseis_vg != 0:
        lista_vigas.insert('end',f'{q_vg} VG = {tamanho_vg} metros {reforco_dezesseis_vg:.0f}br 16mm')
        reload.append(f'{q_vg} VG = {tamanho_vg} metros {reforco_dezesseis_vg:.0f}br 16mm')
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
    reload.pop(apagar[0])


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
    
    with open(f'{nome_entry.get()}.txt','w') as salvar:
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

    lista={'quantidade':quantidade,
                'tamanho':tamanho,
                'metro': metro_linear,
                '5mm' : reforco_cinco,
                '6mm': reforco_seis,
                '8mm': reforco_oito,
                '10mm':reforco_dez,
                '12,5mm' : reforco_doze,
                '16mm': reforco_dezesseis,
                'reload': reload
            }
    
    pd_lista=DataFrame.from_dict(lista,orient='index')
    pd_lista.fillna(0,inplace=True)
    pd_lista=pd_lista.transpose()
    
    pd_lista.to_excel(f'{nome_entry.get()}.xlsx')

def recarregar():
    quantidade.clear()
    tamanho.clear()
    metro_linear.clear()
    reforco_cinco.clear()
    reforco_seis.clear()
    reforco_oito.clear()
    reforco_dez.clear()
    reforco_doze.clear()
    reforco_dezesseis.clear()
    reload.clear()

    lista_vigas.delete(0,END)
    path= easygui.fileopenbox()
    pandas=read_excel(f'{path}')
    pandas.fillna(0,inplace=True)
    

    nome=Path(path).stem
    nome=str(nome)
    nome_entry.delete(0,END) #reseta entry para 0
    nome_entry.insert(0,f'{nome}') #reseta entry para 0

    quantidadepd=pandas['quantidade'].values.tolist()
    for q in quantidadepd:
        quantidade.append(q)
    tamanhopd=pandas['tamanho'].values.tolist()
    for t in tamanhopd:
        tamanho.append(t)
    metro_linearpd=pandas['metro'].values.tolist()
    for ml in metro_linearpd:
        metro_linear.append(ml)
    reforco_cincopd=pandas['5mm'].values.tolist()
    for cinco in reforco_cincopd:
        reforco_cinco.append(cinco)
    reforco_seispd=pandas['6mm'].values.tolist()
    for seis in reforco_seispd:
        reforco_seis.append(seis)
    reforco_oitopd=pandas['8mm'].values.tolist()
    for oito in reforco_oitopd:
        reforco_oito.append(oito)
    reforco_dezpd=pandas['10mm'].values.tolist()
    for dez in reforco_dezpd:
        reforco_dez.append(dez)
    reforco_dozepd=pandas['12,5mm'].values.tolist()
    for doze in reforco_dozepd:
        reforco_doze.append(doze)
    reforco_dezesseispd=pandas['16mm'].values.tolist()
    for dezesseis in reforco_dezesseispd:
        reforco_dezesseis.append(dezesseis)
    reloadpd=pandas['reload'].values.tolist()
    for rel in reloadpd:
        reload.append(rel)

    reloads=pandas['reload'].values.tolist()
    
    for f in reloads:
        lista_vigas.insert('end',f)
    
    

# #----------------------------------

# janela_principal.title('Calculadora de Lajes')
# janela_principal.configure(background='#000080')
# janela_principal.geometry('1200x800')
# janela_principal.resizable(True,True)
# janela_principal.maxsize(width=1920, height=1080)
# janela_principal.minsize(width=500,height=500)

# frame_titulo = Frame(janela_principal, bg='yellow', highlightbackground='white',highlightthickness=3)  
# frame_titulo.place(relx=0.02,rely=0.022, relwidth=0.97, relheight=0.045)
# frame_titulo.configure(background='yellow')
        
# frame_cliente= Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
# frame_cliente.place(relx=0.02,rely=0.1, relwidth=0.97, relheight=0.1)
# frame_cliente.configure(background='white')

# frame_vigas = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
# frame_vigas.place(relx=0.02,rely=0.22, relwidth=0.3, relheight=0.6)
# frame_vigas.configure(background='white')

# frame_lista = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
# frame_lista.place(relx=0.33,rely=0.22, relwidth=0.4, relheight=0.6)
# frame_lista.configure(background='white')

# frame_resultado = Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
# frame_resultado.place(relx=0.74,rely=0.22, relwidth=0.25, relheight=0.6)
# frame_resultado.configure(background='white')
        
# frame_botao= Frame(janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
# frame_botao.place(relx=0.33,rely=0.83, relwidth=0.66, relheight=0.1)
# frame_botao.configure(background='white')

# bt_apaga_u=Button(frame_botao, text='Apagar', fg='black',relief=RAISED,command=apagar_ultimo)
# bt_apaga_u.place(relx=0.015,rely=0.2,relwidth=0.1, relheight=0.6)


# bt_calc=Button(frame_botao, text='Calcular',fg='black', relief=RAISED,command=calcular)
# bt_calc.place(relx=0.43,rely=0.2,relwidth=0.25, relheight=0.6)

# bt_save=Button(frame_botao, text='Salvar (Criar arquivo .txt)', fg='black',relief=RAISED,command=salvar)
# bt_save.place(relx=0.72,rely=0.2,relwidth=0.25, relheight=0.6)
        
# bt_adicionar=Button(frame_vigas, text='Adicionar viga',fg='black', relief=RAISED,command=vigas_visual)
# bt_adicionar.place(relx=0.05,rely=0.89,relwidth=0.4, relheight=0.1)

# bt_recarregar=Button(frame_vigas, text='Abrir ".xls"',fg='black', relief=RAISED,command=recarregar)
# bt_recarregar.place(relx=0.5,rely=0.89,relwidth=0.4, relheight=0.1)
 
# titulo=Label(frame_titulo, text='CALCULADORA DE MATERIAS PARA LAJE PREMOLDADA',fg='black',font=('Helvetica',18))
# titulo.pack(side=TOP)
# titulo.configure(background='yellow')

#         #  MEDIDAS E QUANTIDADES DE VIGAS MAIS REFORÇOS
# vigas=Label(frame_vigas, text="Largura do comodo em METROS\n (calcula a quantidade de vigas)",fg='black')
# vigas.place(relx=0.03,rely=0.010)
# vigas.configure(background='white')

# varvg=IntVar()
# menos_viga_cb=Checkbutton(frame_vigas, text='menos 1 viga',variable=varvg,onvalue=1,offvalue=0)
# menos_viga_cb.place(relx=0.06, rely=.1)

# vigas_entry=Entry(frame_vigas,fg='black')
# vigas_entry.place(relx=0.6,rely=0.06,relwidth=0.3,relheight=0.05)
# vigas_entry.configure(background='lightgray')

# dash=Label(frame_vigas, text="----------------------------------------------------------------",fg='black')
# dash.place(relx=0.03,rely=0.15)
# dash.configure(background='white')

# tamanho_label=Label(frame_vigas, text='Tamanho das vigas em METROS',fg='black')
# tamanho_label.place(relx=0.03, rely=0.2)
# tamanho_label.configure(background='white')
        
# tamanho_entry=Entry(frame_vigas, fg='black')
# tamanho_entry.place(relx=0.6,rely=0.2,relwidth=0.3,relheight=0.05)
# tamanho_entry.configure(background='lightgray')

# dash2=Label(frame_vigas, text="----------------------------------------------------------------",fg='black')
# dash2.place(relx=0.03,rely=0.25)
# dash2.configure(background='white')

# lista_reforco=Label(frame_vigas, text='Selecione a quantidade de barras de reforço adicional:',fg='black')
# lista_reforco.place(relx=0.03,rely=0.3)
# lista_reforco.configure(background='white')

# cinco_mm=Label(frame_vigas, text='5mm ------------->',bg='white',fg='black')
# cinco_mm.place(relx=0.1,rely=0.37)

# cinco_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# cinco_mm_entry.place(relx=0.4,rely=0.37,relwidth=0.3,relheight=0.05)
# cinco_mm_entry.insert(0,'0')

# seis_mm=Label(frame_vigas, text='1/4 -- 6mm ------>',bg='white',fg='black')
# seis_mm.place(relx=0.1, rely=0.44)

# seis_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# seis_mm_entry.place(relx=0.4,rely=0.44,relwidth=0.3,relheight=0.05)
# seis_mm_entry.insert(0,'0')

# oito_mm=Label(frame_vigas, text='5/16 -- 8mm ----->',bg='white',fg='black')
# oito_mm.place(relx=0.1,rely=0.51)

# oito_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# oito_mm_entry.place(relx=0.4, rely=0.51, relwidth=0.3,relheight=0.05)
# oito_mm_entry.insert(0,'0')

# dez_mm=Label(frame_vigas, text='3/8 -- 10mm ----->',bg='white',fg='black')
# dez_mm.place(relx=0.1,rely=0.58)

# dez_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# dez_mm_entry.place(relx=0.4, rely=0.58, relwidth=0.3,relheight=0.05)
# dez_mm_entry.insert(0,'0')

# doze_mm=Label(frame_vigas, text='1/2 -- 12,5mm --->',bg='white',fg='black')
# doze_mm.place(relx=0.1,rely=0.65)

# doze_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# doze_mm_entry.place(relx=0.4, rely=0.65, relwidth=0.3,relheight=0.05)
# doze_mm_entry.insert(0,'0')

# dezesseis_mm=Label(frame_vigas, text='5/8 -- 16mm ----->',bg='white',fg='black')
# dezesseis_mm.place(relx=0.1,rely=0.72)


# dezesseis_mm_entry=Entry(frame_vigas, bg='lightgray',fg='black')
# dezesseis_mm_entry.place(relx=0.4, rely=0.72, relwidth=0.3,relheight=0.05)
# dezesseis_mm_entry.insert(0,'0')
# # DADOS DO CLIENTE
# nome=Label(frame_cliente, text='Nome:', bg='white',fg='black')
# nome.place(relx=0.12,rely=0.1)

# nome_entry=Entry(frame_cliente, bg='lightgray')
# nome_entry.place(relx=0.16,rely=0.11,relwidth=0.2)

# cpf=Label(frame_cliente, text='CPF:', bg='white',fg='black')
# cpf.place(relx=0.37,rely=0.1)

# cpf_entry=Entry(frame_cliente, bg='lightgray')
# cpf_entry.place(relx=0.4,rely=0.11,relwidth=0.2)

# telefone=Label(frame_cliente, text='Contato:', bg='white',fg='black')
# telefone.place(relx=0.6,rely=0.1)

# telefone_entry=Entry(frame_cliente, bg='lightgray')
# telefone_entry.place(relx=0.65,rely=0.11,relwidth=0.2)

# endereco=Label(frame_cliente, text='Endereço:', bg='white',fg='black')
# endereco.place(relx=0.05,rely=0.6)

# endereco_entry=Entry(frame_cliente, bg='lightgray')
# endereco_entry.place(relx=0.1,rely=0.6,relwidth=0.8)

# #quadro de lista de viga
# lista_vigas=Listbox(frame_lista, bg='lightgray',fg='black')
# lista_vigas.place(relx=0.01,rely=0.08, relwidth=0.98, relheight=0.9)
# lista_viga_titulo=Label(frame_lista, text='Lista de vigas',fg='black')
# lista_viga_titulo.place(relx=0.4, rely=0.01)
# barra_scroll=Scrollbar(lista_vigas)
# barra_scroll.pack(side=RIGHT, fill=Y)

# #espaço dos resultados

# resultados_label=Label(frame_resultado, text='Resultados',fg='black')
# resultados_label.place(relx=0.4,rely=0.01)

# resultados=Label(frame_resultado, text='',fg='black',justify=LEFT,font=('arial black', 12))
# resultados.place(relx=0.01,rely=0.08,relwidth=0.98,relheight=0.9)

# janela_principal.mainloop()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer






OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\acolajes\Dropbox\My PC (LAJES003)\Downloads\build\build\assets\frame0")





def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x680")
window.configure(bg = "#004A8B")


canvas = Canvas(
    window,
    bg = "#004A8B",
    height = 680,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    658.0,
    32.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    658.0,
    97.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    145.0,
    383.0,
    image=image_image_3
)


def checkb():

    if vareps_quarenta.get()==1:
        eps_trinta_cb.config(state='disabled')
    else:
        eps_trinta_cb.config(state='normal')

    if vareps_trinta.get()==1:
        eps_quarenta_cb.config(state='disabled')
    else:
        eps_quarenta_cb.config(state='normal')


vareps_trinta=IntVar(window)
eps_trinta_cb= Checkbutton(text='30CM',variable=vareps_trinta,onvalue=1,offvalue=0,disabledforeground="gray",command=checkb)
eps_trinta_cb.place(x=120,y=298)


vareps_quarenta=IntVar(window)
eps_quarenta_cb= Checkbutton(text='40CM',variable=vareps_quarenta,onvalue=1,offvalue=0,disabledforeground="gray",command=checkb)
eps_quarenta_cb.place(x=195,y=298)


def trelica():
    if h8.get()==1:
        h12_cb.config(state='disabled')
        h12_cb.deselect()
        h16_cb.config(state='disabled')
        h16_cb.deselect()
        h20_cb.config(state='disabled')
        h20_cb.deselect()
        h25_cb.config(state='disabled')
        h25_cb.deselect()
    
    elif h12.get()==1:
        h8_cb.config(state='disabled')
        h8_cb.deselect()
        h16_cb.config(state='disabled')
        h16_cb.deselect()
        h20_cb.config(state='disabled')
        h20_cb.deselect()
        h25_cb.config(state='disabled')
        h25_cb.deselect()
    elif h16.get()==1:
        h8_cb.config(state='disabled')
        h8_cb.deselect()
        h12_cb.config(state='disabled')
        h12_cb.deselect()
        h20_cb.config(state='disabled')
        h20_cb.deselect()
        h25_cb.config(state='disabled')
        h25_cb.deselect()
    elif h20.get()==1:
        h8_cb.config(state='disabled')
        h8_cb.deselect()
        h12_cb.config(state='disabled')
        h12_cb.deselect()
        h16_cb.config(state='disabled')
        h16_cb.deselect()
        h25_cb.config(state='disabled')
        h25_cb.deselect()
    elif h25.get()==1:
        h8_cb.config(state='disabled')
        h8_cb.deselect()
        h12_cb.config(state='disabled')
        h12_cb.deselect()
        h16_cb.config(state='disabled')
        h16_cb.deselect()
        h20_cb.config(state='disabled')
        h20_cb.deselect()
    else:
        h8_cb.config(state='normal')
        h12_cb.config(state='normal')
        h16_cb.config(state='normal')
        h20_cb.config(state='normal')
        h25_cb.config(state='normal')

h8=IntVar()
h8_cb= Checkbutton(state='normal',variable=h8,onvalue=1,offvalue=0,background='white',disabledforeground="gray",command=trelica)
h8_cb.place(x=18,y=220)

h12=IntVar()
h12_cb= Checkbutton(state='normal',variable=h12,onvalue=1,offvalue=0,background='white',disabledforeground="gray",command=trelica)
h12_cb.place(x=55,y=220)

h16=IntVar()
h16_cb= Checkbutton(state='normal',variable=h16,onvalue=1,offvalue=0,background='white',disabledforeground="gray",command=trelica)
h16_cb.place(x=105,y=220)

h20=IntVar()
h20_cb= Checkbutton(state='normal',variable=h20,onvalue=1,offvalue=0,background='white',disabledforeground="gray",command=trelica)
h20_cb.place(x=160,y=220)

h25=IntVar()
h25_cb= Checkbutton(state='normal',variable=h25,onvalue=1,offvalue=0,background='white',disabledforeground="gray",command=trelica)
h25_cb.place(x=225,y=220)




image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1064.0,
    382.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    617.0,
    383.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    613.0,
    234.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    613.0,
    395.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    407.0,
    546.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    613.0,
    546.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    819.0,
    546.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    1065.0,
    386.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    738.0,
    652.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    145.0,
    654.0,
    image=image_image_20
)

canvas.create_text(
    179.0,
    18.0,
    anchor="nw",
    text="CALCULADORA DE LAJE TRELIÇADA",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    149.0,
    69.0,
    anchor="nw",
    text="Cliente:",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    145.0,
    103.0,
    anchor="nw",
    text="Endereço:",
    fill="#000000",
    font=("Inter", 20 * -1)
)


nome_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
nome_entry.place(
    x=225.0,
    y=72.0,
    width=378.0,
    height=20.0
)


endereco_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
endereco_entry.place(
    x=264.0,
    y=100.0,
    width=895.0,
    height=22.0
)

canvas.create_text(
    625.0,
    70.0,
    anchor="nw",
    text="CPF:",
    fill="#000000",
    font=("Inter", 20 * -1)
)


cpf_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
cpf_entry.place(
    x=682.0,
    y=72.0,
    width=197.0,
    height=20.0
)

canvas.create_text(
    890.0,
    70.0,
    anchor="nw",
    text="Tel.:",
    fill="#000000",
    font=("Inter", 20 * -1)
)


telefone_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
telefone_entry.place(
    x=937.0,
    y=72.0,
    width=222.0,
    height=20.0
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    71.0,
    369.0,
    image=image_image_21
)

canvas.create_text(
    156.0,
    329.0,
    anchor="nw",
    text="LARGURA\n(quantidade de vigas)",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    158.0,
    425.0,
    anchor="nw",
    text="COMPRIMENTO",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    20.0,
    152.0,
    anchor="nw",
    text="ALTURA  DA TRELIÇA",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)


vigas_entry=Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
vigas_entry.place(
    x=160.0,
    y=362.0,
    width=61.0,
    height=19.0
)

canvas.create_text(
    226.0,
    365.0,
    anchor="nw",
    text="METROS",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)


vigas_quantidade_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
vigas_quantidade_entry.place(
    x=160.0,
    y=387.0,
    width=61.0,
    height=18.0
)

canvas.create_text(
    226.0,
    392.0,
    anchor="nw",
    text="VIGAS",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    45.0,
    397.0,
    anchor="nw",
    text="MENOS 1 VIGA",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)


tamanho_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
tamanho_entry.place(
    x=160.0,
    y=450.0,
    width=61.0,
    height=18.0
)

canvas.create_text(
    223.0,
    455.0,
    anchor="nw",
    text="METROS",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_rectangle(
    17.366424560546875,
    412.1398787498474,
    271.6487579345703,
    416.1172180175781,
    fill="#FFF400",
    outline="")

canvas.create_rectangle(
    17.366424560546875,
    326.7780303955078,
    271.6487579345703,
    330.75537109375,
    fill="#FFF400",
    outline="")

canvas.create_rectangle(
    17.366424560546875,
    486.3995819091797,
    271.6487579345703,
    490.3769226074219,
    fill="#FFF400",
    outline="")

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    87.0,
    449.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    31.0,
    191.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    116.0,
    185.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    174.0,
    183.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    238.0,
    181.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    66.0,
    188.0,
    image=image_image_27
)

canvas.create_text(
    23.0,
    208.0,
    anchor="nw",
    text="H8",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    58.0,
    208.0,
    anchor="nw",
    text="H12",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    105.0,
    208.0,
    anchor="nw",
    text="H16",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    161.0,
    208.0,
    anchor="nw",
    text="H20",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    226.0,
    208.0,
    anchor="nw",
    text="H25",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)



image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    222.0,
    274.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    147.0,
    270.0,
    image=image_image_30
)

# canvas.create_text(
#     136.0,
#     291.0,
#     anchor="nw",
#     text="30CM",
#     fill="#000000",
#     font=("Inter Bold", 10 * -1)
# )

canvas.create_text(
    25.0,
    266.0,
    anchor="nw",
    text="LARGURA \n     DO \nPREENCHIMENTO",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

# canvas.create_text(
#     196.0,
#     291.0,
#     anchor="nw",
#     text="40CM",
#     fill="#000000",
#     font=("Inter Bold", 10 * -1)
# )

canvas.create_text(
    28.0,
    491.0,
    anchor="nw",
    text="AÇO ADICIONAL(REFORÇO):",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    22.0,
    505.0,
    anchor="nw",
    text="(informar quantidade de barras)",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    220.0,
    575.0,
    image=image_image_31
)

canvas.create_text(
    30.0,
    520.0,
    anchor="nw",
    text="5mm = ",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    30.0,
    537.0,
    anchor="nw",
    text="6mm =",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    30.0,
    553.0,
    anchor="nw",
    text="8mm = ",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    28.0,
    568.0,
    anchor="nw",
    text="10mm = ",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    28.0,
    583.0,
    anchor="nw",
    text="12mm = ",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    28.0,
    599.0,
    anchor="nw",
    text="16mm = ",
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)


cinco_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
cinco_mm_entry.place(
    x=71.0,
    y=522.0,
    width=30.0,
    height=11.0
)


seis_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
seis_mm_entry.place(
    x=71.0,
    y=538.0,
    width=30.0,
    height=11.0
)


oito_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
oito_mm_entry.place(
    x=71.0,
    y=554.0,
    width=30.0,
    height=11.0
)


dez_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
dez_mm_entry.place(
    x=71.0,
    y=569.0,
    width=30.0,
    height=11.0
)


doze_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
doze_mm_entry.place(
    x=71.0,
    y=585.0,
    width=30.0,
    height=11.0
)


dezesseis_mm_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
dezesseis_mm_entry.place(
    x=71.0,
    y=600.0,
    width=30.0,
    height=11.0
)

bt_adicionar_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
bt_adicionar = Button(
    image=bt_adicionar_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=vigas_visual,
    relief="flat"
)
bt_adicionar.place(
    x=53.80316162109375,
    y=639.84716796875,
    width=182.38223266601562,
    height=28.847259521484375
)

bt_apaga_u_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
bt_apaga_u = Button(
    image=bt_apaga_u_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=apagar_ultimo,
    relief="flat"
)
bt_apaga_u.place(
    x=322.08612060546875,
    y=638.0253295898438,
    width=162.62486267089844,
    height=28.847259521484375
)

bt_calc_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
bt_calc = Button(
    image=bt_calc_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=calcular,
    relief="flat"
)
bt_calc.place(
    x=514.6905517578125,
    y=638.0253295898438,
    width=235.09896850585938,
    height=28.847259521484375
)

bt_save_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
bt_save = Button(
    image=bt_save_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=salvar,
    relief="flat"
)
bt_save.place(
    x=781.5368041992188,
    y=638.0253295898438,
    width=171.46316528320312,
    height=28.847259521484375
)

bt_recarregar_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
bt_recarregar= Button(
    image=bt_recarregar_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=recarregar,
    relief="flat"
)
bt_recarregar.place(
    x=980.0,
    y=637.9197387695312,
    width=171.463134765625,
    height=28.847259521484375
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    70.0,
    69.0,
    image=image_image_32
)

canvas.create_text(
    863.0,
    162.0,
    anchor="nw",
    text="H8",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    860.0,
    319.0,
    anchor="nw",
    text="H12",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    470.0,
    481.0,
    anchor="nw",
    text="H16",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    676.0,
    481.0,
    anchor="nw",
    text="H20",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    882.0,
    481.0,
    anchor="nw",
    text="H25",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)
window.resizable(False, False)
window.mainloop()


