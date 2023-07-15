import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json

key_dict = json.loads(st.secrets(["textkey"]))
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="DripIndex")



st.title(':fire: DRIP INDEX')
st.header('Discover New Streetwear startup brands')

with st.expander('About this app'):
  st.write('This app serves as an index of various upcoming streetwear brands')
  st.write('if you would like your brand added, please email the country your brand is located, links to your store, ig and tiktok(if you have one) at dripdreamer@gmail.com ')
  st.write("Also if you have any feature requests message me and i'll see what i can do")

#Africa
st.header("Africa")
#Ghana
st.write(":flag-gh: __Free The Youth__ [shop](https://freetheyouth.net/collections/all) [insta](https://www.instagram.com/freetheyouth_ghana/?hl=en)")
#Nigeria
st.write(":flag-ng: __ashluxe__ : [shop](https://ash-luxe.com/collections/men) [insta](https://www.instagram.com/ashluxe/?hl=en)")
#Tanzania
st.write(":flag-tz: __Kitenge__ : [shop](https://kitengestore.com/) [insta](https://www.instagram.com/kitengestore/?hl=en)")


st.header("Antartica :flag-aq:")
st.write("Nothing...yet!")

# Asia
st.header("Asia")

#India
st.write(":flag-in: __audstro.__  : [shop](https://audstro.com/) [insta](https://www.instagram.com/audstro._/?hl=en)")
st.write(":flag-in: __op-haneen__ : [shop](https://ophaneen.com/) [insta](https://www.instagram.com/op_haneen/?hl=en)")
#japan
st.write(":flag-jp: __SEAVEN セヴン__ : [shop](https://www.antiqua.co.jp/html/page92.html) [insta](https://www.instagram.com/seaven.wear/?hl=en)")
#Malaysia
st.write(":flag-my: __Good Times__ : [shop](https://www.goodtimes.store/) [insta](https://www.instagram.com/goodtimeswear/)")
#Pakistan
st.write(":flag-pk: __Rastah__ : [shop](https://row.rastah.co/) [insta](https://www.instagram.com/rastahofficial/) [tiktok](https://www.instagram.com/rastahofficial/)")
st.write(":flag-pk: __Rooh__ : [Shop](https://roohshop.com/) [Insta](https://www.instagram.com/rooh.officialpk/)")
st.write(":flag-pk: __SANNUKI__ : [Shop](https://www.sannuki.co/) [Insta](https://www.instagram.com/shop.sannuki/?hl=en)")




#Australia 
st.header("Australia")
st.write("Au")
st.write(":flag-au: __Eruji__ : [insta](https://www.instagram.com/eruji_apparel/?hl=en)" )
st.write(":flag-au: __Lacorsia__ : [shop](https://lacorsia.co/collections/amalfi) [insta](https://www.instagram.com/lacorsiaco/)")
st.write(":flag-au: __Roki OverTime__ [shop](https://rokiovertime.com/collections/anime-hand-wraps) [insta](https://www.instagram.com/rokiovertime/) [tiktok](https://www.tiktok.com/@rokiovertime)")
st.write(":flag-au: __The Lucky Brand__ [shop](https://the-lucky-brand-4698.myshopify.com/) [tiktok](https://www.tiktok.com/@the.lucky.brand) ")

# New Zealand
st.write("Nz")
st.write(":flag-nz: __A Brutal Revelation__ [shop](https://abrutalrevelation.com/) [insta](https://www.instagram.com/abrutalrevelation/) [tiktok](https://www.tiktok.com/@behindbrvtl?lang=en)")
st.write(":flag-nz: __daplaza__ [shop](https://www.daplaza.co.nz/shop) [insta](https://www.instagram.com/daplaza/?hl=en)")
st.write(":flag-nz: __OCDC Clothing__ [shop](https://www.ocdcclothing.com/) [insta](https://www.instagram.com/ocdcclothing/?hl=en) [tiktok](https://www.tiktok.com/@ocdcclothing?lang=en)")
st.write(":flag-nz: __Skip The Boat__ [shop](https://skiptheboat.com/collections/all) [insta](https://www.instagram.com/skiptheboat/?hl=en)")

#Europe
st.header("Europe")
st.write(":flag-england: __Pokiey__ [shop](https://pokiey.com/collections/all) [insta](https://www.instagram.com/pokieyldn/)")
st.write(":flag-se: __DFTK clothing__ [shop](https://dfktclothing.com/collections/all-products) [insta](https://www.instagram.com/dfkt_clothing/)")

#North America
st.header("North America")
#Canada
st.write(":flag-ca: __Castle Frank__ [shop](https://castlefrankstudio.com/) [insta](https://www.instagram.com/castlefrankstudio/)")
st.write(":flag-ca: __Cuffs__ : [shop](https://www.xocuffs.com/) [insta](https://www.instagram.com/xocuffs/)")
st.write(":flag-ca: __True Hearts__ : [shop](https://truehearts.ca/) [insta](https://www.instagram.com/weekenddrive/)")
st.write(":flag-ca: __Weekend Drive__ : [shop](https://www.weekenddr.ca/) [insta](https://www.instagram.com/weekenddrive/)")
#USA
st.write(":flag-us: __Andino__ [shop](https://andinoofficial.com/collections/all)")
st.write(":flag-us: __Entry Level__ [shop](https://entrylevel-llc.com/) [insta](https://www.instagram.com/entrylevel.llc/)")
st.write(":flag-us: __Lazy Los Angeles__ : [shop](https://lazylosangeles.com/) [insta](https://www.instagram.com/lazylosangeles_/)")
st.write(":flag-us: __Lovely Hearts Kiss Club__ [shop](https://www.instagram.com/lacorsiaco/) [insta](https://www.instagram.com/lovelyheartskissclub/)")
st.write(":flag-us: __Pieces Cache__ : [shop](https://www.piecescache.com/store) [insta](https://www.instagram.com/pieces.cache/?hl=en)")

st.header("South America")
st.write("Nothing... yet!")




