import urllib.parse

def search_google_patents(keyword):
    base_url = "https://patents.google.com/"
    return f"{base_url}?q={urllib.parse.quote(keyword)}"

def check_idea_on_web(keyword):
    query = f"{keyword} site:startupindia.gov.in OR site:techcrunch.com"
    return f"https://www.bing.com/search?q={urllib.parse.quote(query)}"

def producthunt_manual_url():
    return "https://www.producthunt.com/"

# Example keyword
keyword = "AI waste management"

data = {
    "🔎 Google Patents": search_google_patents(keyword),
    "🌐 Search on StartupIndia/TechCrunch": check_idea_on_web(keyword),
    "🔥 Trending Today (Visit Manually)": producthunt_manual_url(),
}

for label, url in data.items():
    print(f"{label}: {url}")
