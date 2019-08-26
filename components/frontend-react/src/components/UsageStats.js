import React, { useState } from 'react';
import { PieChart, Pie, Sector } from 'recharts';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  container: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    maxHeight: '100vh'
  },
  chart: {
    paddingLeft: 30
  }
}));

const renderActiveShape = props => {
  const RADIAN = Math.PI / 180;
  const {
    cx, // center's x-coordinate
    cy, // center's y-coordinate
    midAngle,
    innerRadius,
    outerRadius,
    startAngle,
    endAngle,
    fill,
    payload,
    percent,
    value
  } = props;
  const sin = Math.sin(-RADIAN * midAngle);
  const cos = Math.cos(-RADIAN * midAngle);
  const sx = cx + (outerRadius + 10) * cos;
  const sy = cy + (outerRadius + 10) * sin;
  const mx = cx + (outerRadius + 30) * cos;
  const my = cy + (outerRadius + 30) * sin;
  const ex = mx + (cos >= 0 ? 1 : -1) * 22;
  const ey = my;
  const textAnchor = cos >= 0 ? 'start' : 'end';

  /*
    Notations above represent:
    sin, cos: -sin(midAngle), -cos(midAngle) = cos(midAngle) used for connecting sx, sy to active sector
    sx, sy: starting x, y coordinates for path connecting active sector and data displayed
    mx, my: middle x, y coordinates
    ex, ey: ending x, y coordinates for the path 
  */

  return (
    <g>
      <text x={cx} y={cy} dy={8} textAnchor="middle" fill={fill}>
        {payload.name}
      </text>
      <Sector
        cx={cx}
        cy={cy}
        innerRadius={innerRadius}
        outerRadius={outerRadius}
        startAngle={startAngle}
        endAngle={endAngle}
        fill={fill}
      />
      <Sector
        cx={cx}
        cy={cy}
        startAngle={startAngle}
        endAngle={endAngle}
        innerRadius={outerRadius + 6}
        outerRadius={outerRadius + 10}
        fill={fill}
      />
      <path
        d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`}
        stroke={fill}
        fill="none"
      />
      <circle cx={ex} cy={ey} r={2} fill={fill} stroke="none" />
      <text
        x={ex + (cos >= 0 ? 1 : -1) * 12}
        y={ey}
        textAnchor={textAnchor}
        fill="#333"
      >{`${value} KB`}</text>
      <text
        x={ex + (cos >= 0 ? 1 : -1) * 12}
        y={ey}
        dy={18}
        textAnchor={textAnchor}
        fill="#999"
      >
        {`(Rate ${(percent * 100).toFixed(2)}%)`}
      </text>
    </g>
  );
};

const UsageStats = props => {
  const data = [];
  const [activeIndex, setActiveIndex] = useState(0);
  const { userData } = props;
  userData.map(obj =>
    data.push({ name: obj.user_name, value: parseInt(obj.size, 10) / 1000 })
  );
  const classes = useStyles();

  const handleActiveIndex = (_data, index) => {
    setActiveIndex(index);
  };

  return (
    <div className={classes.container}>
      <PieChart width={1000} height={600} className={classes.chart}>
        <Pie
          activeIndex={activeIndex}
          activeShape={renderActiveShape}
          data={data}
          innerRadius={160}
          outerRadius={180}
          fill="#8884d8"
          onMouseEnter={handleActiveIndex}
          dataKey="value"
        />
      </PieChart>
    </div>
  );
};

export default UsageStats;
