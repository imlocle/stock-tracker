"use client";

import { useEffect, useState } from "react";
import { getTimeSeriesDaily, ITimeSeriesDaily } from "@utils/api";
import { IPrice } from "@models/interfaces";
import { motion } from "framer-motion";
import "@styles/TimeSeriesChart.css"

export default function TimeSeriesChart({ symbol }: { symbol: string }) {
  const [tableHeaders, setTableHeaders] = useState<string[]>([])

  const [historicalPrices, setHistoricalPrices] = useState<IPrice[]>([]);
  const [loading, setLoading] = useState(true);
  const [timeSeriesMessage, setTimeSeriesMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const tableHeaders = ["Date", "Close Price", "Volume", "% Change"];
        const response = await getTimeSeriesDaily(symbol);

        if (response.data && Object.keys(response.data).length > 0) {
          const entries = Object.entries(response.data) as [string, ITimeSeriesDaily][];
          const prices: IPrice[] = entries.map(([date, data], index) => {
            const prevClose =
              index < entries.length - 1
                ? parseFloat(entries[index + 1][1]["4. close"])
                : parseFloat(data["4. close"]);

            const close = parseFloat(data["4. close"]);
            const volume = parseInt(data["5. volume"], 10);
            const percentChange = ((close - prevClose) / prevClose) * 100;
            return { date, close, volume, percentChange };
          });

          setTableHeaders(tableHeaders)
          setHistoricalPrices(prices);
        } else if (response.message) {
          setTimeSeriesMessage(response.message);
        } else {
          setTimeSeriesMessage("No historical data available.");
        }
      } catch (err: any) {
        console.warn("Time series fetch error:", err);
        setError("Failed to load time series data");
        setHistoricalPrices([]);
        setTableHeaders([])
        setTimeSeriesMessage(err?.message || "Time series data unavailable.");
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [symbol]);

   if (error) return <p style={{ color: "red" }}>{error}</p>;

   

  return (
    <div className="time-series-container">
      <h2>Historical Stock Prices:</h2>
      
      {timeSeriesMessage && (
        <p style={{ color: "orange", marginBottom: "1rem" }}>{timeSeriesMessage}</p>
      )}

      {historicalPrices.length > 0 ? (
              <div style={{ overflowX: "auto" }}>
                <table style={{ width: "100%", borderCollapse: "collapse", borderRadius: 12, overflow: "hidden" }}>
                  <thead>
                    <tr style={{ background: "#f3f4f6" }}>
                      {tableHeaders.map((h) => (
                         <th key={h} className="chart-table-header ">{h}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {historicalPrices.map((item) => (
                      <motion.tr
                        key={item.date}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ duration: 0.2 }}
                        whileHover={{ backgroundColor: "rgba(0,0,0,0.05)" }}
                      >
                        <td className="chart-table-row">{item.date}</td>
                        <td className="chart-table-row">$ {item.close.toFixed(2)}</td>
                        <td className="chart-table-row">{item.volume.toLocaleString()}</td>
                        <td className="chart-table-row">{item.percentChange.toFixed(2)}%</td>
                      </motion.tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <p>No historical price data available.</p>
            )}
    </div>
  );
}
