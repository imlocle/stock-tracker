export interface StockInfo {
  symbol: string;
  domain: string;
}



export const STOCKS: StockInfo[] = [
  { symbol: "AAPL", domain: "apple.com" },
  { symbol: "ADBE", domain: "adobe.com" },
  { symbol: "AMZN", domain: "amazon.com" },
  { symbol: "CRM", domain: "salesforce.com" },
  { symbol: "CSCO", domain: "cisco.com" },
  { symbol: "GOOGL", domain: "abc.xyz" },
  { symbol: "INTC", domain: "intel.com" },
  { symbol: "META", domain: "meta.com" },
  { symbol: "MSFT", domain: "microsoft.com" },
  { symbol: "NFLX", domain: "netflix.com" },
  { symbol: "NVDA", domain: "nvidia.com" },
  { symbol: "ORCL", domain: "oracle.com" },
  { symbol: "PYPL", domain: "paypal.com" },
  { symbol: "TSLA", domain: "tesla.com" },
  { symbol: "UBER", domain: "uber.com" },
];