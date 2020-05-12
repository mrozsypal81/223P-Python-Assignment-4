# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:09:33 2020

@author: jtcshen
"""

import pandas as pd

class product:
    def __init__(self, i, t, name):
        self._prodId = i
        self._prodType = t
        self._prodName = name
        self._clientList = list()
        
    def addClient2ClientList(self, cl):
        self._clientList.append(cl)
    
class client:
    def __init__(self, i, name):
        self._id = i
        self._name = name
        self._shoppingCart = None
        self._prefernceList = list()

    def setShoppingCart(self, sc):
        # implement one-to-one relationship
        self._shoppingCart = sc
        sc.setClient(self)

    def getShoppingCart(self):
        return self._shoppingCart

    def addProduct2PrefList(self, prd):
        # implement many-many relationship 
        self._preferenceList.append(prd)
        prd.addClient2ClientList(self)

    def delete(self):
        # first find the row index of this object
        df = pd.read_csv('client.csv')
        row = df[df.Id == self._id]
        print('+++ delete +++' , row.index[0])
        if (len(row.index) != 0):
            print('+++ Before ', df)
            df.drop(row.index[0], inplace=True)
            print('+++ After ', df)
            df.to_csv('client.csv', index=False)
            # Call shoppingCart delete() method 
        
    def save(self):
        # client.csv 
        try:
            df = pd.read_csv('client.csv')
            row = df[df.Id == self._id]
            if (len(row.index) != 0):
                # update an existing object 
                df.loc[row.index[0], 'Id'] = self._id
                df.loc[row.index[0], 'Name'] = self._name
                if (self._shoppingCart != None):
                    df.loc[row.index[0], 'Cart'] = self._shoppingCart._id
                else:
                    df.loc[row.index[0], 'Cart'] = self._shoppingCart
            else:
                # new object 
                cnt = len(df.index)
                print('+++ Appending to the DataFrame +++', df.index, df)
                if (self._shoppingCart != None): 
                    df.loc[cnt] = {'Id':self._id, 'Name': self._name, 'Cart':self._shoppingCart._id}
                else:
                    df.loc[cnt] = {'Id':self._id, 'Name': self._name, 'Cart':self._shoppingCart}                
        except:
            print('+++ Creating a new DataFrame +++')
            if (self._shoppingCart != None):
                df = pd.DataFrame([[self._id, self._name, self._shoppingCart._id]], columns=['Id', 'Name', 'Cart'])
            else:
                df = pd.DataFrame([[self._id, self._name, self._shoppingCart]], columns=['Id', 'Name', 'Cart'])                
        #
        df.to_csv('client.csv', index=False)
        if (self._shoppingCart != None):
            self._shoppingCart.save()
        
        
class shoppingCart:
    def __init__(self, i):
        self._id = i
        self._client = None
        self._orders = list()

    def setClient(self, cl):
        self._client = cl
        
    def addOrder(self, order):
        # implement the one-many relationship 
        self._orders.append(order)
        order.setCart(self)

    def delete(self):
        pass
    
    def save(self):
        # shoppingcart.csv 
        try:
            df = pd.read_csv('shoppingcart.csv')
            #Apply the same 'update object' logic here 
            
            cnt = len(df.index)
            print('+++ Appending to the DataFrame +++', df.index, df)
            df.loc[cnt] = {'Id':self._id, 'Client': self._client._id}
        except:
            print('+++ Creating a new DataFrame +++')
            df = pd.DataFrame([[self._id, self._client._id]], columns=['Id', 'Client'])
        #
        df.to_csv('shoppingcart.csv', index=False)
        for o in self._orders:
            o.save()
                
class order:
    def __init__(self, i, pr, q):
        self._id = i
        self._prodId = pr
        self._qty = q
        self._shoppingCart = None
        
    def setCart(self, sc):
        self._shoppingCart = sc

    def delete(self):
        pass
    
    def save(self):
        # order.csv 
        try:
            df = pd.read_csv('order.csv')
            #Apply the same 'update object' logic here 
            
            cnt = len(df.index)
            print('+++ Appending to the DataFrame +++', df.index, df)
            df.loc[cnt] = {'Id':self._id, 'Prod': self._prodId, 'QTY': self._qty, 'Cart':self._shoppingCart._id}
        except:
            print('+++ Creating a new DataFrame +++')
            df = pd.DataFrame([[self._id, self._prodId, self._qty, self._shoppingCart._id]], columns=['Id', 'Client', 'QTY', 'Cart'])
        #
        df.to_csv('order.csv', index=False)

#       
cObj = client(1, 'John Chen')

'''
scObj = shoppingCart(1)
cObj.setShoppingCart(scObj)
oObj = order(5, 'P1', 10)
scObj.addOrder(oObj)
oObj = order(6, 'P2', 4)
scObj.addOrder(oObj)
'''
#
cObj.save()

cObj._name = 'Geroge Chen'
cObj.save()

cObj.delete()


'''
cObj = client(2, 'Mary Chiu')
cObj.save()

cObj = client(3, 'James Shen')
cObj.save()
'''

'''        
cObj = client(1, 'John Chen')
scObj = shoppingCart(1)
cObj.setShoppingCart(scObj)

scObj = cObj.getShoppingCart()
o = order(1, 1, 4)
scObj.addOrder(o)
o = order(2, 2, 5)
scObj.addOrder(o)

prod = product(1, 'A', 'Product I')
prod1 = product(2, 'A', 'Product II')
prod2 = product(2, 'A', 'Product III')

cObj.addProduct2PrefList(prod)
cObj.addProduct2PrefList(prod2)

cObj1 = client(2, 'Frank Wang')
cObj1.addProduct2PrefList(prod1)
cObj1.addProduct2PrefList(prod2)
'''







