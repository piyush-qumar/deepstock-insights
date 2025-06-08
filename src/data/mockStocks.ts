export type StockPrediction =  "bullish" | "bearish" | "neutral";

export interface Stock  {
  symbol: string;
  name: string;
  price: number;
  change: number;
  prediction: StockPrediction;
};
export const mockStocks: Stock[] = [
  {
    symbol: "AAPL",
    name: "Apple Inc.",
    price: 175.64,
    change: 1.23,
    prediction: "bullish",
  },
  {
    symbol: "GOOGL",
    name: "Alphabet Inc.",
    price: 2800.12,
    change: -15.67,
    prediction: "bearish",
  },
  {
    symbol: "AMZN",
    name: "Amazon.com Inc.",
    price: 3400.50,
    change: 10.45,
    prediction: "bullish",
  },
  {
    symbol: "MSFT",
    name: "Microsoft Corporation",
    price: 299.99,
    change: -2.34,
    prediction: "neutral",
  },
];