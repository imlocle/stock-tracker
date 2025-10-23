"use client";

import { STOCKS } from "@utils/stocks";
import { motion, AnimatePresence } from "framer-motion";
import Link from "next/link";
import "@styles/StockCard.css"

const StockCard = () => {
    return (
      <div className="stock-card-container">
        <AnimatePresence>
          {STOCKS.map((stock) => (
            <Link key={stock.symbol} href={`/stock/${stock.symbol}`}>
              <motion.div
                className="stock-card"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                whileHover={{ scale: 1.05, boxShadow: "0px 10px 20px rgba(0,0,0,0.15)" }}
                exit={{ opacity: 0 }}
              >
                <img
                  src={`/logos/${stock.symbol.toLowerCase()}.png`}
                  alt={`${stock.symbol} logo`}
                  style={{ width: 60, height: 60, objectFit: "contain", marginBottom: 8 }}
                />
                <h2 style={{ fontSize: "1.2rem", fontWeight: 600 }}>{stock.symbol}</h2>
              </motion.div>
            </Link>
          ))}
        </AnimatePresence>
      </div>
    )
}

export default StockCard;