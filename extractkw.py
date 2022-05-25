from tqdm import tqdm
import vk
from itertools import groupby
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import sys

MAIN_TOKEN = "ENTER_YOUR_TOKEN_HERE"

def vk_auth(TOKEN=MAIN_TOKEN):
    session = vk.AuthSession(access_token=TOKEN)
    return vk.API(session)


def get_posts(OWNER_ID,
              N_POSTS=100,
              TOKEN=MAIN_TOKEN):
    # Авторизация в вк API по токену
    vk_api = vk_auth(TOKEN)
    # Получение постов со страницы
    wall_posts = vk_api.wall.get(owner_id=OWNER_ID, v=5.131, count=N_POSTS)
    return wall_posts


def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    s = tokenizer.decode(hypotheses[0], skip_special_tokens=True)
    s = s.replace('; ', ';').replace(' ;', ';').lower().split(';')[:-1]
    s = [el for el, _ in groupby(s)]
    return s


def model_initialize(MODEL_LARGE=True):
    if MODEL_LARGE:
        model_name = "keyt5-large"
    else:
        model_name = "keyt5-base"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


def get_keywords(OWNER_ID,
                 N_POSTS=100,
                 MODEL_LARGE=True,
                 TOP_N=5,
                 TOKEN=MAIN_TOKEN):
    
    # Получение постов со страницы
    wall_posts = get_posts(OWNER_ID=OWNER_ID,
                           N_POSTS=N_POSTS,
                           TOKEN=TOKEN)
    
    
    # Извлечене ключевых слов из каждого поста
    keywords = []
    for post in tqdm(wall_posts['items']):
        keywords.append(generate(post['text'], top_p=1.0, max_length=64))
    
    # Составление словаря частотности ключевого слова
    total_ls = [j for sub in keywords for j in sub]
    d = {}
    for i, key in enumerate(list(set(total_ls))):
        d[key] = total_ls.count(key)
    
    # Возврат top-n ключевах слов со страницы
    main_themes = []
    for i in dict(sorted(d.items(), key=lambda item: item[1], reverse=True)):
        main_themes.append(i)
        if len(main_themes) == TOP_N:
            break
    return main_themes


def save():
    with open(f'{PAGE_ID}_main_themes.txt', 'w') as f:
        f.write(str(main_themes))


PAGE_ID, N_POSTS, MODEL_LARGE = str(sys.argv[1]), int(sys.argv[2]), bool(sys.argv[3])


tokenizer, model = model_initialize(MODEL_LARGE)
main_themes = get_keywords(PAGE_ID, N_POSTS=N_POSTS)
print("Главные темы страницы: ", main_themes)
save()




