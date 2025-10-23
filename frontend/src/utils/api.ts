export interface ICompanyOverviewResponse {
  data: ICompanyOverview;
  message?: string | null;
}

export interface ICompanyOverview {
  Symbol: string;
  Name: string;
  AssetType: string;
  Description: string;
  Exchange: string;
  Sector: string;
  Industry: string;
  MarketCapitalization: string;
}

export interface ITimeSeriesDailyResponse {
  data: Record<string, ITimeSeriesDaily>;
  message?: string | null;
}

export interface ITimeSeriesDaily {
  "1. open": string;
  "2. high": string;
  "3. low": string;
  "4. close": string;
  "5. volume": string;
  [key: string]: string;
}

export async function getCompanyOverview(symbol: string): Promise<ICompanyOverviewResponse> {
  const res = await fetch(`http://localhost:8000/api/company-overview?symbol=${symbol}`);
  if (!res.ok) {
    return { data: {
      Symbol: symbol,
      Name: symbol,
      AssetType: "NA",
      Description: "Thank you for using Alpha Vantage! This is a premium endpoint. You may subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly unlock all premium endpoints",
      Exchange: "NA",
      Sector: "NA",
      Industry: "NA",
      MarketCapitalization: "NA"
    }, message: `Failed: ${symbol}: API rate limit reached. Please try again later` };
  }
  return res.json();
}

export async function getTimeSeriesDaily(symbol: string): Promise<ITimeSeriesDailyResponse> {
  const res = await fetch(`http://localhost:8000/api/time-series-daily?symbol=${symbol}`);
  if (!res.ok) {
    return {
      data: {},
      message: `Failed to fetch time series data for ${symbol}`,
    };
  }
  return res.json();
}

