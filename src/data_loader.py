import pandas as pd


def load_stock_data(path):
    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def load_sentiment_data(path):
    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def load_news_data(path):
    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def load_company_summary(path):
    return pd.read_csv(path)


if __name__ == "__main__":

    stock = load_stock_data(
        "../data/raw/stock_data.csv"
    )

    sentiment = load_sentiment_data(
        "../data/raw/sentiment_data.csv"
    )

    news = load_news_data(
        "../data/raw/news_data.csv"
    )

    summary = load_company_summary(
        "../data/raw/company_summary.csv"
    )

    print("Stock:", stock.shape)
    print("Sentiment:", sentiment.shape)
    print("News:", news.shape)
    print("Summary:", summary.shape)