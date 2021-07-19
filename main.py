from fastapi import FastAPI,UploadFile,File
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from mongo import push_buyer,push_product,push_artist,push_gallery
from mongo import get_artist_data,get_product_data,get_buyer_data ,get_gallery_data
from mongo import check_username
from mongo import artist_login,buyer_login,gallery_login
app = FastAPI()

################### ROOT ################################

@app.get('/')
async def root():
    return {'000': 'It works'}


####################### END #############################

#################### LOGIN ##############################

@app.get('/artistlogin')
async def artistlogin(username : str, password : str):
    
    if check_username(username) == False: return {"501":" Username does not exist"}
    else:
        f=artist_login(username,password)
        if f== True: return {"100":" Access Granted"}
        else: return {"101":" Access Denied"}

@app.get('/buyerlogin')
async def buyerlogin(username : str, password : str):
    if check_username(username) == False: return {"501":" Username does not exist"}
    else:
        f=buyer_login(username,password)
        if f== True: return {"100":" Access Granted"}
        else: return {"101":" Access Denied"}

@app.get('/gallerylogin')
async def gallerylogin(username : str, password : str):
    if check_username(username) == False: return {"501":" Username does not exist"}
    else: 
        f=gallery_login(username,password)
        if f== True: return {"100":" Access Granted"}
        else: return {"101":" Access Denied"}

####################  END ###############################

#################### UNIQUE USERNAME CHECK  #############

@app.get('/check_username')
async def check_unique_user(username:str):
    f=check_username(username)
    if f == False:
        return {"500":"Username available"}
    else:
        return {"501":"Username already exist"}

#################### END  ###############################

####################  ARTIST  ###########################

class Artist(BaseModel):
    username : str
    name : str
    email : str
    phone : str
    password : str
    user_type : str

@app.get('/artist')
async def get_artist(key:str,sid:str):
    data = get_artist_data(key,sid)
    send_data=[]
    for da in data:
        send_data.append(Artist(**da))
    return send_data

@app.post('/artist')
async def add_artist(artist:Artist):
    artist.name = artist.name.title()
    artist.user_type = 'artist'
    push_artist(artist.dict())
    os.mkdir(artist.username)
    return {"300":"Artist Added"}

####################  END  ###############################

####################  PRODUCT  ##########################
    
class Product(BaseModel):
    product_id : str
    name : str
    length : float
    breadth : float
    genre : str
    artist_name : str
    artist_username : str
    weight : float
    price : float

@app.get('/product')
async def get_product(key:str,pid:str):
    data=get_product_data(key,pid)
    send_data=[]
    for da in data:
        send_data.append(Product(**da))
    return send_data

@app.post('/product')
async def add_product(product:Product):
    product.name = product.name.title()
    product.artist_name= product.artist_name.title()
    push_product(product.dict())
    return {"400":"Product Added"}

####################  END  #################################

####################  BUYER  ##############################

class Buyer(BaseModel):
    username : str
    name : str 
    password: str
    email: str
    user_type : str

@app.get('/buyer')
async def get_buyer(key:str,bid:str):
    data = get_buyer_data(key,bid)
    send_data=[]
    for da in data:
        send_data.append(Buyer(**da))
    return send_data

@app.post('/buyer')
async def add_buyer(buyer:Buyer):
    buyer.name = buyer.name.title()
    buyer.user_type = 'buyer'
    push_buyer(buyer.dict())
    os.mkdir(buyer.username)
    return {"700":"Buyer Added"}

######################  END  ###############################

###################### GALLERY  ############################

class Gallery(BaseModel):
    username : str
    name : str
    password : str
    email : str
    phone : str
    bio : str

@app.get('/gallery')
async def get_gallery(key:str,gid : str):
    data = get_gallery_data(key,gid)
    send_data=[]
    for da in data:
        send_data.append(Gallery(**da))
    return send_data

@app.post('/gallery')
async def add_gallery(gallery : Gallery):
    gallery.name = gallery.name.title()
    push_gallery(gallery.dict())
    os.mkdir(gallery.username)
    return {'800': "Gallery added"}


####################  END  #################################

#################### PROFILE PIC ####################
@app.get('/profilepic')
async def get_profilepic(username : str):
    path = f'{username}/{username}.png'
    if os.path.exists(path):return await FileResponse(path,media_type = 'image/png')
    else:return {'901': "Profile picture not found"}


@app.post('/profilepic')
async def upload(username :str ,dp : UploadFile = File(...)):
    index = dp.content_type.index('/') 
    ext = dp.content_type[index+1:]
    path =f'{username}/{username}.{ext}'
    with open(path,'wb+') as f:
        f.write( await dp.read())
    return {'file': dp.filename , 'username': username, 'filecontent': dp.content_type}

#################### END ###################################

#################### ART WORK  #######################

@app.post('/artwork')
async def uploadartwork(username : str, name : str,artwork : UploadFile = File(...)):
    index =artwork.content_type.index('/')
    ext =artwork.content_type[index+1:]
    path = f'{username}/{name}.{ext}'
    with open(path,'wb+') as f:
        f.write( await artwork.read())
    return {'file': artwork.filename, 'username': username,'name': name}

#################### END ###################################
