import pytest
from search_engine import search_engine


@pytest.mark.parametrize(
    "documents, queries, expected",
    [
        (
            ["i love coffee", "coffee with milk and sugar", "free tea for everyone"],
            ["i like black coffee without milk", "everyone loves new year", "mary likes black coffee without milk"],
            [[1, 2], [3], [2, 1]],
        ),
        (
            [
                "buy flat in moscow",
                "rent flat in moscow",
                "sell flat in moscow",
                "want flat in moscow like crazy",
                "clean flat in moscow on weekends",
                "renovate flat in moscow",
            ],
            ["flat in moscow for crazy weekends"],
            [[4, 5, 1, 2, 3]],
        ),
        (
            ["i like dfs and bfs", "i like dfs dfs", "i like bfs with bfs and bfs"],
            ["dfs dfs dfs dfs bfs"],
            [[3, 1, 2]],
        ),
    ],
)
def test_search_engine(documents, queries, expected) -> None:
    assert search_engine(documents, queries) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["--timeout=1", "-vvv"])
