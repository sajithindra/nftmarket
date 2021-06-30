from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db= client["marketplace"]
artistcollections=db["artist"]
productcollections=db["product"]
buyercollections=db["buyer"]
gallerycollections=db["gallery"]

############### LOGIN  ############################

def artist_login(username,password):
    data = list(artistcollections.find({'username':username},{'password':1}))
    if (password  == data[0]['password']):return True
    else: return False

def buyer_login(username,password):
    data = list(buyercollections.find({'username':username},{'password':1}))
    if (password == data[0]['password']):return True
    else: return False

def gallery_login(username,password):
    data = list(gallerycollections.find({'username':username},{'password':1}))
    if (password  == data[0]['password']):return True
    else: return False

###############  END ##############################

############### UNIQUE USERNAME CHECK #############

def check_username(data):
    if (artistcollections.count_documents({'username':data})== 0 and buyercollections.count_documents({'username':data})== 0 and gallerycollections.count_documents({'username':data})==0):
        return False
    else: return True

############### END ################################

################# ARTIST ###########################

def push_artist(data):
    artistcollections.insert(data)

def get_artist_data(key,value):
    return list(artistcollections.find({key:value}))

################ END  #############################

###############  PRODUCT  ###########################

def push_product(data):
    productcollections.insert(data)

def get_product_data(key,value):
    return list(productcollections.find({key:value}))

###############  END  ###############################

###############  BUYER  #############################

def push_buyer(data):
    buyercollections.insert(data)

def get_buyer_data(key,value):
    return list(buyercollections.find({key:value}))

###############  END  #################################    

###############  GALLERY ##############################

def push_gallery(data):
    gallerycollections.insert(data)

def get_gallery_data(key,value):
    return list(gallerycollections.find({key:value}))

###############  END ##################################