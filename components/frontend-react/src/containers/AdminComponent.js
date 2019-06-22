import React from 'react';
import Appbar from '../components/Appbar';
import StartKillDownloads from '../components/StartKillDownloads';
import PendingSignupRequests from '../components/PendingSignupRequests';
import UsageStats from '../components/UsageStats';

import { requestsList } from '../stories/PendingSignupRequests.stories';
import { usageStatsData } from '../stories/UsageStats.stories';

const AdminComponent = (props) => {
  const startDownloads = () => {
    console.log('Start downloads');
  };
  
  const killDownloads = () => {
    console.log('Kill downloads');
  };
  
  return (
    <div>
      <Appbar data-test="component-appbar" isloggedIn={true} />
      <StartKillDownloads data-test="component-start-kill-downloads" onStart={startDownloads} onKill={killDownloads} />
      <PendingSignupRequests data-test="component-pending-signup-requests" requestsList={requestsList}/>
      <UsageStats data-test="component-usage-statistics" data={usageStatsData}/>
    </div>
  )
}

export default AdminComponent;