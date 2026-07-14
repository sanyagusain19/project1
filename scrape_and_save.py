import json
from bs4 import BeautifulSoup
import requests


def top_companies_scraper():

    url = "https://www.ambitionbox.com/list-of-companies?page=1"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    company_cards = soup.find_all("div", class_="companyCardWrapper")

    companies = []

    for company in company_cards:

        name = company.find("h2").get_text(strip=True)

        rating = company.find(
            "span",
            class_="companyCardWrapper__companyRatingCount"
        ).get_text(strip=True)

        spans = company.find_all("span")
        location = spans[2].get_text(strip=True) if len(spans) > 2 else "NA"

        rating_values = company.find_all(
            "span",
            class_="companyCardWrapper__ratingValues"
        )

        best_rated_for = (
            rating_values[0].get_text(strip=True)
            if len(rating_values) > 0
            else "NA"
        )

        worst_rated_for = (
            rating_values[1].get_text(strip=True)
            if len(rating_values) > 1
            else "NA"
        )

        companies.append({
            "name": name,
            "rating": rating,
            "location": location,
            "best_rated_for": best_rated_for,
            "worst_rated_for": worst_rated_for
        })

    return companies


if __name__ == "__main__":
    data = top_companies_scraper()
    with open("companies_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} companies to companies_data.json")