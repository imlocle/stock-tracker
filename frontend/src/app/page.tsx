"use client"; // required for hooks + motion

import Link from "next/link";
import { STOCKS } from "@lib/stocks";
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function HomePage() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 500); // simulate load
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return (
      <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh" }}>
        <motion.div
          style={{
            width: 64,
            height: 64,
            border: "5px solid #ccc",
            borderTopColor: "#0070f3",
            borderRadius: "50%",
          }}
          animate={{ rotate: 360 }}
          transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
        />
      </div>
    );
  }

  return (
    <div style={{ padding: "2rem", maxWidth: 1200, margin: "0 auto" }}>
      <h1 style={{ fontSize: "3rem", fontWeight: "bold", textAlign: "center", marginBottom: "2rem" }}>
        Stock Summaries
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(180px, 1fr))",
          gap: "1rem",
        }}
      >
        <AnimatePresence>
          {STOCKS.map((stock) => (
            <Link key={stock.symbol} href={`/stock/${stock.symbol}`}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                whileHover={{ scale: 1.05, boxShadow: "0px 10px 20px rgba(0,0,0,0.15)" }}
                exit={{ opacity: 0 }}
                style={{
                  background: "#fff",
                  padding: "1rem",
                  borderRadius: "12px",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  cursor: "pointer",
                  transition: "box-shadow 0.3s",
                }}
              >
                <img
                  src={`https://logo.clearbit.com/${stock.domain}`}
                  alt={`${stock.symbol} logo`}
                  style={{ width: 60, height: 60, objectFit: "contain", marginBottom: 8 }}
                />
                <h2 style={{ fontSize: "1.2rem", fontWeight: 600 }}>{stock.symbol}</h2>
              </motion.div>
            </Link>
          ))}
        </AnimatePresence>
      </div>
    </div>
  );
}
