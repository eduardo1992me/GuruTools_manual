import React from "react";

import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

const data = [
  { name: "Enero", 2022: 100, 2023: 600 },
  { name: "Febrero", 2022: 270, 2023: 780 },
  { name: "Marzo", 2022: 300, 2023: 810 },
  { name: "Abril", 2022: 250, 2023: 700 },
  { name: "Mayo", 2022: 210, 2023: 550 },
  { name: "Junio", 2022: 210, 2023: 550 },
  { name: "Julio", 2022: 212, 2023: 550 },
];

function MDChartsBars() {
  return (
    <ResponsiveContainer width="100%" aspect={3}>
      <BarChart
        data={data}
        width={500}
        height={300}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="4 1 2" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip/>
        <Legend />
        <Bar dataKey="2022" fill="#00b894" />
        <Bar dataKey="2023" fill="#0984e3" />
        
      </BarChart>
    </ResponsiveContainer>
  );
}

export default MDChartsBars;
