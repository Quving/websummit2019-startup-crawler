# Websummit2019-Startup-Crawler
Crawl every startup that participated at the websummit 2019 from the [official website](https://websummit.com/featured-startups)


![](https://i.imgur.com/JbGUV54.jpg)

<img src="https://i.imgur.com/QNQEIcT.png" width="300"/>

# Setup
A chromedriver is necessary. Download and extract it to chromedriver/chromedriver

Link: https://chromedriver.chromium.org/home


# Usage
```python
python crawl_websummit_startups.py
```

# Output
A list of objects with the following structure
```json
{
  "id": "16cc94d4-5207-4c51-8ffe-43a0efd8b4da",
  "company_id": "dcb777dc-9100-4b39-ab27-1de6c45994f4",
  "fundraising": true,
  "meet_investors": true,
  "selected_for_machine_demo": false,
  "selected_for_pitch": false,
  "selected_for_forty_words": false,
  "selected_for_road_to": false,
  "selected_for_investor_meetings": true,
  "selected_for_startup_showcase": false,
  "recommended_amplify_startup": false,
  "recommended_impact_startup": false,
  "recommended_women_in_tech_startup": false,
  "recommended_web_three_startup": false,
  "stand_number": "G101, Exhibition date: Fri, Nov 4",
  "booth_url": null,
  "venue": null,
  "endorsed_by": null,
  "exhibition_date": "04-11-2022",
  "industry": "Sports, fitness & wellness",
  "logo_urls": {
   "tinythumb": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=48&h=48",
   "tiny": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=48&h=48",
   "thumb": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=100&h=100",
   "medium": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=300&h=300",
   "large": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1&auto=format&fit=fill&fill=solid&fill-color=white&w=600&h=600",
   "original": "https://web-summit-avenger.imgix.net/production/logos/original/ba199cac1a7a2b897146ac0575f1c58b1e4e42be.png?ixlib=rb-3.2.1"
  },
  "name": "1Fit",
  "city": "Almaty",
  "elevator_pitch": "1Fit is your last fitness app \u2014 gyms, personal trainers, and tailored recommendations based on users' data. Fastest-growing startup in CIS.",
  "external_urls": {
   "homepage": "https://1fit.app",
   "angellist": null,
   "crunchbase": null,
   "instagram": "https://instagram.com/1fit.app",
   "twitter": null,
   "facebook": "https://www.facebook.com/1fitapp",
   "linkedin": "https://www.linkedin.com/company/1fit",
   "youtube": null,
   "alternative_website": null
  },
  "country": "Kazakhstan",
  "funding_tier": "USD 500k - USD 1m",
  "attendance_ids": [
   "aa21b15d-2d9f-4f6f-bf03-952c22e8bcf2",
   "dd03c3df-7f4c-4250-9d5e-9f25c2eb5683",
   "e17ba3ca-178c-46be-8a8c-a2120d48f09c",
   "71e0d8ee-8ff2-4812-be46-af87cb0fcb3c",
   "4b9aa42b-651b-46d0-a0f1-6c149a0ee4c7"
  ],
  "track": "GROWTH",
  "currently_recruiting": true,
  "has_pitch_deck": true,
  "has_pitch_video": false,
  "has_appearance_video": false,
  "conference_industries": [],
  "funding_stage": "Series A",
  "revenue": "> $10,000,000",
  "geographical_regions": [
   "Asia"
  ],
  "_tags": [
   "ws22",
   "GROWTH"
  ],
  "objectID": "16cc94d4-5207-4c51-8ffe-43a0efd8b3da",
  "_highlightResult": {
   "stand_number": {
    "value": "G101, Exhibition date: Fri, Nov 4",
    "matchLevel": "none",
    "matchedWords": []
   },
   "industry": {
    "value": "Sports, fitness & wellness",
    "matchLevel": "none",
    "matchedWords": []
   },
   "name": {
    "value": "1Fit",
    "matchLevel": "none",
    "matchedWords": []
   },
   "city": {
    "value": "Almaty",
    "matchLevel": "none",
    "matchedWords": []
   },
   "elevator_pitch": {
    "value": "1Fit is your last fitness app \u2014 gyms, personal trainers, and tailored recommendations based on users' data. Fastest-growing startup in CIS.",
    "matchLevel": "none",
    "matchedWords": []
   },
   "country": {
    "value": "Kazakhstan",
    "matchLevel": "none",
    "matchedWords": []
   },
   "track": {
    "value": "GROWTH",
    "matchLevel": "none",
    "matchedWords": []
   }
  }
 }
```
