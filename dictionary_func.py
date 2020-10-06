import spacy
nlp= spacy.load("en_core_web_sm")
dict1= {"turn": {"light","sync","account","hotspot","mode","blutooth","wifi","internet","data","flashlight","phone","app"},
       "switch": {"light","hotspot","blutooth","window","wifi","internet","data","flashlight","phone"},
       "open":{"calender","panel","setting","file","app","mail","message","document","sheet","game","photo","image","video","drive","file","wallpaper","google","slide"},
       "set":{"alarm","reminder","timer","ringtone","mode","location","font","theme","wallpaper"},
       "reset":{"alarm","date","timer","time"},
       "save":{"message","file","folder","document","mail","headline","note","contact"},
       "update":{"phone","mobile","app","schedule","note"},
       "mark":{"reminder","mail","message","done"},
       "book":{"event","cab","ticket","table","service","room","hotel"},
       "call":{"contact"},
       "close":{"recent","app"},
       "message":{"contact"},
       "find":{"file","document","file","photo","video","mail"},
       "search":{"video","photo","contact","file","document","file"},
       "play":{"music","video","audio","ringtone"},
       "check":{"message","reminder","calender","mail"},
       "record":{"video","audio","voice"},
       "read":{"message","notification","file","folder","document","mail","headline","note"},
       "remove":{"contact","wallpaper","reminder","alarm","ringtone","file","folder","document","note","cache","event"},
       "add":{"image","music","audio","photo","contact","alarm","reminder","note","document","file","folder","event"},
       "write":{"message","file","document","sheet","mail","note","folder"},
       "click":{"photo","pic","image","selfie"},
       "play":{"game","music","song","audio","video"},
       "wake":{"me"},
       "show":{"notification","recent","release","screen","homescreen","headline","call","app","contact","message","game","slide","video","mail","photo","image","note","folder","file","document","time","date"},
       "send":{"image","message","video","audio","mail","file","sheet","slide"},
       "share":{"image","picture","pic","photo","message","video","audio","mail","file","sheet","slide","hotspot"},
       "download":{"image","video","audio","file","photo","music","song","document","app"},
       "create":{"new","contact","message","reminder","event","schedule","calendar","mail","note","folder","file","document","sheet","account"},
       "change":{"wallpaper","music","reminder","ringtone","event","schedule","file","time","date","theme","hotspot","wifi","mode","account"},
       "rotate":{"screen","display","wallpaper","app"},
       "increase":{"volume","brightness","resolution","audio","sound"},
       "reduce":{"volume","brightness","resolution","audio","sound"},
       "decrease":{"volume","brightness","resolution","audio","sound"},
       "update":{"app","mail","slide","wallpaper","contact"},
       "clean":{"cache","memory","disk","space"},
       "order":{"food","part","item","clothes","drink"},
       "make":{"call","note"},
       "take":{"note","screenshot","picture","selfie"},
       "launch":{"app"},
       "buy":{"food","drink","clothes","book","furniture","car","mobile","snacks"},
       "apply":{"effect","wallpaper"},
       "swipe":{"right","left","up","down","bottom"},
       "go":{"next","back","forward","setting"},
       "disconnect":{"wifi","internet","net"},
       "scan":{"wifi","bluetooth"},
       "stop":{"music","send"}
        }


perm_list=["call","message","order","block","scan","link","buy","mail"]
def find(sentence):
    sentence= nlp(sentence)
    words=[]
    for token in sentence:
        words.append(token.lemma_)
    for i in perm_list:
        if i in words:
            return 1
    for i,j in dict1.items():
        if i in words:
            for m in j:
                if m in words:
                    return 1
    return 0

# Test input for user
#sentence=input("enter the command: ")
#print(find(sentence))
    
