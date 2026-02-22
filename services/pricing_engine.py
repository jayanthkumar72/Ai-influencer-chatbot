def estimate_price(followers, engagement_rate, niche):

    multipliers = {
        "fashion": 1.2,
        "tech": 1.5,
        "lifestyle": 1.0,
        "fitness": 1.3
    }

    multiplier = multipliers.get(niche, 1.0)

    estimated_price = followers * engagement_rate * multiplier

    return round(estimated_price, 2)