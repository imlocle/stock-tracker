// Price type for historical data
export interface IPrice {
  date: string;
  close: number;
  volume: number;
  percentChange: number;
}