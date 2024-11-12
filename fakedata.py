import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()
Faker.seed(0)
random.seed(0)

# Generate Users with varied personas
def generate_users(num_users):
    users = []
    for user_id in range(1, num_users + 1):
        users.append({
            "User_ID": user_id,
            "Name": fake.name(),
            "Age": random.randint(18, 70),
            "Gender": random.choice(['M', 'F']),
            "Location": fake.city(),
            "Occupation": fake.job(),
            "Income_Bracket": random.choice(['Low', 'Medium', 'High']),
            "Investment_Experience_Level": random.choice(['Beginner', 'Intermediate', 'Expert']),
            "Ethical_Preferences": random.choice(['Environmental', 'Social', 'Governance', 'Neutral']),
            "Financial_Goals": random.choice(['Retirement', 'Wealth Accumulation', 'Income']),
            "Risk_Tolerance": random.choice(['Low', 'Moderate', 'High'])
        })
    return pd.DataFrame(users)

# Generate Portfolios linked to Users
def generate_portfolios(users, num_portfolios):
    portfolios = []
    for portfolio_id in range(1, num_portfolios + 1):
        user_id = random.choice(users['User_ID'])
        portfolios.append({
            "Portfolio_ID": portfolio_id,
            "User_ID": user_id,
            "Portfolio_Name": fake.word().capitalize() + " Fund",
            "Creation_Date": fake.date_this_decade(),
            "Risk_Tolerance": random.choice(['Low', 'Moderate', 'High']),
            "Goal_Type": random.choice(['Retirement', 'Wealth Growth', 'Income Generation']),
            "Investment_Strategy": random.choice(['ESG Focused', 'High-Risk', 'Income Focused']),
            "Total_Asset_Value": random.uniform(50000, 500000),
            "Asset_Distribution": {
                "Equity": random.randint(40, 80),
                "Bonds": random.randint(10, 40),
                "Cash": random.randint(5, 20)
            }
        })
    return pd.DataFrame(portfolios)

# Generate Investment Assets
def generate_assets(num_assets):
    assets = []
    for asset_id in range(1, num_assets + 1):
        assets.append({
            "Asset_ID": asset_id,
            "Asset_Name": fake.company(),
            "Ticker_Symbol": fake.lexify(text='???').upper(),
            "Asset_Type": random.choice(['Stock', 'Mutual Fund', 'Bond', 'ETF']),
            "Sector": random.choice(['Technology', 'Renewable', 'Healthcare', 'Finance']),
            "Market": random.choice(['NYSE', 'NASDAQ']),
            "Risk_Level": random.choice(['Low', 'Moderate', 'High']),
            "Expected_Return_Rate": round(random.uniform(2, 10), 2),
            "Volatility": round(random.uniform(5, 20), 2),
            "Dividend_Yield": round(random.uniform(0, 5), 2),
            "ESG_Score": random.randint(50, 100),
            "Ethical_Alignment": random.choice(['Environmental', 'Social', 'Governance', 'Neutral']),
            "Market_Cap": random.uniform(1e6, 1e10),
            "Inception_Date": fake.date_this_century()
        })
    return pd.DataFrame(assets)

# Generate Transactions for each Portfolio and Asset
def generate_transactions(portfolios, assets, num_transactions):
    transactions = []
    for transaction_id in range(1, num_transactions + 1):
        portfolio_id = random.choice(portfolios['Portfolio_ID'])
        asset_id = random.choice(assets['Asset_ID'])
        transaction_amount = random.uniform(1000, 50000)
        transaction_price = random.uniform(50, 500)
        transactions.append({
            "Transaction_ID": transaction_id,
            "Portfolio_ID": portfolio_id,
            "Asset_ID": asset_id,
            "Transaction_Type": random.choice(['Buy', 'Sell']),
            "Transaction_Date": fake.date_this_year(),
            "Transaction_Amount": transaction_amount,
            "Units": round(transaction_amount / transaction_price, 2),
            "Transaction_Price": round(transaction_price, 2),
            "Total_Transaction_Value": round(transaction_amount, 2),
            "Transaction_Fees": round(random.uniform(1, 100), 2)
        })
    return pd.DataFrame(transactions)

# Generate Performance Metrics for Assets within Portfolios
def generate_performance_metrics(assets, portfolios, num_metrics):
    metrics = []
    for metric_id in range(1, num_metrics + 1):
        asset_id = random.choice(assets['Asset_ID'])
        portfolio_id = random.choice(portfolios['Portfolio_ID'])
        metrics.append({
            "Performance_ID": metric_id,
            "Asset_ID": asset_id,
            "Portfolio_ID": portfolio_id,
            "Time_Period": random.choice(["1M", "3M", "6M", "1Y", "5Y"]),
            "Return_Percentage": round(random.uniform(-10, 20), 2),
            "Price_Change": round(random.uniform(-5, 10), 2),
            "Risk_Adjusted_Return": round(random.uniform(0, 15), 2),
            "Benchmark_Performance": round(random.uniform(-5, 10), 2),
            "Dividend_Payouts": round(random.uniform(0, 5), 2)
        })
    return pd.DataFrame(metrics)

# Generate Market Data and Trends for each Asset
def generate_market_data(assets, num_records):
    market_data = []
    for data_id in range(1, num_records + 1):
        asset_id = random.choice(assets['Asset_ID'])
        open_price = round(random.uniform(50, 500), 2)
        close_price = round(open_price * random.uniform(0.9, 1.1), 2)
        high_price = round(max(open_price, close_price) * random.uniform(1.0, 1.1), 2)
        low_price = round(min(open_price, close_price) * random.uniform(0.9, 1.0), 2)
        market_data.append({
            "Market_Data_ID": data_id,
            "Asset_ID": asset_id,
            "Date": fake.date_this_year(),
            "Open_Price": open_price,
            "Close_Price": close_price,
            "High_Price": high_price,
            "Low_Price": low_price,
            "Trading_Volume": random.randint(100000, 1000000),
            "News_Sentiment_Score": round(random.uniform(-1, 1), 2),
            "Social_Media_Sentiment_Score": round(random.uniform(-1, 1), 2)
        })
    return pd.DataFrame(market_data)

# Generate User Behavior and Preferences
def generate_user_behavior_preferences(users):
    behavior_preferences = []
    for user_id in users['User_ID']:
        behavior_preferences.append({
            "User_ID": user_id,
            "Preferred_Asset_Types": ["Stocks", "Bonds", "Real Estate", "Commodities"][random.randint(0, 3)],
            "Historical_Investment_Choices": random.choice(["Tech", "Energy", "Healthcare", "Finance"]),
            "Sector_Preferences": random.choice(["Technology", "Renewable Energy", "Healthcare", "Finance"]),
            "Sentiment_Sensitivity": random.choice(["High", "Medium", "Low"]),
            "Content_Consumption_Habits": ["Articles", "Videos", "Podcasts", "Newsletters"][random.randint(0, 3)],
            "Learning_Preferences": random.choice(["Visual", "Interactive", "Text-Based"])
        })
    return pd.DataFrame(behavior_preferences)

# Generate Investment Recommendations
def generate_investment_recommendations(users, portfolios, assets, num_recommendations):
    recommendations = []
    for recommendation_id in range(1, num_recommendations + 1):
        user_id = random.choice(users['User_ID'])
        portfolio_id = random.choice(portfolios['Portfolio_ID'])
        asset_id = random.choice(assets['Asset_ID'])
        recommendations.append({
            "Recommendation_ID": recommendation_id,
            "User_ID": user_id,
            "Portfolio_ID": portfolio_id,
            "Asset_ID": asset_id,
            "Recommendation_Date": fake.date_this_year(),
            "Reason": random.choice(["Strong growth potential", "High ESG score", "Low risk", "Sector performance"]),
            "Expected_Return": round(random.uniform(2, 10), 2),
            "Risk_Level": random.choice(["Low", "Moderate", "High"]),
            "Ethical_Alignment": random.choice(["Environmental", "Social", "Governance"]),
            "Investment_Horizon": random.choice(["1 year", "3 years", "5 years"])
        })
    return pd.DataFrame(recommendations)

# Generate Dashboard Layout
def generate_dashboard_layout(users):
    dashboard_layouts = []
    for user_id in users['User_ID']:
        dashboard_layouts.append({
            "Layout_ID": fake.uuid4(),
            "User_ID": user_id,
            "Section_Order": ["Portfolio Overview", "Performance Metrics", "Market Data", "Recommendations"][random.randint(0, 3)],
            "Most_Used_Sections": ["Portfolio Overview", "Performance Metrics"],
            "User_Customization": {"
