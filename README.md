# vk-keywords-extractor
This project helps to analyse vk pages, using vk API and [text2kewords keyword extractor](https://github.com/0x7o/text2keywords).
It may be necessary to download [keyT5. Base (small) version](https://huggingface.co/0x7194633/keyt5-base) and [keyT5. Large version] (https://huggingface.co/0x7194633/keyt5-large) files to local machine

## Requirements
You can install all necessary packages using `pip install -r requirements.txt`

## Usage:
`extractkw.py PAGE_ID POSTS_NUMBER USE_LARGE_MODEL`
* PAGE_ID - id of personal page / group page (Page must have opened privacy settings)
* POSTS_NUMBER - number of posts to analyse (From 1 to 100)
* USE_LARGE_MODEL - True / False parameters specifies wich model to use as a keyword extractor. *If True - increases quality but works slower*

**It takes about 9 min to analyse 100 posts with large model and 3 min for base model**

## Example:
`extractkw.py 1 100 True`

Returns:
> Главные темы страницы:  ['социальные сети и сообщества', 'архитектура', 'разработка веб', 'архитектура архитектура', 'информационная безопасность']

*Sctipt also creates .txt file containing main themes of analysing page in project folder*

