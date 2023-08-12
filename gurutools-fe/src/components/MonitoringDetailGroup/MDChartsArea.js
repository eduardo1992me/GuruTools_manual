import React from 'react'
import { Area, AreaChart, CartesianAxis, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const data = [
    { name: "Ago-1", guruhotel: 123, expedia: 115, booking: 135 },
    { name: "Ago-2", guruhotel: 111, expedia: 115, booking: 135 },
    { name: "Ago-3", guruhotel: 115, expedia: 120, booking: 100 },
    { name: "Ago-4", guruhotel: 140, expedia: 135, booking: 150 },

  ];
  

function MDChartsArea() {
  return (
    <ResponsiveContainer width="100%" aspect={2}>
        <AreaChart
        width={400}
        height={300}
        data={data}
        margin={{
            top:10,
            right:10,
            left:0,
            bottom:0
        }}
        >
        <CartesianGrid strokeDasharray="3 3"/>
        <XAxis dataKey="name"/>
        <YAxis />
        <Tooltip/>
        <Area type="monotone" dataKey="guruhotel" stackId="1" stroke='#FD9937' fill='#FD9937'/>
        <Area type="monotone" dataKey="expedia" stackId="1" stroke='#f1c40f' fill='#f1c40f'/>
        <Area type="monotone" dataKey="booking" stackId="1" stroke='#3498db' fill='#3498db'/>
        </AreaChart>

    </ResponsiveContainer>
  )
}

export default MDChartsArea