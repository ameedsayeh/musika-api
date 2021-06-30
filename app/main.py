from typing import Optional

from fastapi import FastAPI

app = FastAPI()


songs = [

{"name":"Chasing Stars","author":"STAR SEED","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/969/325x325/chasing-stars-1624964430-9z451Hiqm3.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/969/chasing-stars-1624964433-hg66qg0Tlv.mp3"},

{"name":"Talk Is Cheap","author":"VinDon, Magnus","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/967/325x325/talk-is-cheap-1624636831-KD0i3ASa2O.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/967/talk-is-cheap-1624636835-Z5Mlt4YdD9.mp3"},

{"name":"Feelings","author":"Azertion, Diviners","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/968/325x325/feelings-1624636843-jwJFZuXA5i.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/968/feelings-1624636846-EhVGAuxtSW.mp3"},

{"name":"Mr. Bully","author":"CHENDA","type":"Melodic Dubstep","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/965/325x325/mr-bully-1624525234-oKwDk6LSMA.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/965/mr-bully-1624525239-TwxU4630qj.mp3"},

{"name":"Band-Aid","author":"Halvorsen","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/966/325x325/1624533625_pJOE7fq9B7_Artwork.png","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/9…6/1624533627_7Io83Xo1Eh_Halvorsen---Band-Aid-NCS-Release.mp3"},

{"name":"Biology","author":"Gameboy Tetris, nublu, Cartoon","type":"Drum & Bass","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/964/325x325/biology-1624035630-RGVPK9iy6a.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/964/biology-1624035636-7bAv4E2brA.mp3"},

{"name":"Power !","author":"Godmode, LBLVNC","type":"Trap","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/963/325x325/power-1623945632-f2IYxNfTMb.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/963/power-1623945636-cmtHdqhL1v.mp3"},

{"name":"Sanity","author":"Whats Gud, Magnus","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/962/325x325/sanity-1623769234-GVRbCfFddp.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/962/sanity-1623769237-KjJMmVoEli.mp3"},

{"name":"Horizon","author":"GLNNA, Blosso, Slippy","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/961/325x325/horizon-1623423631-OFXaSSOVfa.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/961/horizon-1623423635-1ggDBXu1pj.mp3"},

{"name":"Grow","author":"VØR, Alisky","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/960/325x325/grow-1623340831-wgpasrzj7u.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/960/grow-1623340834-HSmBClszHl.mp3"},

{"name":"Hardwired","author":"Rameses B","type":"Drum & Bass","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/958/325x325/hardwired-1623153631-BwJ0DmW435.png","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/958/hardwired-1623153636-SAnRqY97C4.mp3"},

{"name":"Freefalling","author":"Facading","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/959/325x325/freefalling-1623322830-hoUJMHtt6U.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/959/freefalling-1623322833-xK24YExUmy.mp3"},

{"name":"Luna","author":"DNAKM, GalaxyTones, Abandoned","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/956/325x325/luna-1622725232-Xv27jVhE5w.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/956/luna-1622725235-DVd60web3Y.mp3"},

{"name":"Rewind","author":"More Plastic","type":"Drum & Bass","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/955/325x325/rewind-1622570432-cLyJ63pp3w.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/955/rewind-1622570435-qxaemvVFRf.mp3"},

{"name":"Healing","author":"Moe Aly, Clarx","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/954/325x325/healing-1622206832-2QFgqYRmfi.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/954/healing-1622206835-mUaTHvniGN.mp3"},

{"name":"Ten More Minutes","author":"Shiah Maisel, CHENDA","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/953/325x325/ten-more-minutes-1622116832-rfwiim0zzc.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/953/ten-more-minutes-1622116835-BjiBRTQJWr.mp3"},

{"name":"Need You","author":"if found","type":"Trap","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/952/325x325/need-you-1621951230-d2WKA4iTM3.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/952/need-you-1621951234-DdIeIyFtQ3.mp3"},

{"name":"Wait For Me","author":"Micah Martin, Doctor Neiman","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/9…4291_4xlexrHwfP_Doctor-Neiman---Wait-For-Me-Artwork-2021.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/951/wait-for-me-1621612835-LSVlmFX5IJ.mp3"},

{"name":"Game Over","author":"EMM, Egzod","type":"Trap","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/950/325x325/game-over-1621515630-RkJKCl3hXb.png","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/950/game-over-1621515634-QoO4gwi3Oq.mp3"},

{"name":"Found You","author":"RYVM, Avaya, Time To Talk","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/949/325x325/found-you-1621346432-RnS6G01xoa.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/949/found-you-1621346435-SPf25x7uLM.mp3"},

{"name":"Mr. Bully","author":"CHENDA","type":"Melodic Dubstep","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/965/325x325/mr-bully-1624525234-oKwDk6LSMA.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/965/mr-bully-1624525239-TwxU4630qj.mp3"},

{"name":"Band-Aid","author":"Halvorsen","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/966/325x325/1624533625_pJOE7fq9B7_Artwork.png","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/9…6/1624533627_7Io83Xo1Eh_Halvorsen---Band-Aid-NCS-Release.mp3"},

{"name":"Talk Is Cheap","author":"VinDon, Magnus","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/967/325x325/talk-is-cheap-1624636831-KD0i3ASa2O.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/967/talk-is-cheap-1624636835-Z5Mlt4YdD9.mp3"},

{"name":"Feelings","author":"Azertion, Diviners","type":"House","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/968/325x325/feelings-1624636843-jwJFZuXA5i.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/968/feelings-1624636846-EhVGAuxtSW.mp3"},

{"name":"Chasing Stars","author":"STAR SEED","type":"Electronic","image_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/969/325x325/chasing-stars-1624964430-9z451Hiqm3.jpg","file_url":"https://ncsmusic.s3.eu-west-1.amazonaws.com/tracks/000/000/969/chasing-stars-1624964433-hg66qg0Tlv.mp3"}

]

@app.get("/")
def read_root():
    return "Welcome to Musika-api"


@app.get("/songs")
def read_item():
    return songs