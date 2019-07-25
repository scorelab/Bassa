import React from 'react';
import Appbar from '../components/Appbar';
import { connect } from 'react-redux';
import { startAllDownloads, killAllDownloads } from '../actions/downloadActions'; 
import StartKillDownloads from '../components/StartKillDownloads';
import PendingSignupRequests from '../components/PendingSignupRequests';
import UsageStats from '../components/UsageStats';

const AdminComponent = (props) => {
  const {startDownloads, killDownloads, requestsList, usageStats} = props;
  return (
    <div>
      <Appbar data-test="component-appbar" isloggedIn={true} />
      <StartKillDownloads data-test="component-start-kill-downloads" onStart={startDownloads} onKill={killDownloads} />
      <PendingSignupRequests data-test="component-pending-signup-requests" requestsList={requestsList}/>
      <UsageStats data-test="component-usage-statistics" data={usageStats}/>
    </div>
  )
}

const mapStateToProps = state => ({
  requestsList: state.userReducer.requests,
  usageStats: state.userReducer.stats
})

const mapDispatchToProps = dispatch => ({
  startDownloads: () => dispatch(startAllDownloads()),
  killDownloads: () => dispatch(killAllDownloads())
})
export default connect(mapStateToProps, mapDispatchToProps)(AdminComponent);