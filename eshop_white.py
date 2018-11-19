# -*- coding: utf-8 -*-

#%%
products={"Guitar":"1000",
          "Pick box":"5",
          "Guitar Strings":"10"}

def checkout(list):
    cost=0
    if list==[]:
        return "Please add something to your shopping cart before checkout"
    else:
        for product in list:
            cost+=int(products[product])
            if cost>10000:
                return "Please remove items from your shopping bag, you preceded the spending limit"
        return cost
    