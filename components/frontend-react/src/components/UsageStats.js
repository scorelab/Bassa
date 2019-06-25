import React from 'react';
import {
  PieChart, Pie, Cell,
} from 'recharts';
import { makeStyles } from '@material-ui/core/styles';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const useStyles = makeStyles(theme => ({
  container: {
    display:'flex',
    justifyContent: 'center',
    alignItems: 'center',
    maxHeight: '100vh',
  },
  chart: {
    paddingLeft: 30,
  }
}))

const UsageStats = (props) => {
  const classes = useStyles();
  return (
    <div className={classes.container}>
      <PieChart width={800} height={400} className={classes.chart}>
        <Pie
          data={props.data}
          cx={180}
          cy={200}
          innerRadius={160}
          outerRadius={180}
          fill="#8884d8"
          paddingAngle={5}
          dataKey="value"
        >
          {
            props.data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
          }
        </Pie>
      </PieChart>
    </div>
  );
}

export default UsageStats;