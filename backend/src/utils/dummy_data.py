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
    "META": {
        "Symbol": "META",
        "AssetType": "Common Stock",
        "Name": "Meta Platforms Inc.",
        "Description": "Meta Platforms, Inc. is a leading technology firm based in Menlo Park, California, renowned for transforming social connectivity through its flagship platforms, including Facebook, Instagram, and WhatsApp. Pioneering developments in virtual and augmented reality via its Reality Labs division, Meta is at the forefront of the metaverse, exploring innovative consumer engagement avenues. By significantly investing in immersive technologies, the company not only attracts a large, diverse user base but also enhances its advertising revenue, thereby reinforcing its position as a dominant force in the rapidly evolving digital landscape.",
        "Exchange": "NASDAQ",
        "Sector": "Communication Services",
        "Industry": "Interactive Media & Services",
        "MarketCapitalization": "1842429690000",
    },
    "NVDA": {
        "Symbol": "NVDA",
        "AssetType": "Common Stock",
        "Name": "NVIDIA Corporation",
        "Description": "NVIDIA Corporation is a prominent American multinational technology firm based in Santa Clara, California, recognized for its leadership in the design and manufacturing of advanced graphics processing units (GPUs) for gaming and professional markets. The company is at the cutting edge of AI and visual computing technologies, developing critical solutions such as System on a Chip (SoC) products that enhance mobile computing and automotive applications, particularly in the expanding field of autonomous driving. With a diverse portfolio that encompasses gaming, data centers, and AI infrastructure, NVIDIA is committed to delivering innovative products and services that meet the demands of a dynamic technology landscape.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Semiconductors",
        "MarketCapitalization": "4389277270000",
    },
    "NFLX": {
        "Symbol": "NFLX",
        "AssetType": "Common Stock",
        "Name": "Netflix Inc",
        "Description": "Netflix, Inc. is a premier American over-the-top content platform and production company, headquartered in Los Gatos, California. Since its inception in 1997, Netflix has transformed the entertainment landscape with its subscription-based streaming service, offering an expansive library of films and television series, including a diverse array of critically acclaimed original programming. As a trailblazer in the streaming industry, Netflix is strategically expanding its global footprint, employing innovative distribution methods and investing heavily in original content to enhance viewer engagement and drive subscriber growth. With a steadfast commitment to shaping the future of media consumption, Netflix continues to lead the way in the digital entertainment revolution.",
        "Exchange": "NASDAQ",
        "Sector": "Communication Services",
        "Industry": "Entertainment",
        "MarketCapitalization": "474374996000",
    },
    "ADBE": {
        "Symbol": "ADBE",
        "AssetType": "Common Stock",
        "Name": "Adobe Systems Incorporated",
        "Description": "Adobe Inc. is a premier American multinational software company based in San Jose, California, recognized for its innovative leadership in digital media and marketing solutions. With flagship products like Adobe Photoshop, Illustrator, and Acrobat, it has become an essential partner for creative professionals across diverse industries. The company has further expanded its portfolio through Adobe Experience Cloud, a comprehensive suite that enhances customer engagement and marketing strategies for businesses. By harnessing the power of artificial intelligence and cloud technologies, Adobe is well-positioned to sustain its competitive advantage and address the evolving demands of the digital landscape, boasting a vast global user base.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Software - Application",
        "MarketCapitalization": "148222067000",
    },
    "ORCL": {
        "Symbol": "ORCL",
        "AssetType": "Common Stock",
        "Name": "Oracle Corporation",
        "Description": "Oracle Corporation is a leading multinational technology company based in Austin, Texas, specializing in a broad range of software products and cloud computing solutions. As a dominant force in the cloud infrastructure sector, Oracle is committed to driving digital transformation for enterprises by leveraging cutting-edge technologies, including artificial intelligence and machine learning. The company maintains a robust focus on research and development, consistently updating its portfolio to meet the evolving needs of global businesses, thereby solidifying its reputation for innovation and excellence in the technology space.",
        "Exchange": "NYSE",
        "Sector": "Technology",
        "Industry": "Software - Infrastructure",
        "MarketCapitalization": "822948987000",
    },
    "INTC": {
        "Symbol": "INTC",
        "AssetType": "Common Stock",
        "Name": "Intel Corporation",
        "Description": "Intel Corporation, headquartered in Santa Clara, California, is a preeminent player in the global semiconductor industry, known as the world's largest chip manufacturer by revenue. The company revolutionized personal computing with its x86 microprocessors, which dominate the market. In response to shifting industry demands, Intel is strategically evolving its offerings to emphasize data-centric technologies, artificial intelligence, and cloud solutions, positioning itself at the forefront of the next generation of computing. With a robust emphasis on innovation and a commitment to extensive R&D, Intel continues to enhance its competitive advantage in an increasingly interconnected world.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Semiconductors",
        "MarketCapitalization": "175636480000",
    },
    "CSCO": {
        "Symbol": "CSCO",
        "AssetType": "Common Stock",
        "Name": "Cisco Systems Inc.",
        "Description": "Cisco Systems, Inc. is a premier technology conglomerate headquartered in San Jose, California, renowned for its extensive portfolio of networking hardware, software, and telecommunications solutions. As a leader in the rapidly evolving sectors of the Internet of Things (IoT) and cybersecurity, Cisco's innovations, including its Webex communications platform, exemplify its commitment to enhancing connectivity and secure data exchange. The company leverages strategic acquisitions and research to maintain its competitive edge in the global technology market, solidifying its status as a crucial actor in shaping the future of digital transformation and network security.",
        "Exchange": "NASDAQ",
        "Sector": "Technology",
        "Industry": "Communication Equipment",
        "MarketCapitalization": "279332913000",
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
        "Name": "Salesforce.com Inc",
        "Description": "Salesforce.com, Inc. (CRM) is a preeminent cloud-based software provider headquartered in San Francisco, California, specializing in Customer Relationship Management (CRM) solutions that drive digital transformation across diverse industries. The company's extensive suite of enterprise applications enhances customer service, marketing automation, analytics, and app development, enabling businesses to forge strong customer relationships and achieve sustainable growth. Utilizing advanced technologies such as artificial intelligence and data analytics, Salesforce remains at the forefront of innovation in the cloud computing sector. Through strategic acquisitions and continuous enhancements to its platform, Salesforce solidifies its position as a leading force in shaping the future of enterprise software.",
        "Exchange": "NYSE",
        "Sector": "Technology",
        "Industry": "Software - Application",
        "MarketCapitalization": "244321288000",
    },
    "UBER": {
        "Symbol": "UBER",
        "AssetType": "Common Stock",
        "Name": "Uber Technologies Inc",
        "Description": "Uber Technologies, Inc. is a prominent American technology firm redefining the landscape of transportation and logistics through its innovative digital solutions. Founded in San Francisco, the company operates a multifaceted platform encompassing ride-hailing, food delivery via Uber Eats, and freight transportation services. By strategically expanding into urban mobility with electric bicycle and scooter rentals, Uber is pioneering sustainable transportation initiatives. Leveraging advanced technology, Uber not only enhances user experience but also drives operational efficiency, solidifying its role as a leader in the evolving global mobility ecosystem.",
        "Exchange": "NYSE",
        "Sector": "Software - Application",
        "Industry": "Information Technology Services",
        "MarketCapitalization": "194006499000",
    },
}


def get_dummy_time_series_data():
    dummy_data = {}
    today = datetime.today()
    price = 100.0
    for i in range(30):
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
