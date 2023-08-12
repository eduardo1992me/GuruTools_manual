import React from "react";
import {
  ResponsiveContainer,
  LineChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  Line,
} from "recharts";
const data = [
  { name: "10/07/2023", Guruhotel: 123, Expedia: 115, Booking: 135 },
  { name: "17/07/2023", Guruhotel: 111, Expedia: 115, Booking: 135 },
  { name: "24/07/2023", Guruhotel: 115, Expedia: 120, Booking: 100 },
  { name: "31/07/2023", Guruhotel: 85, Expedia: 98, Booking: 90 },
  { name: "7/08/2023", Guruhotel: 135, Expedia: 140, Booking: 155 },
  { name: "14/08/2023", Guruhotel: 130, Expedia: 132, Booking: 148 },
  { name: "21/08/2023", Guruhotel: 138, Expedia: 127, Booking: 152 },
];

function MDCChartsLine() {
  return (
    <ResponsiveContainer width="100%" aspect={2}>
      <LineChart
        width={730}
        height={250}
        data={data}
        margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="Guruhotel" stroke="#FD9937" strokeWidth={4} fill="#FD9937" />
        <Line type="monotone" dataKey="Expedia" stroke="#f1c40f" fill="#f1c40f" />
        <Line type="monotone" dataKey="Booking" stroke="#3498db" fill="#3498db" />
      </LineChart>
    </ResponsiveContainer>
  );
}

export default MDCChartsLine;
