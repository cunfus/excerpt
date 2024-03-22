# excerpt

Excerpt your favorite lines from books and movies.

It's a toy for my blog.

## usage

1. start service `python app.py`
2. input data `python data_reader.py input-format.txt (etc.)`
3. test api `php index.php`

## input format

```txt
category source
hitokoto
hitokoto
...
```

## table format

| field    | meaning                             |
| -------- | ----------------------------------- |
| category | book, movie, lyrics, etc.           |
| source   | book/movie/etc name or someone said |
| hitokoto | words you like                      |


```json
{
    "category": "Book",
    "source": "William-Shakespeare",
    "hitokotos": []
}
```

