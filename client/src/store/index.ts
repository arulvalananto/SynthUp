import { configureStore } from '@reduxjs/toolkit';

import uploadReducer from '@store/reducers/upload';

const store = configureStore({
    reducer: {
        upload: uploadReducer,
    },
});

export default store;
