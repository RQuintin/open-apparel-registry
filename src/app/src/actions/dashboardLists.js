import { createAction } from 'redux-act';

import csrfRequest from '../util/csrfRequest';

import {
    logErrorAndDispatchFailure,
    makeGetContributorsURL,
    makeDashboardFacilityListsURL,
    mapDjangoChoiceTuplesToSelectOptions,
} from '../util/util';

export const startFetchDashboardListContributors =
    createAction('START_FETCH_DASHBOARD_LIST_CONTRIBUTORS');
export const failFetchDashboardListContributors =
    createAction('FAIL_FETCH_DASHBOARD_LIST_CONTRIBUTORS');
export const completeFetchDashboardListContributors =
    createAction('COMPLETE_FETCH_DASHBOARD_LIST_CONTRIBUTORS');

export function fetchDashboardListContributors() {
    return (dispatch) => {
        dispatch(startFetchDashboardListContributors());

        return csrfRequest
            .get(makeGetContributorsURL())
            .then(({ data }) => mapDjangoChoiceTuplesToSelectOptions(data))
            .then(data => dispatch(completeFetchDashboardListContributors(data)))
            .catch(err => dispatch(logErrorAndDispatchFailure(
                err,
                'An error prevented fetching dashboard list contributors',
                failFetchDashboardListContributors,
            )));
    };
}

export const setDashboardListContributor =
    createAction('SET_DASHBOARD_LIST_CONTRIBUTOR');

export const startFetchDashboardFacilityLists =
    createAction('START_FETCH_DASHBOARD_FACILITY_LISTS');
export const failFetchDashboardFacilityLists =
    createAction('FAIL_FETCH_DASHBOARD_FACILITY_LISTS');
export const completeFetchDashboardFacilityLists =
    createAction('COMPLETE_FETCH_DASHBOARD_FACILITY_LISTS');
export const resetDashboardFacilityLists =
    createAction('RESET_DASHBOARD_FACILITY_LISTS');

export function fetchDashboardFacilityLists(contributor) {
    return (dispatch) => {
        dispatch(startFetchDashboardFacilityLists());

        return csrfRequest
            .get(makeDashboardFacilityListsURL(contributor))
            .then(({ data }) => dispatch(completeFetchDashboardFacilityLists(data)))
            .catch(err => dispatch(logErrorAndDispatchFailure(
                err,
                'An error prevented fetching facility lists',
                failFetchDashboardFacilityLists,
            )));
    };
}