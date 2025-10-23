"use client";

import { useEffect, useState } from "react";
import { getTimeSeriesDaily, ITimeSeriesDaily } from "@utils/api";
import { IPrice } from "@models/interfaces";
import { motion } from "framer-motion";
import "@styles/TimeSeriesChart.css"
import PriceHistoryChart from "./PriceHistoryChart";

export default function TimeSeriesChart({ symbol }: { symbol: string }) {
  
  const [historicalPrices, setHistoricalPrices] = useState<IPrice[]>([]);
  const [timeSeriesMessage, setTimeSeriesMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [currentPage, setCurrentPage] = useState(1);
  const rowsPerPage = 10;
  
  
  useEffect(() => {
    async function fetchData() {
      try {
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
        setTimeSeriesMessage(err?.message || "Time series data unavailable.");
      }
    }

    fetchData();
  }, [symbol]);

   if (error) return <p style={{ color: "red" }}>{error}</p>;

  const tableHeaders = ["Date", "Close Price", "Volume", "% Change"];
  const indexOfLastRow = currentPage * rowsPerPage;
  const indexOfFirstRow = indexOfLastRow - rowsPerPage;
  const currentRows = historicalPrices.slice(indexOfFirstRow, indexOfLastRow);
  const totalPages = Math.ceil(historicalPrices.length / rowsPerPage);

  return (
    <div className="time-series-container">
      <h2>Historical Stock Prices:</h2>
      
      {timeSeriesMessage && (
        <p style={{ color: "orange", marginBottom: "1rem" }}>{timeSeriesMessage}</p>
      )}

      {historicalPrices.length > 0 ? (
        <>
        <PriceHistoryChart data={historicalPrices} />

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
                {currentRows.map((item) => (
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
          <div style={{ display: "flex", justifyContent: "center", marginTop: 16, gap: 8 }}>
            <button
              onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
              disabled={currentPage === 1}
              className="pagination-button"
            >
              Prev
            </button>

            <span>Page {currentPage} of {totalPages}</span>

            <button
              onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
              disabled={currentPage === totalPages}
              className="pagination-button"
            >
              Next
            </button>
          </div>
        </>
            ) : (
              <p>No historical price data available.</p>
            )}
    </div>
  );
}
