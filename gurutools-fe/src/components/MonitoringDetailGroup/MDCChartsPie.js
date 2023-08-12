import React from 'react'
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from 'recharts'

const data = [
    { name: "Sencilla, 1 Individual", value: 25 },
    { name: "Doble, 2 Matrimoniales", value: 45 },
    { name: "Luxury, 1 King Size", value: 7 },
    { name: "Penthouse, 1 King California", value: 2 },
 


]

const COLORS = ['#74b9ff', '#2ecc71', '#a29bfe', '#fab1a0', '#ff9ff3']

function MDCChartsPie() {
  return (
    <div style={{width: '100%', height: 500}}>
        <ResponsiveContainer>
            <PieChart>
                <Pie 
                dataKey="value"
                data={data}
                innerRadius={110}
                outerRadius={160}
                
                >
                    {data.map((entry, index) => (
                        <Cell key={"cell-${index}"} fill={COLORS[index % COLORS.length]}/>
                        
                    ) )}
                </Pie>
                <Tooltip />
            </PieChart>
        </ResponsiveContainer>
    </div>
  )
}

export default MDCChartsPie