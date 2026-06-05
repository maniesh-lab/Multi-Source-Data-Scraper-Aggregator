from scraper import scrape_books
from processors import clean_data
from processors import merge_datasets
from visualizer import generate_charts

def main():
    mystery_raw = scrape_books("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
    classics_raw = scrape_books("https://books.toscrape.com/catalogue/category/books/classics_6/index.html")
    thriller_raw= scrape_books("https://books.toscrape.com/catalogue/category/books/thriller_37/index.html")
    philosophy_raw = scrape_books("https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html")


    mystery_clean = clean_data(mystery_raw)
    classics_clean = clean_data(classics_raw)
    thriller_clean = clean_data(thriller_raw)
    philosophy_clean = clean_data(philosophy_raw)


    combined_df = merge_datasets(mystery_clean, classics_clean,thriller_clean,philosophy_clean)

    generate_charts(combined_df)

    output_path = "output/combined_books.csv"
    combined_df.to_csv(output_path, index=False)

    print(f"Scraped {len(combined_df)} books across {combined_df['Category'].nunique()} categories → saved to {output_path}")

if __name__ == "__main__":
    main()