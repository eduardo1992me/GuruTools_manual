import React from "react";
import {
  ResponsiveContainer,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  Bar,
} from "recharts";

const data = [
  { name: "8/07/2023", flash: 2400, long: 2400 },
  { name: "9/07/2023", flash: 1398, long: 2210 },
  { name: "10/07/2023", flash: 9800, long: 2790 },
  { name: "11/07/2023", flash: 3908, long: 2000 },
  { name: "12/07/2023", flash: 4800, long: 3181 },
  { name: "13/07/2023", flash: 3700, long: 3500 },
  { name: "14/07/2023", flash: 4300, long: 2700 },
  { name: "15/07/2023", flash: 2400, long: 2400 },
  { name: "16/07/2023", flash: 1398, long: 2210 },
  { name: "17/07/2023", flash: 8000, long: 2290 },
  { name: "18/07/2023", flash: 3908, long: 2300 },
  { name: "19/07/2023", flash: 4800, long: 2181 },
  { name: "20/07/2023", flash: 3900, long: 2500 },
  { name: "21/07/2023", flash: 4300, long: 2100 },
  { name: "22/07/2023", flash: 2400, long: 2700 },
  { name: "23/07/2023", flash: 1398, long: 2210 },
  { name: "24/07/2023", flash: 2800, long: 1290 },
  { name: "25/07/2023", flash: 3908, long: 2500 },
  { name: "26/07/2023", flash: 4800, long: 2181 },
  { name: "27/07/2023", flash: 3800, long: 2500 },
  { name: "28/07/2023", flash: 4300, long: 2100 },
  { name: "29/07/2023", flash: 4300, long: 2200 },
  { name: "30/07/2023", flash: 2400, long: 2400 },
  { name: "31/07/2023", flash: 1398, long: 2210 },
  { name: "01/08/2023", flash: 9100, long: 2290 },
  { name: "02/08/2023", flash: 3908, long: 2200 },
  { name: "03/08/2023", flash: 4800, long: 2181 },
  { name: "04/08/2023", flash: 3800, long: 2800 },
  { name: "05/08/2023", flash: 4300, long: 2100 },
  { name: "06/08/2023", flash: 3908, long: 2000 },
  { name: "07/08/2023", flash: 4800, long: 2381 },
  { name: "08/08/2023", flash: 3800, long: 2300 },

];

function MDCChartsMixBar() {
  return (
    <ResponsiveContainer width="100%" height="100%" aspect={3}>
      <BarChart
        width={500}
        height={300}
        data={data}
        margin={{
          top: 20,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="flash" stackId="a" fill="#8884d8" />
        <Bar dataKey="long" stackId="a" fill="#82ca9d" />
      </BarChart>
    </ResponsiveContainer>
  );
}

export default MDCChartsMixBar;
