import React from 'react';
import { connect } from 'react-redux';
import Appbar from '../components/Appbar';
import {
  startAllDownloads,
  killAllDownloads
} from '../actions/downloadActions';
import StartKillDownloads from '../components/StartKillDownloads';
import PendingSignupRequests from '../components/PendingSignupRequests';
import UsageStats from '../components/UsageStats';
import SnackbarComponent from '../components/ToastComponent';

const AdminComponent = props => {
  const {
    startDownloads,
    killDownloads,
    requestsList,
    usageStats,
    isUserAdmin,
    hasUserApprovalFailed,
    haveDownloadsKilled,
    haveDownloadsStarted,
    errorMessage
  } = props;

  // eslint-disable-next-line consistent-return
  const renderSnackbar = () => {
    if (hasUserApprovalFailed) {
      return (
        <SnackbarComponent
          variant="error"
          didEventOccured={hasUserApprovalFailed}
          message={errorMessage.message}
        />
      );
    }
    if (haveDownloadsStarted) {
      return (
        <SnackbarComponent
          variant="info"
          didEventOccured={haveDownloadsStarted}
          message="Started downloading files!"
        />
      );
    }
    if (haveDownloadsKilled) {
      return (
        <SnackbarComponent
          variant="info"
          didEventOccured={haveDownloadsKilled}
          message="Killed files to be downloaded!"
        />
      );
    }
  };
  if (isUserAdmin) {
    return (
      <div>
        <Appbar data-test="component-appbar" isloggedIn />
        <StartKillDownloads
          data-test="component-start-kill-downloads"
          onStart={startDownloads}
          onKill={killDownloads}
        />
        <PendingSignupRequests
          data-test="component-pending-signup-requests"
          requestsList={requestsList}
        />
        <UsageStats
          data-test="component-usage-statistics"
          userData={usageStats}
        />
        {renderSnackbar()}
      </div>
    );
  }
  return (
    <div>
      <Appbar data-test="component-appbar" isloggedIn />
      You are not admin! Sorry, you cannot access this section{' '}
    </div>
  );
};

const mapStateToProps = state => ({
  requestsList: state.userReducer.requests,
  usageStats: state.userReducer.stats,
  isUserAdmin: state.userReducer.isUserAdmin,
  hasUserApprovalFailed: state.userReducer.hasUserApprovalFailed,
  haveDownloadsStarted: state.downloadReducer.haveDownloadsStarted,
  haveDownloadsKilled: state.downloadReducer.haveDownloadsKilled,
  errorMessage: state.userReducer.errorMessage
});

const mapDispatchToProps = dispatch => ({
  startDownloads: () => dispatch(startAllDownloads()),
  killDownloads: () => dispatch(killAllDownloads())
});
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AdminComponent);
