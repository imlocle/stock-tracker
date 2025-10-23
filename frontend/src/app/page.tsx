"use client"; // required for hooks + motion

import { useState, useEffect } from "react";
import Title from "@components/Title";
import StockCard from "@components/StockCard";
import LoadingCircle from "@components/LoadingCircle";

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
      <StockCard />
    </div>
  );
}

export default HomePage;
