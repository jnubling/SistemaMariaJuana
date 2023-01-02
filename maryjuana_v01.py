# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:07:10 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk
from datetime import date
# from vendas import (Estoque,
#                     Financeiro,
#                     Gastos,
#                     Painel,
#                     Produtos,
#                     Vendas,
#                     tk,ttk)


class SistemaLoja(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.title("MARYJUANA")
        self.frames_dict = dict()
        
        # main_panel_frame = ttk.Frame(self)
        # main_panel_frame.pack(side="top",
        #                       fill="y",
        #                       expand=False,
        #                       padx=5, pady=5
        #                       )
        
        container_frame = ttk.Frame(self) 
        container_frame.pack(side="top",
                             fill="y",
                             expand=True,
                             padx=15, pady=5
                             )
        
        
        
        
        
        for FrameClass in (Painel, 
                           Vendas, 
                           Estoque, 
                           Gastos, 
                           Financeiro, 
                           Produtos):
            # creates all the frames and assign them to the frames dictionary
            frames = FrameClass(container_frame, self)
            self.frames_dict[FrameClass] = frames
            frames.grid(column=0, row=0, sticky="wnes")
            
        # frames = Vendas(container_frame, self)
        # self.frames_dict[Vendas] = frames
        # frames.pack(side="top", fill="both", expand=True)
        
        
        
        self.change_frame(Vendas)
        
    def change_frame(self, frame):
        # creates a function that changes the respective frame
        changing = self.frames_dict[frame]
        # self.bind("<Return>", changing.calculator)
        changing.tkraise() # raises the respective frame to the front
        
        
# class MainPanel(ttk.Frame):
#     def __init__(self, container_frame, frame_controller, **kwargs):
#         super().__init__(container_frame, **kwargs) 
        
class Vendas(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        # --variables--
        self.date_value = date.today().strftime("%d/%m/%Y")
        self.client_value = tk.StringVar()
        self.sell_type_selected = tk.StringVar()
        self.vendor_selected = tk.StringVar()
        # self.search_product_code = tk.StringVar()
        # self.search_product_name = tk.StringVar()
    

# =============================================================================
#         --small stock for test purposes--
# =============================================================================
        self.stock_test = {"ABFN0001": {"name": "Abafador vulcan colorido",
                                        "supplier": "Vuelta",
                                        "sell price": 30},
                           "ABFN0002": {"name": "Abafador dourado",
                                        "supplier": "Vuelta",
                                        "sell price": 50},
                            "ABFN0003": {"name": "Abafador hookah",
                                         "supplier": "Vuelta",
                                         "sell price": 45},
                            "BLDR0001": {"name": "Bolador Lion Rolling Circus",
                                         "supplier": "Fam/SP",
                                         "sell price": 25},
                            "BLNT0001": {"name": "Blunt Aleda",
                                         "supplier": "Ribeirao",
                                         "sell price": 30},
                            "BLNT0002": {"name": "King Blunt Mix",
                                         "supplier": "Cifal",
                                         "sell price": 8},
                            "CARV0001": {"name": "Carvao de Coco Zomo",
                                         "supplier": "Cifal",
                                         "sell price": 10},
                            "CHMB0001": {"name": "Cachimbo de madeira",
                                         "supplier": "Cifal",
                                         "sell price": 15},
                            "CNZR0002": {"name": "Cinzeiro Vidro",
                                         "supplier": "Cifal",
                                         "sell price": 25},
                            "ESSN0001": {"name": "Zomo Maldives Paradise",
                                         "supplier": "Vuelta",
                                         "sell price": 12}
                            }
        
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="we", ipadx=7)
        sells_button.grid(column=2, row=0, sticky="we", ipadx=7)
        stock_button.grid(column=4, row=0, sticky="we", ipadx=7)
        spents_button.grid(column=6, row=0, sticky="we", ipadx=7)
        financing_button.grid(column=8, row=0, sticky="we", ipadx=7)
        products_button.grid(column=10, row=0, sticky="we", ipadx=7)
        
# =============================================================================
#         # --widgets (first part)-- 
# =============================================================================
        vendor_label = ttk.Label(self, 
                               text="Vendedor "
                               )
        vendor_input = ttk.Combobox(self,
                               width=20,
                               textvariable=self.vendor_selected,
                               values=("Gabrieli",
                                       "Jhone",
                                       "Priscila",
                                       "Tiago"),
                               state="readonly"
                               )
        client_label = ttk.Label(self, 
                               text="Cliente "
                               )
        client_input = ttk.Entry(self,
                               width=23,
                               textvariable=self.client_value
                               )
        sell_type_label = ttk.Label(self, 
                               text="Tipo de Venda "
                               )
        sell_type_input = ttk.Combobox(self,
                               width=20,
                               textvariable=self.sell_type_selected,
                               values=("Cartão de Crédito",
                                       "Cartão de Débito",
                                       "Pagamento via PIX",
                                       "Pagamento em espécie",
                                       "Venda Fiado"),
                               state="readonly"
                               )
        
        
# =============================================================================
#         # --Layout (first part)--
# =============================================================================
        vendor_label.grid(column=2, row=2,
                          sticky="e"
                          )
        vendor_input.grid(column=3, row=2, columnspan=2,
                          sticky="w",
                          ipady=3
                          )
        
        client_label.grid(column=5, row=2,
                          sticky="e"
                          )
        client_input.grid(column=6, row=2, columnspan=2,
                          sticky="w",
                          ipady=3
                          )
        
        sell_type_label.grid(column=0, row=2,
                             sticky="e"
                             )
        sell_type_input.grid(column=1, row=2, columnspan=2,
                             sticky="w",
                             ipady=3
                             )

        
# =============================================================================
#         # --separator--
# =============================================================================
        ttk.Separator(self, orient="horizontal").grid(columnspan=7,
                                                      row=4, 
                                                      sticky="ew"
                                                      )
        
# =============================================================================
#         # --widgets (second part)--
# =============================================================================
        item_label = ttk.Label(self, text="\nItem")
        item_text = tk.Text(self,
                            height=10,
                            width=8
                            )
        
        product_label = ttk.Label(self, text="\nCód. Produto")
        product_text = tk.Text(self,
                            height=10,
                            width=10
                            )
        
        product_name_label = ttk.Label(self, text="\nNome do Produto")
        product_name_text = tk.Text(self,
                            height=10,
                            width=25
                            )
        
        # product_name_text.insert("1.0", self.stock_test["ABFN0001"]["name"])
        
        quantity_label = ttk.Label(self, text="\nQtd.")
        quantity_text = tk.Text(self,
                            height=10,
                            width=8
                            )
        
        unit_value_label = ttk.Label(self, text="\nVr. Unitário (R$)")
        unit_value_text = tk.Text(self,
                            height=10,
                            width=10
                            )
        
        total_label = ttk.Label(self, text="\nSubtotal (R$)")
        total_text = tk.Text(self,
                            height=10,
                            width=10
                            )
        
        discount_label = ttk.Label(self, text="\nDesc. (%)")
        discount_text = tk.Text(self,
                            height=10,
                            width=8
                            )
        
# =============================================================================
#         # --Layout (second part)--
# =============================================================================
        item_label.grid(column=0, row=5)
        item_text.grid(column=0, row=6)
        
        product_label.grid(column=1, row=5)
        product_text.grid(column=1, row=6)
        
        product_name_label.grid(column=2, row=5, columnspan=2)
        product_name_text.grid(column=2, row=6, columnspan=2)
        
        quantity_label.grid(column=4, row=5)
        quantity_text.grid(column=4, row=6)
        
        unit_value_label.grid(column=5, row=5)
        unit_value_text.grid(column=5, row=6)
        
        total_label.grid(column=6, row=5)
        total_text.grid(column=6, row=6)
        
        discount_label.grid(column=7, row=5)
        discount_text.grid(column=7, row=6)
        
# =============================================================================
#         # --separator--
# =============================================================================
        ttk.Separator(self, orient="horizontal").grid(columnspan=7,
                                                      row=7, 
                                                      sticky="ew"
                                                      )
        
# =============================================================================
#         # --Widgets (third part)--
# =============================================================================
        items_total_label = ttk.Label(self, text="Total de\nitens")
        items_total_text = tk.Text(self,
                            height=2, width=7
                            )
        total_products_label = ttk.Label(self, text="Total de\nprodutos")
        total_products_text = tk.Text(self,
                            height=2, width=7
                            )
        total_discounts_label = ttk.Label(self, text="Total de\ndescontos")
        total_discounts_text = tk.Text(self,
                            height=2, width=7
                            )
        total_general_label = ttk.Label(self, text="Total Geral")
        total_general_text = tk.Text(self,
                            height=2, width=7
                            )
        
# =============================================================================
#         # --layout (third part)--
# =============================================================================
        items_total_label.grid(column=0, row=8)
        items_total_text.grid(column=0, row=9)
        total_products_label.grid(column=5, row=8)
        total_products_text.grid(column=5, row=9)
        total_discounts_label.grid(column=6, row=8)
        total_discounts_text.grid(column=6, row=9)
        total_general_label.grid(column=7, row=8)
        total_general_text.grid(column=7, row=9)
        
# =============================================================================
#         # --Widgets (fourth part)--
# =============================================================================
        observation_label = ttk.Label(self, text="Observações ")
        observation_text = ttk.Entry(self, width=5)
        
        payment_condition_label = ttk.Label(self, text="Condição de\npagamento")
        payment_condition_text = ttk.Entry(self, width=7)
        
# =============================================================================
#         # --Layout (fourth part)--
# =============================================================================
        observation_label.grid(column=1, row=10)
        observation_text.grid(column=2, row=10, columnspan=3,
                              sticky="we", ipady=30)
        
        payment_condition_label.grid(column=5, row=10)
        payment_condition_text.grid(column=6, row=10, columnspan=2,
                                    sticky="we", ipady=5)
        
# =============================================================================
#         # --widgets (lateral part)
# =============================================================================
        date_label = ttk.Label(self, 
                               text="Data "
                               )
        date_text = tk.Text(self,
                               width=10,
                               height=1,
                               )
        date_text.insert("1.0", self.date_value)
        # date_change = date_text.get("1.0", "end")
        
        # self.entry_product_code = ttk.Entry(self,
        #                                     width=12
        #                                     )
        # entry_product_code_label = ttk.Label(self, text="Código       ")
        
        self.search_product = ttk.Entry(self,
                                        width=40
                                        )
        search_product_label = ttk.Label(self,
                                         text="Nome / Código do Produto  ")
        
        self.search_product_list = tk.Listbox(self,
                                              width=20, height=10)
        
        select_product_button = ttk.Button(self,
                                           text="Selecionar\nProduto",
                                           command=None)
        finalize_register_button = ttk.Button(self,
                                              text="Finalizar\nRegistrar",
                                              command=None
                                              )
# =============================================================================
#         # --layout (lateral part)--
# =============================================================================
        date_label.grid(column=10, row=1,
                        sticky="e"
                        )

        date_text.grid(column=11, row=1,
                       sticky="we",
                       ipady=3
                       )
        
        # entry_product_code_label.grid(column=8, row=1,
        #                               columnspan=2, sticky="e"
        #                               )
        # self.entry_product_code.grid(column=8, row=2, columnspan=2,
        #                              ipady=3, sticky="e"
        #                              )
        search_product_label.grid(column=9, row=2, sticky="w", columnspan=3
                                  )
        self.search_product.grid(column=9, row=3,
                                 sticky="w", columnspan=3,
                                 ipady=3
                                 )
        self.search_product_list.grid(column=9, row=4, rowspan=6, columnspan=3,
                                      sticky="wnes"
                                      )
        
        select_product_button.grid(column=10, row=10, sticky="w"
                                   )
        finalize_register_button.grid(column=11, row=10, sticky="w"
                                      )
        
        self.search_product.bind("<KeyRelease>", self.check_search)
        # self.entry_product_code.bind("<KeyRelease>", self.check_search)
        
        
# =============================================================================
#         --FUNCTIONS--        
# =============================================================================
    
    # update the search widget with the selected item in list    
    def check_search(self, *args):
        # get the product codes and names in the inventory dictionary
        product_data = []
        for code, name in self.stock_test.items():
            product_data.append(code + " " + list(name.values())[0])
            
        v = self.search_product.get()
        if v == "":
            data = product_data
        else:
            data = []
            for item in product_data:
                if v.lower() in item.lower():
                    data.append(item)
                    self.update_product_list(data)
        
    
    def update_product_list(self, data):
        # clear the list box
        self.search_product_list.delete(0, "end")
        # add values to the list box
        for value in data:
            self.search_product_list.insert(0, value)
        
    
    
    
class Painel(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        panel_frame = ttk.Label(self, text="Painel em desenvolvimento")
        panel_frame.grid(column=0, row=1, sticky="wnes")
        
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="w")
        sells_button.grid(column=2, row=0, sticky="w")
        stock_button.grid(column=4, row=0, sticky="w")
        spents_button.grid(column=6, row=0, sticky="w")
        financing_button.grid(column=8, row=0, sticky="w")
        products_button.grid(column=10, row=0, sticky="w")
        
        
class Estoque(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        panel_frame = ttk.Label(self, text="Estoque em desenvolvimento")
        panel_frame.grid(column=0, row=1, sticky="wnes")
        
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="wnes", ipadx=7)
        sells_button.grid(column=2, row=0, sticky="wnes", ipadx=7)
        stock_button.grid(column=3, row=0, sticky="wnes", ipadx=7)
        spents_button.grid(column=4, row=0, sticky="wnes", ipadx=7)
        financing_button.grid(column=5, row=0, sticky="wnes", ipadx=7)
        products_button.grid(column=6, row=0, sticky="wnes", ipadx=7)
        
        
class Gastos(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        panel_frame = ttk.Label(self, text="Gastos em desenvolvimento")
        panel_frame.grid(column=0, row=1, sticky="wnes")
        
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="wnes", ipadx=7)
        sells_button.grid(column=2, row=0, sticky="wnes", ipadx=7)
        stock_button.grid(column=3, row=0, sticky="wnes", ipadx=7)
        spents_button.grid(column=4, row=0, sticky="wnes", ipadx=7)
        financing_button.grid(column=5, row=0, sticky="wnes", ipadx=7)
        products_button.grid(column=6, row=0, sticky="wnes", ipadx=7)
        
        
class Financeiro(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        panel_frame = ttk.Label(self, text="Financeiro em desenvolvimento")
        panel_frame.grid(column=0, row=1, sticky="wnes")
        
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="wnes", ipadx=7)
        sells_button.grid(column=2, row=0, sticky="wnes", ipadx=7)
        stock_button.grid(column=3, row=0, sticky="wnes", ipadx=7)
        spents_button.grid(column=4, row=0, sticky="wnes", ipadx=7)
        financing_button.grid(column=5, row=0, sticky="wnes", ipadx=7)
        products_button.grid(column=6, row=0, sticky="wnes", ipadx=7)
        
class Produtos(ttk.Frame):
    def __init__(self, container_frame, frame_controller, **kwargs):
        super().__init__(container_frame, **kwargs)
        
        panel_frame = ttk.Label(self, text="Produtos em desenvolvimento")
        panel_frame.grid(column=0, row=1, sticky="wnes")
        
# =============================================================================
#         # --Control Panel Widgets--
# =============================================================================
        panel_button = ttk.Button(self,
                                  text="PAINEL",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Painel)
                                  )
        sells_button = ttk.Button(self,
                                  text="VENDAS",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Vendas)
                                  )
        stock_button = ttk.Button(self,
                                  text="ESTOQUE",
                                  width=20,
                                  command=lambda: frame_controller.change_frame(Estoque)
                                  )
        spents_button = ttk.Button(self,
                                   text="GASTOS",
                                   width=20,
                                   command=lambda: frame_controller.change_frame(Gastos)
                                   )
        financing_button = ttk.Button(self,
                                      text="FINANCEIRO",
                                      width=20,
                                      command=lambda: frame_controller.change_frame(Financeiro)
                                      )
        products_button = ttk.Button(self,
                                     text="PRODUTOS",
                                     width=20,
                                     command=lambda: frame_controller.change_frame(Produtos)
                                     )
        
        
# =============================================================================
#         # --Control Panel Layout--
# =============================================================================
        panel_button.grid(column=0, row=0, sticky="wnes", ipadx=7)
        sells_button.grid(column=2, row=0, sticky="wnes", ipadx=7)
        stock_button.grid(column=3, row=0, sticky="wnes", ipadx=7)
        spents_button.grid(column=4, row=0, sticky="wnes", ipadx=7)
        financing_button.grid(column=5, row=0, sticky="wnes", ipadx=7)
        products_button.grid(column=6, row=0, sticky="wnes", ipadx=7)
               





        
        
        
        
        
root = SistemaLoja()
root.columnconfigure(0, weight=1)
# style = ttk.Style(root)   
# print(style.theme_names())
# print(style.theme_use("alt"))

root.mainloop()