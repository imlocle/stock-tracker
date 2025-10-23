"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";

import { getCompanyOverview, ICompanyOverview, ICompanyOverviewResponse } from "@lib/api";
import CompanyOverviewCard from "@components/CompanyOverviewCard";
import TimeSeriesChart from "@components/TimeSeriesChart";
import LoadingCircle from "@components/LoadingCircle";

export default function StockDetailsPage() {
  const { symbol } = useParams() as { symbol: string };
  const router = useRouter();

  const [company, setCompany] = useState<ICompanyOverview | null>(null);
  const [loadingCompany, setLoadingCompany] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCompany() {
      if (!symbol) return;

      setLoadingCompany(true);
      setError(null);

      try {
        const response: ICompanyOverviewResponse = await getCompanyOverview(symbol);
        if (response.data) setCompany(response.data);
        if (response.message) console.warn("Company API message:", response.message);
      } catch (err: any) {
        console.error(err);
        setError(err?.message || "Failed to fetch company overview.");
      } finally {
        setLoadingCompany(false);
      }
    }

    fetchCompany();
  }, [symbol]);

  if (loadingCompany) {
    return (
      <LoadingCircle />
    );
  }

  if (error) {
    return <p style={{ color: "red", textAlign: "center", marginTop: 32 }}>{error}</p>;
  }

  if (!company) return <p>No company data available.</p>;

  return (
    <div className="container">
      <button
        onClick={() => router.push("/")}
        style={{
          background: "none",
          border: "none",
          color: "#0070f3",
          cursor: "pointer",
          fontSize: "1rem",
          display: "flex",
          alignItems: "center",
          gap: "0.5rem",
        }}
      >
        ← Back to Home
      </button>
      <CompanyOverviewCard company={company} />
      <TimeSeriesChart symbol={symbol} />
    </div>
  );
}
