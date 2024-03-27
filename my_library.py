import array

english_verb= ["answer", "work", "begin", "get", "use", "visit", "pay", "stay", "need", "last", "think", "discover", "invent", "complete", "permit", "tell", "eat", "find", "fish", "fly", "ask", "go", "win", "believe", "help", "buy", "know", "come", "run", "teach", "learn", "love", "lay", "make", "happen", "smoke", "travel", "run2", "call", "say", "sleep", "write", "swim", "see", "sing", "sit", "save", "put", "stand", "study", "lookfor", "dance", "meet", "separate", "drink", "earn", "forget", "lose", "promise", "understand", "wait", "wash", "wave", "wipe", "wish", "move"]
german_verb = ["antworten", "arbeiten", "beginnen", "bekommen", "benutzen", "besuchen", "bezahlen", "bleiben", "brauchen", "dauern", "denken", "entdecken", "erfinden", "erganzen", "erlauben", "erzahlen", "essen", "finden", "fischen", "fliegen", "fragen", "gehen", "gewinnen", "glauben", "helfen", "kaufen", "kennen", "kommen", "laufen", "lehren", "lernen", "lieben", "liegen", "machen", "passieren", "rauchen", "reisen", "rennen", "rufen", "sagen", "schlafen", "schreiben", "schwimmen", "sehen", "singen", "sitzen", "sparen", "stecken", "stehen", "studieren", "suchun", "tanzen", "treffen", "trennen", "trinken", "verdienen", "vergessen", "verlieren", "versprechen", "verstehen", "warten", "waschen", "winken", "wischen", "wunschen", "ziehen"]
english_noun =["time", "man", "hand", "day", "way", "eye", "thing", "head", "year", "room",
    "door", "woman", "face", "mother", "people", "night", "house", "father", "life", "back",
    "voice", "girl", "place", "boy", "car", "side", "arm", "child", "word", "moment",
    "hair", "foot", "water", "light", "world", "name", "friend", "window", "body", "table",
    "morning", "bed", "wall", "street", "school", "air", "ground", "hour", "end", "family",
    "guy", "child", "minute", "story", "god", "week", "work", "shoulder", "part", "mind",
    "book", "finger", "mouth", "child", "glass", "tree", "sound", "line", "wife", "heart", "money",
    "phone", "look", "leg", "chair", "office", "brother", "question", "city", "month", "baby",
    "home", "dog", "road", "idea", "kitchen", "property", "son", "job", "paper", "sister",
    "smile", "point", "thought", "love", "city", "death", "floor", "others", "fire", "step",
    "blood", "fact", "breath", "lip", "sun", "building", "number", "husband", "parent", "corner",
    "problem", "pair", "daughter", "bag", "hell", "peace", "business", "sky", "box", "person",
    "reason", "right", "skin", "father", "case", "piece", "doctor", "edge", "mother", "picture", "meaning",
    "ear", "second", "lady", "neck", "wind", "desk", "weapon", "stone", "coffee", "ship",
    "earth", "food", "horse", "field", "war", "afternoon", "sir", "room", "evening", "letter", "bar",
    "dream", "apartment", "chest", "game", "summer", "matter", "silence", "tip", "rock", "power",
    "clothing", "sign", "attention", "music", "condition", "bag", "dinner", "hall", "pain",
    "age", "river", "chance", "nose", "shadow", "police", "memory", "color", "knee", "wood",
    "shirt", "party", "land", "truck", "tooth", "bill", "scene", "land", "star", "bird",
    "bedroom", "uncle", "kind", "group", "truth", "difficulty", "crowd", "station", "tear",
    "class", "sea", "animal", "center", "feeling", "business", "mountain", "news", "shoe", "view",
    "tongue", "second", "lady", "neck", "wind", "computer", "flower", "ring", "bathroom", "metal",
    "moon", "song", "soldier", "radio", "story", "wave", "plan", "college", "fish", "garden",
    "train", "business", "policeman", "art", "beer", "north", "island", "bus", "smell", "noise",
    "mama", "park", "south", "pair", "sir", "plate", "jacket", "help", "dad", "grass", "thanks",
    "heat", "sleep", "brain", "service", "trip", "hit", "knife", "spot", "news", "sign",
    "teacher", "look", "village", "winter", "front", "law", "surface", "bank", "team", "maximum",
    "position", "stomach", "turn", "west", "lunch", "change", "creature", "soul", "leaf",
    "show", "gate", "palm", "plastic", "strength", "beach", "president", "shape", "smoke", "wheel",
    "silver", "roof", "weight", "tongue", "tea", "stretch", "angle", "shape", "tone", "circle",
    "spring", "porch", "leaf", "member", "pool", "need", "hope", "lake", "bridge",
    "period", "campaign", "campaign", "leader", "habit", "habit", "government", "citizen", "past",
    "neck", "water", "consumer", "count",]
german_noun = ["Die Zeit", "Der Mann", "Die Hand", "Der Tag", "Der Weg", "Das Auge", "Die Sache", "Der Kopf", "Das Jahr", "Das Zimmer",
    "Die Tür", "Die Frau", "Das Gesicht", "Die Mutter", "Die Leute", "Die Nacht", "Das Haus", "Der Vater", "Das Leben", "Der Rücken",
    "Die Stimme", "Das Mädchen", "Der Ort", "Der Junge", "Das Auto", "Die Seite", "Der Arm", "Das Kind", "Das Wort", "Der Moment",
    "Das Haar", "Der Fuß", "Das Wasser", "Das Licht", "Die Welt", "Der Name", "Der Freund", "Das Fenster", "Der Körper", "Der Tisch",
    "Der Morgen", "Das Bett", "Die Wand", "Die Straße", "Die Schule", "Die Luft", "Der Boden", "Die Stunde", "Das Ende", "Die Familie",
    "Der Kerl", "Das Kind", "Die Minute", "Die Geschichte", "Der Gott", "Die Woche", "Die Arbeit", "Die Schulter", "Der Teil", "Der Verstand",
    "Das Buch", "Der Finger", "Der Mund", "Das Kind", "Das Glas", "Der Baum", "Der Klang", "Die Linie", "Die Ehefrau", "Das Herz", "Das Geld",
    "Das Telefon", "Der Blick", "Das Bein", "Der Stuhl", "Das Büro", "Der Bruder", "Die Frage", "Die Stadt", "Der Monat", "Das Baby",
    "Das Zuhause", "Der Hund", "Die Straße", "Die Idee", "Die Küche", "Das Grundstück", "Der Sohn", "Der Job", "Das Papier", "Die Schwester",
    "Das Lächeln", "Der Punkt", "Der Gedanke", "Die Liebe", "Die Stadt", "Der Tod", "Der Boden", "Die Anderen", "Das Feuer", "Der Schritt",
    "Das Blut", "Die Tatsache", "Der Atem", "Die Lippe", "Die Sonne", "Das Gebäude", "Die Nummer", "Der Ehemann", "Der Elternteil", "Die Ecke",
    "Das Problem", "Das Paar", "Die Tochter", "Die Tasche", "Die Hölle", "Die Ruhe", "Das Geschäft", "Der Himmel", "Die Schachtel", "Die Person",
    "Der Grund", "Das Recht", "Die Haut", "Der Vater", "Der Fall", "Das Stück", "Der Arzt", "Der Rand", "Die Mutter", "Das Bild", "Der Sinn",
    "Das Ohr", "Die Sekunde", "Die Dame", "Der Hals", "Der Wind", "Der Schreibtisch", "Die Waffe", "Der Stein", "Der Kaffee", "Das Schiff",
    "Die Erde", "Das Essen", "Das Pferd", "Das Feld", "Der Krieg", "Der Nachmittag", "Der Herr", "Der Raum", "Der Abend", "Der Brief", "Die Bar",
    "Der Traum", "Die Wohnung", "Die Brust", "Das Spiel", "Der Sommer", "Die Angelegenheit", "Die Stille", "Die Spitze", "Der Felsen", "Die Macht",
    "Die Kleidung", "Das Schild", "Die Aufmerksamkeit", "Die Musik", "Der Zustand", "Die Tasche", "Das Abendessen", "Der Saal", "Der Schmerz",
    "Das Alter", "Der Fluss", "Die Chance", "Die Nase", "Der Schatten", "Die Polizei", "Die Erinnerung", "Die Farbe", "Das Knie", "Das Holz",
    "Das Hemd", "Die Party", "Das Land", "Der Lastwagen", "Der Zahn", "Die Rechnung", "Die Szene", "Das Land", "Der Stern", "Der Vogel",
    "Das Schlafzimmer", "Der Onkel", "Die Art", "Die Gruppe", "Die Wahrheit", "Die Schwierigkeit", "Die Menschenmenge", "Der Bahnhof", "Die Träne",
    "Die Klasse", "Das Meer", "Das Tier", "Das Zentrum", "Das Gefühl", "Das Geschäft", "Der Berg", "Die Nachrichten", "Der Schuh", "Die Sicht",
    "Die Zunge", "Die Sekunde", "Die Lady", "Der Hals", "Der Wind", "Der Computer", "Die Blume", "Der Ring", "Das Badezimmer", "Das Metall",
    "Der Mond", "Das Lied", "Der Soldat", "Das Radio", "Die Geschichte", "Die Welle", "Der Plan", "Das College", "Der Fisch", "Der Garten",
    "Der Zug", "Das Geschäft", "Der Polizist", "Die Kunst", "Das Bier", "Der Norden", "Die Insel", "Der Bus", "Der Geruch", "Das Geräusch",
    "Mama", "Der Park", "Der Süden", "Das Paar", "Der Herr", "Der Teller", "Die Jacke", "Die Hilfe", "Der Papa", "Das Gras", "Der Dank",
    "Die Hitze", "Der Schlaf", "Das Gehirn", "Der Service", "Die Reise", "Der Schlag", "Das Messer", "Der Fleck", "Die Nachricht", "Das Zeichen",
    "Der Lehrer", "Der Blick", "Das Dorf", "Der Winter", "Die Front", "Das Gesetz", "Die Oberfläche", "Die Bank", "Das Team", "Das Maximum",
    "Die Position", "Der Magen", "Die Wende", "Der Westen", "Das Mittagessen", "Die Veränderung", "Das Lebewesen", "Die Seele", "Das Blatt",
    "Die Show", "Das Tor", "Die Palme", "Das Plastik", "Die Kraft", "Der Strand", "Der Präsident", "Die Form", "Der Rauch", "Das Rad",
    "Das Silber", "Das Dach", "Das Gewicht", "Die Zunge", "Der Tee", "Die Strecke", "Der Winkel", "Die Form", "Der Ton", "Der Kreis",
    "Der Frühling", "Die Veranda", "Das Blatt", "Das Mitglied", "Der Pool", "Das Bedürfnis", "Die Hoffnung", "Der See", "Die Brücke",
    "Die Periode", "Die Kampagne", "Die Kampagne", "Der Führer", "Die Gewohnheit", "Die Gewohnheit", "Die Regierung", "Der Bürger", "Die Vergangenheit",
    "Der Hals", "Das Wasser", "Der Verbraucher", "Die Zählung"]
word_lib = [english_verb,german_verb,english_noun,german_noun]


def rev (num):
    if (num == 0):
        return 1
    elif(num == 1) :
        return 0
    elif(num == 2):
        return 3
    return 2 
def Translate (word_in):
    answer = {"not found"}
    for word in range(len(word_lib)):
        for type_it in range (len(word_lib[word])):
            if(word_in.lower() == word_lib[word][type_it]):
                answer = word_lib[rev(word)][type_it]
                break
    return answer

def Translation ():
    token = int(input("Enter the value for your token  :"))
    count = 0
    while count <+ token :
        word_in = input("Enter word to translate :")
        print('word translation is ' + str(Translate((word_in))) )
        count +=1

#Translation()

def prnoun_of (word_in):
   word_in.lower
   word = 0
   for word in range(len(word_lib)):
        for type_it in range (len(word_lib[word])):
            if(word_in.lower() == word_lib[word][type_it]):
                answer = word_lib[3][type_it]
                break
   desired_answer = answer[0:3]
   return desired_answer


def get_pronoun(): 
    for word in (range (len(german_verb))):
        answer = german_verb[word]
        desired_answer = answer[0:3]
    return desired_answer

my_word = "car"
print (prnoun_of(my_word) , Translate(my_word))
print (Translate("SEE"))
#def Translation (word_in,word_type):
        
    