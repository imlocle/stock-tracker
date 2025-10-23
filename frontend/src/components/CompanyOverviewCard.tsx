"use client";

import { ICompanyOverview } from "@lib/api";
import Title from "./Title";
import "@styles/CompanyOverviewCard.css"

interface Props {
  company: ICompanyOverview;
}

export default function CompanyOverviewCard({ company }: Props) {
  const logoUrl = `/logos/${company.Symbol.toLowerCase()}.png`

  return (
    <div className="company-overview-container">
    <Title title={company.Name}/>
      <div className="subtitle">
        <img src={logoUrl} alt={company.Symbol} />
        <h1>{company.Symbol}</h1>
      </div>
      <p style={{ marginBottom: "1rem" }}>{company.Description || "N/A"}</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))", gap: 16 }}>
        <div><strong>Asset Type:</strong> {company.AssetType || "N/A"}</div>
        <div><strong>Exchange:</strong> {company.Exchange || "N/A"}</div>
        <div><strong>Sector:</strong> {company.Sector || "N/A"}</div>
        <div><strong>Industry:</strong> {company.Industry || "N/A"}</div>
        <div><strong>Market Cap:</strong> {company.MarketCapitalization || "N/A"}</div>
      </div>
    </div>
  );
}
