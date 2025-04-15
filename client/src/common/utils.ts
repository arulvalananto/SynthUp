/* eslint-disable @typescript-eslint/no-explicit-any */
import { AxiosError } from 'axios';
import { toast } from 'react-toastify';
import { GetThunkAPI } from '@reduxjs/toolkit';

import constants from './constants';

const { ERROR_TEXT, MESSAGE } = constants;

/**
 * Transforms a given error message to a more generalized format.
 *
 * @param {string} originalMessage - The original error message to be transformed.
 * @returns {string} The transformed error message.
 */
export const transformErrorMessage = (originalMessage: string) => {
    // Check if the error message contains "network-related"
    const errorMessage = originalMessage?.toLowerCase();
    if (errorMessage?.includes(ERROR_TEXT.NETWORK_RELATED)) {
        return MESSAGE.NETWORK_RELATED_OR_INSTANCE_SPECIFIC_ERROR;
    } else if (errorMessage === ERROR_TEXT.CANCELED) {
        return MESSAGE.REQUEST_WAS_CANCELLED;
    } else {
        return originalMessage;
    }
};

/**
 * Get a user-friendly error message from an error object, handling Axios errors and generic JavaScript errors.
 *
 * @param {unknown} error - The error object from which to extract the message.
 * @param {string} defaultMessage - The default error message.
 * @returns {string} A user-friendly error message or a default message if none is available.
 */
export const getErrorMessage = (
    error: unknown,
    defaultMessage = MESSAGE.SOMETHING_WENT_WRONG
): string => {
    let message = '';

    if (error instanceof AxiosError) {
        if (
            error.response &&
            error.response.data &&
            (error.response.data?.detail || error.response.data?.error)
        ) {
            message = error.response.data?.detail || error.response.data.error;
        } else {
            message = error.message;
        }
    } else if (error instanceof Error) {
        message = error.message;
    } else if (typeof error === 'string') {
        message = error;
    }

    return message ? transformErrorMessage(message) : defaultMessage;
};

/**
 * Processes an API error and displays a toast notification.
 *
 * @param {unknown} error - The error object.
 * @param {string} [defaultMessage=MESSAGE.SOMETHING_WENT_WRONG] - The default error message.
 * @returns {string} - The error message.
 */
export const handleAPIError = (
    error: unknown,
    defaultMessage: string
): string => {
    const message = getErrorMessage(error, defaultMessage);
    toast.error(message);
    return message;
};

/**
 * Handles the rejection of a thunk by processing the error and rejecting with a value.
 *
 * @param {unknown} error - The error object.
 * @param {GetThunkAPI<any>} thunkAPI - The thunk API object.
 * @param {string} defaultMessage - The default error message.
 * @returns {ReturnType<GetThunkAPI<any>['rejectWithValue']>} - The rejection value.
 */
export const handleThunkRejection = (
    error: unknown,
    thunkAPI: GetThunkAPI<any>,
    defaultMessage: string = MESSAGE.SOMETHING_WENT_WRONG
): ReturnType<GetThunkAPI<any>['rejectWithValue']> => {
    const message = handleAPIError(error, defaultMessage);
    return thunkAPI.rejectWithValue(message);
};
