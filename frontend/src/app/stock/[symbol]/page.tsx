"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { getCompanyOverview, getTimeSeriesDaily } from "@lib/api";

// Types
interface Company {
  Symbol: string;
  Name: string;
  Description: string;
  AssetType: string;
  Exchange: string;
  Sector: string;
  Industry: string;
  MarketCapitalization: string;
}

interface Price {
  date: string;
  close: number;
  volume: number;
  percentChange: number;
}

export default function StockDetailsPage() {
  const { symbol } = useParams() as { symbol: string };
  const [loading, setLoading] = useState(true);
  const [company, setCompany] = useState<Company | null>(null);
  const [historicalPrices, setHistoricalPrices] = useState<Price[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      if (!symbol) {
        setError("Symbol not found");
        setLoading(false);
        return;
      }

      try {
        setLoading(true);
        setError(null);

        // Fetch company overview
        const comp = await getCompanyOverview(symbol);
        if ("message" in comp && comp.message) {
          setError(comp.message);
        } else {
          setCompany(comp as Company);
        }

        // Fetch time series
        const ts = await getTimeSeriesDaily(symbol);
        if ("message" in ts && ts.message) {
          setError(ts.message);
          setHistoricalPrices([]); // return empty array to prevent crash
        } else {
          const tsData = (ts as any)["Time Series (Daily)"] as Record<
            string,
            Record<string, string>
          >;

          const entries = Object.entries(tsData);

          const prices: Price[] = entries.map(([date, data], index) => {
            const prevClose =
              index < entries.length - 1
                ? parseFloat(entries[index + 1][1]["4. close"])
                : parseFloat(data["4. close"]);
            const close = parseFloat(data["4. close"]);
            const volume = parseInt(data["5. volume"]);
            const percentChange = ((close - prevClose) / prevClose) * 100;
            return { date, close, volume, percentChange };
          });

          setHistoricalPrices(prices);
        }
      } catch (err: any) {
        setError(err.message || "Failed to fetch data");
        setHistoricalPrices([]);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [symbol]);

  if (loading) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <motion.div
          style={{
            width: 48,
            height: 48,
            border: "4px solid #ccc",
            borderTopColor: "#0070f3",
            borderRadius: "50%",
          }}
          animate={{ rotate: 360 }}
          transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
        />
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ color: "red", textAlign: "center", marginTop: 32 }}>
        {error}
      </div>
    );
  }

  return (
    <div style={{ padding: "2rem", maxWidth: 1200, margin: "0 auto" }}>
      <AnimatePresence>
        {company && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.5 }}
            style={{
              background: "#fff",
              padding: "2rem",
              borderRadius: 16,
              boxShadow: "0px 10px 20px rgba(0,0,0,0.1)",
            }}
          >
            {/* Company Header */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "1rem",
                marginBottom: "1rem",
              }}
            >
              <img
                src={`https://logo.clearbit.com/${company.Symbol.toLowerCase()}.com`}
                alt={company.Symbol}
                style={{ width: 48, height: 48, objectFit: "contain" }}
              />
              <h1 style={{ fontSize: "2rem", fontWeight: 700 }}>
                {company.Name} ({company.Symbol})
              </h1>
            </div>

            {/* Description */}
            <p style={{ marginBottom: "1rem" }}>
              {company.Description || "N/A"}
            </p>

            {/* Company Info */}
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
                gap: 16,
                marginBottom: 24,
              }}
            >
              <div>
                <strong>Asset Type:</strong> {company.AssetType || "N/A"}
              </div>
              <div>
                <strong>Exchange:</strong> {company.Exchange || "N/A"}
              </div>
              <div>
                <strong>Sector:</strong> {company.Sector || "N/A"}
              </div>
              <div>
                <strong>Industry:</strong> {company.Industry || "N/A"}
              </div>
              <div>
                <strong>Market Cap:</strong>{" "}
                {company.MarketCapitalization || "N/A"}
              </div>
            </div>

            {/* Historical Prices Table */}
            <h2
              style={{
                fontSize: "1.5rem",
                fontWeight: 600,
                marginBottom: 8,
              }}
            >
              Historical Prices
            </h2>
            <div style={{ overflowX: "auto" }}>
              <table
                style={{
                  width: "100%",
                  borderCollapse: "collapse",
                  borderRadius: 12,
                  overflow: "hidden",
                }}
              >
                <thead>
                  <tr style={{ background: "#f3f4f6" }}>
                    <th style={{ padding: 8, borderBottom: "1px solid #ddd" }}>
                      Date
                    </th>
                    <th style={{ padding: 8, borderBottom: "1px solid #ddd" }}>
                      Close
                    </th>
                    <th style={{ padding: 8, borderBottom: "1px solid #ddd" }}>
                      Volume
                    </th>
                    <th style={{ padding: 8, borderBottom: "1px solid #ddd" }}>
                      % Change
                    </th>
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
                      <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                        {item.date}
                      </td>
                      <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                        {item.close.toFixed(2)}
                      </td>
                      <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                        {item.volume.toLocaleString()}
                      </td>
                      <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                        {item.percentChange.toFixed(2)}%
                      </td>
                    </motion.tr>
                  ))}
                </tbody>
              </table>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
