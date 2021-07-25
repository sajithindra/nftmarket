from google.cloud import firestore
db=firestore.Client('appdata-320712')

############### LOGIN  ##############################

def artist_login(username,password):
    if password == db.collection('artist').document(f'{username}').get().to_dict()['password']:
        return True
    else: return False

def buyer_login(username,password):
    if password == db.collection('buyer').document(f'{username}').get().to_dict()['password']:
        return True
    else: return False
def gallery_login(username,password):
    if password == db.collection('gallery').document(f'{username}').get().to_dict()['password']:
        return True
    else: return False


############### END LOGIN ###########################

################ CHECK USERNAME #####################

def check_username(username):
    artist =db.collection('artist').document(f'{username}').get().to_dict()
    buyer = db.collection('buyer').document(f'{username}').get().to_dict()
    gallery = db.collection('gallery').document(f'{username}').get().to_dict()
    if (artist == None and buyer == None and gallery == None):
        return False
    else: return True

############### END CHECK USERNAME ##################

################# ARTIST  ###########################

def get_artist_data(username):
    return db.collection('artist').document(f'{username}').get().to_dict()

def push_artist(username,data):
    db.collection('artist').document(f'{username}').set(data)

################ END ARTIST ###########################

############### PRODUCT  ##############################

def get_product_data(name):
    return db.collection('product').document(f'{name}').get().to_dict()

def push_product(name,data):
    db.collection('product').document(f'{name}').set(data)
############### END PRODUCT ###########################

################  BUYER  ##############################

def get_buyer_data(username):
    return db.collection('buyer').document(f'{username}').get().to_dict()

def push_buyer(username,data):
    db.collection('buyer').document(f'{username}').set(data)

################  END BUYER #############################

############### GALLERY  ################################

def get_gallery_data(username):
    return db.collection('gallery').document(f'{username}').get().to_dict()
def push_gallery(username,data):
    db.collection('gallery').document(f'{username}').set(data)


############### END GALLERY #############################

############### PROFILE PIC ################################

def get_profilepic_path(username):
    return db.collection('profilepic').document(f'{username}').get().to_dict()['path']

def push_profilepic_data(username,data):
    db.collection('profilepic').document(f'{username}').set(data)

################  END PROFILEPIC ###########################

############### ART WORK METADATA ##########################

def get_artmeta_data(username):
    return db.collection('art_meta').document(f'{username}').get().to_dict()

def push_artmeta_data(username,data):
    db.collection('art_meta').document(f'{username}').set(data)

############### END  #######################################
