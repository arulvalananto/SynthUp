const constants = {
    API_CONFIG: {
        AXIOS_TIMEOUT: 30000, // 30 seconds
        AXIOS_TIMEOUT_MESSAGE: 'Timeout exceeded',
    },
    ENDPOINTS: {
        PREFIX: '/api/v1',
        UPLOAD: {
            SUMMARIZE: '/summarize',
        },
    },
    STORE: {
        UPLOAD: 'upload',
    },
    ERROR_MESSAGE: {
        UNABLE_TO_FETCH_SUMMARY: 'Unable to fetch summary',
    },
    MESSAGE: {
        SOMETHING_WENT_WRONG: 'Something went wrong',
        NETWORK_RELATED_OR_INSTANCE_SPECIFIC_ERROR:
            'A network-related or instance-specific issue',
        REQUEST_WAS_CANCELLED: 'Request was cancelled',
    },
    ERROR_TEXT: {
        NETWORK_RELATED: 'network-related',
        CANCELED: 'canceled',
    },
};

export default Object.freeze(constants);
