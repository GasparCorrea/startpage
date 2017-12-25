from urllib.parse import quote
search_urls ={
    "g": "https://www.google.com/search?q=",
    "r": "https://reddit.com/r/",
    "yt": "https://www.youtube.com/results?search_query=",
    "to": "https://torrentz2.eu/search?f=",
    "wa": "https://www.wolframalpha.com/input/?i=",
    "tjpes": "https://translate.google.com/?um=1&ie=UTF-8&hl=es&client=tw-ob#ja/es/",
    "tesjp": "https://translate.google.com/?um=1&ie=UTF-8&hl=es&client=tw-ob#es/ja/",
    "tenes": "https://translate.google.com/?um=1&ie=UTF-8&hl=es&client=tw-ob#en/es/",
    "tesen": "https://translate.google.com/?um=1&ie=UTF-8&hl=es&client=tw-ob#es/en/",
    "img": "https://www.google.com/search?tbm=isch&q="
}

handy_urls = { 
    "gmail": "https://www.gmail.com",
    "github": "https://github.com",
    "3djuegos": "https://3djuegos.com",
    "fb": "https://facebook.com",
    "aula": "https://aula.usm.cl",
    "moodle": "https://moodle.inf.utfsm.cl",
    "sharelatex":"https://sharelatex.com",
    "calendar":"https://google.com/calendar",
    "md":"https://notehub.org",
    "wsp":"http://web.whatsapp.com/",
    "gr":"https://goodreads.com",
    "drive":"https://drive.google.com/drive/u/0/my-drive",
    "sl":"https://www.sharelatex.com/project",
    "re": "https://reddit.com"
}

def parse(text):
    text = text.split(" ")
    command = text[0]
    if command in handy_urls:
        return handy_urls[command]
    elif command in search_urls:
        return search_urls[command]+quote(" ".join(text[1:]),safe='')
    else:
        return search_urls['g']+quote(" ".join(text),safe='')
