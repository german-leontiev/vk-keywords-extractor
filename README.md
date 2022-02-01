# vk-keywords-extractor
This project helps to analyse vk pages, using keyword extractor

## Requirements
You can install all necessary packages using `pip install -r requirements.txt`

## Usage:
`extractkw.py PAGE_ID POSTS_NUMBER USE_LARGE_MODEL`
* PAGE_ID - id of personal page / group page (Page must have opened privacy settings)
* POSTS_NUMBER - number of posts to analyse (From 1 to 100)
* USE_LARGE_MODEL - True / False parameters specifies wich model to use as a keyword extractor. *If True - increases quality but works slower*

## Example:
`extractkw.py 1 100 True`

Главные темы страницы:  ['социальные сети и сообщества', 'архитектура', 'разработка веб', 'архитектура архитектура', 'информационная безопасность']

*Sctipt also creates .txt file containing main themes of analysing page*

