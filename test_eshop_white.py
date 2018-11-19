# -*- coding: utf-8 -*-

#%%
from eshop_white import checkout

def test_eshop_white_normalorder():
    normalorder=["Pick box","Guitar","Guitar Strings"]
    
    assert checkout(normalorder)==1015

def test_eshop_white_emptycart():
    emptycart=[]
    
    assert checkout(emptycart)=="Please add something to your shopping cart before checkout"
    
def test_eshop_white_preceding_spending_limit():
    tooexpensivecart=["Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Guitar","Pick box"]
    
    assert checkout(tooexpensivecart)=="Please remove items from your shopping bag, you preceded the spending limit"
    
