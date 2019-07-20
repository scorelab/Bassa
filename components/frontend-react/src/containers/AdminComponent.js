import React from 'react';
import Appbar from '../components/Appbar';
import { connect } from 'react-redux';
import { startAllDownloads, killAllDownloads } from '../actions/downloadActions'; 
import StartKillDownloads from '../components/StartKillDownloads';
import PendingSignupRequests from '../components/PendingSignupRequests';
import UsageStats from '../components/UsageStats';

const AdminComponent = (props) => {
  return (
    <div>
      <Appbar data-test="component-appbar" isloggedIn={true} />
      <StartKillDownloads data-test="component-start-kill-downloads" onStart={props.startDownloads} onKill={props.killDownloads} />
      <PendingSignupRequests data-test="component-pending-signup-requests" requestsList={props.requestsList}/>
      <UsageStats data-test="component-usage-statistics" data={props.usageStats}/>
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