from datetime import datetime, timedelta
import random

DUMMY_DATA = {
    "AMZN": {
        "Symbol": "AMZN",
        "AssetType": "Common Stock",
        "Name": "Amazon.com Inc",
        "Description": "Amazon.com, Inc. is a leading American multinational technology company, widely recognized for its dominance in e-commerce, cloud computing via Amazon Web Services (AWS), and digital streaming. As a key player among the \"Big Five\" tech giants, Amazon's innovative approach and unwavering commitment to customer-centric solutions have established it as one of the world's most valuable brands. The company remains at the forefront of technological advancement, with strategic investments in artificial intelligence and logistics, positioning itself to leverage emerging market trends and further enhance its competitive edge in the rapidly evolving digital landscape.",
        "Exchange": "NASDAQ",
        "Sector": "Consumer Cyclical",
        "Industry": "Internet Retail",
        "MarketCapitalization": "2367930499000",
    },
    "AAPL": {
        "Symbol": "AAPL",
        "AssetType": "Common Stock",
        "Name": "Apple Inc",
        "Description": 'Apple Inc. is a leading American multinational technology company that specializes in innovative consumer electronics, software, and online services. With a record revenue of $274.5 billion in 2020, it holds the title of the world\'s most valuable publicly traded company and is a dominant force in the global technology landscape. Its flagship products, such as the iPhone, iPad, and Mac, have cemented its reputation as a trailblazer in the sector, positioning it as the fourth-largest PC vendor and smartphone manufacturer worldwide. As a cornerstone of the "Big Five" technology companies, Apple continues to set industry standards and drive advancements in technology and consumer engagement.',
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Consumer Electronics",
        "MarketCapitalization": "3899609055000",
    },
    "MSFT": {
        "Symbol": "MSFT",
        "AssetType": "Common Stock",
        "Name": "Microsoft Corporation",
        "Description": "Microsoft Corporation is a preeminent American multinational technology company renowned for its extensive product portfolio that includes operating systems, productivity software, and hardware solutions. Best known for its Microsoft Windows OS and the Microsoft Office suite, the company has also established a significant presence in the gaming industry with its Xbox platform and in the hardware market with the Surface series. Demonstrating strong leadership in digital transformation, Microsoft leverages cloud computing services, particularly through its Azure platform, to enhance productivity and drive innovation across numerous sectors. Its robust market position and commitment to research and development underscore its pivotal role in shaping the future of technology globally.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Software - Infrastructure",
        "MarketCapitalization": "3847852655000",
    },
    "GOOGL": {
        "Symbol": "GOOGL",
        "AssetType": "Common Stock",
        "Name": "Alphabet Inc Class A",
        "Description": "Alphabet Inc. (GOOGL) is a leading American multinational conglomerate based in Mountain View, California, established as the parent company of Google and its subsidiaries following a strategic restructuring in October 2015. As one of the world's largest technology companies by revenue, it operates in diverse segments including online advertising, cloud computing, consumer electronics, and artificial intelligence. Co-founders Larry Page and Sergey Brin continue to influence the company's strategic direction as controlling shareholders and board members. With a robust portfolio and a commitment to innovation, Alphabet remains at the forefront of tech advancements, driving significant market value and growth potential for institutional investors.",
        "Exchange": "NASDAQ",
        "Sector": "Communication Services",
        "Industry": "Interactive Media & Services",
        "MarketCapitalization": "2993288380000",
    },
    "TSLA": {
        "Symbol": "TSLA",
        "AssetType": "Common Stock",
        "Name": "Tesla Inc",
        "Description": "Tesla, Inc. is a leading American electric vehicle and clean energy company headquartered in Palo Alto, California. With a diverse product portfolio that includes electric cars, battery energy storage solutions, and solar energy products, Tesla is at the forefront of sustainable transportation and energy innovation. In 2020, Tesla captured a significant share of the global market, achieving a 16% share in the plug-in vehicle segment and 23% in the battery-electric vehicle segment, solidifying its position as the largest seller of electric vehicles. Additionally, through its subsidiary Tesla Energy, the company is a key player in the solar and battery storage market, making substantial contributions to the renewable energy landscape. As it continues to scale production and expand its product offerings, Tesla remains poised for long-term growth and leadership in the transition to a more sustainable future.",
        "Exchange": "NASDAQ",
        "Sector": "Consumer Cyclical",
        "Industry": "Auto Manufacturers",
        "MarketCapitalization": "1471711805000",
    },
    "FB": {
        "Symbol": "FB",
        "AssetType": "Common Stock",
        "Name": "Meta Platforms, Inc.",
        "Description": "Meta Platforms, formerly Facebook, focuses on social media, digital advertising, and virtual reality products.",
        "Exchange": "NASDAQ",
        "Sector": "Communication Services",
        "Industry": "Interactive Media & Services",
        "MarketCapitalization": "800000000000",
    },
    "NVDA": {
        "Symbol": "NVDA",
        "AssetType": "Common Stock",
        "Name": "NVIDIA Corporation",
        "Description": "NVIDIA is a technology company known for GPUs and AI hardware, serving gaming, data center, and AI markets.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Semiconductors",
        "MarketCapitalization": "1000000000000",
    },
    "NFLX": {
        "Symbol": "NFLX",
        "AssetType": "Common Stock",
        "Name": "Netflix, Inc.",
        "Description": "Netflix is a global streaming service offering TV shows, movies, and original content to subscribers worldwide.",
        "Exchange": "NASDAQ",
        "Sector": "Communication Services",
        "Industry": "Movies & Entertainment",
        "MarketCapitalization": "250000000000",
    },
    "ADBE": {
        "Symbol": "ADBE",
        "AssetType": "Common Stock",
        "Name": "Adobe Inc.",
        "Description": "Adobe is a software company known for creative and multimedia software like Photoshop, Illustrator, and Acrobat.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Software - Application",
        "MarketCapitalization": "300000000000",
    },
    "ORCL": {
        "Symbol": "ORCL",
        "AssetType": "Common Stock",
        "Name": "Oracle Corporation",
        "Description": "Oracle is a technology company providing database software, cloud services, and enterprise software products.",
        "Exchange": "NYSE",
        "Sector": "Technology",
        "Industry": "Information Technology Services",
        "MarketCapitalization": "300000000000",
    },
    "INTC": {
        "Symbol": "INTC",
        "AssetType": "Common Stock",
        "Name": "Intel Corporation",
        "Description": "Intel designs and manufactures microprocessors and semiconductor components for computers and devices.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Semiconductors",
        "MarketCapitalization": "200000000000",
    },
    "CSCO": {
        "Symbol": "CSCO",
        "AssetType": "Common Stock",
        "Name": "Cisco Systems, Inc.",
        "Description": "Cisco designs and sells networking hardware, software, and telecommunications equipment worldwide.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Information Technology Services",
        "MarketCapitalization": "200000000000",
    },
    "PYPL": {
        "Symbol": "PYPL",
        "AssetType": "Common Stock",
        "Name": "PayPal Holdings, Inc.",
        "Description": "PayPal Holdings, Inc. is a prominent global technology platform that revolutionizes digital and mobile payments for consumers and merchants worldwide. Renowned for its innovative online payment systems, the company delivers a secure and seamless transaction experience, catering to millions and providing services from peer-to-peer transfers to sophisticated e-commerce payment processing solutions. Leveraging its extensive network, PayPal is well-positioned to capitalize on the growing demand for fintech solutions, continually enhancing its offerings with a strong emphasis on security and innovation, thereby reinforcing its status as a key player in the financial technology sector.",
        "Exchange": "NASDAQ",
        "Sector": "Financial Services",
        "Industry": "Credit Services",
        "MarketCapitalization": "66924261000",
    },
    "CRM": {
        "Symbol": "CRM",
        "AssetType": "Common Stock",
        "Name": "Salesforce, Inc.",
        "Description": "Salesforce is a cloud-based software company specializing in customer relationship management (CRM) solutions.",
        "Exchange": "NYSE",
        "Sector": "Technology",
        "Industry": "Information Technology Services",
        "MarketCapitalization": "200000000000",
    },
    "UBER": {
        "Symbol": "UBER",
        "AssetType": "Common Stock",
        "Name": "Uber Technologies, Inc.",
        "Description": "Uber is a ride-hailing and transportation network company providing services like rides, delivery, and freight.",
        "Exchange": "NYSE",
        "Sector": "Industrials",
        "Industry": "Information Technology Services",
        "MarketCapitalization": "100000000000",
    },
}


def get_dummy_time_series_data():
    dummy_data = {}
    today = datetime.today()
    price = 100.0
    for i in range(7):
        day = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        open_price = round(price + random.uniform(-1, 1), 2)
        close_price = round(open_price + random.uniform(-1, 1), 2)
        high_price = max(open_price, close_price) + round(random.uniform(0, 1), 2)
        low_price = min(open_price, close_price) - round(random.uniform(0, 1), 2)
        volume = random.randint(100000, 500000)
        dummy_data[day] = {
            "1. open": str(open_price),
            "2. high": str(high_price),
            "3. low": str(low_price),
            "4. close": str(close_price),
            "5. volume": str(volume),
        }
        price = close_price  # Next day base
    return dummy_data
