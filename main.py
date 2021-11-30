import pynytimes

nyt = pynytimes.NYTAPI("zAYv3eaPSZwkYgfwPZVQE4MNMdQBwSNp", parse_dates=True)

articles = nyt.article_search(
    query="intersex",
    results=30,
    options={
        "sort": "oldest"
    }
)

print(articles)