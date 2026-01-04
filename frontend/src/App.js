import React from "react";
import Plot from "react-plotly.js";

function App() {
  return (
    <div>
      <h1>Air Quality Visualization</h1>
      <h1>PM2.5 & PM10 Levels by Date in Istanbul (2024)</h1>

      <Plot
        data={[
          {
            x: ["2024-01-04", "2024-09-03"],
            y: [30, 115],
            type: "scatter",
            mode: "lines+markers",
            name: "PM2.5",
          },
          {
            x: ["2024-01-04", "2024-09-03"],
            y: [60, 85],
            type: "scatter",
            mode: "lines+markers",
            name: "PM10",
          },
        ]}
        layout={{
          title: "PM2.5 & PM10 Levels by Date in Istanbul (2024)",
          xaxis:{title:"Dates"},
          yaxis:{title:"Values"},
        }
      
        }
      />
    </div>
  );
}

export default App;
