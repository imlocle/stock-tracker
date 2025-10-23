"use client";

import { motion } from "framer-motion";

const LoadingCircle = () => {
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

export default LoadingCircle;