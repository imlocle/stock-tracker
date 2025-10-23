"use client"; // required for hooks + motion

import { useState, useEffect } from "react";
import Title from "@components/Title";
import StockCard from "@components/StockCard";
import LoadingCircle from "@components/LoadingCircle";
import Link from "next/link";

const HomePage = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 500); // simulate load
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return (
        <LoadingCircle />
    );
  }

  return (
    <div className="container">
      <Title title="Stock Tracker"/>
      <p>Stock Tracker is a full-stack web application that provides real-time and historical stock market data using the Alpha Vantage API. It features a FastAPI backend and a Next.js (React) frontend, designed for speed, scalability, and a clean developer experience.</p>
      <p>Documentation: <Link href="https://www.alphavantage.co/">Alpha Vantage API</Link></p>
      <StockCard />
    </div>
  );
}

export default HomePage;
