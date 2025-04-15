import { createSlice } from '@reduxjs/toolkit';

import { summarize } from './thunk';
import { RootState } from '@store/types';
import constants from '@common/constants';
import { uploadInitialState } from './types';

const initialState: uploadInitialState = {
    isLoading: false,
    summary: '',
    error: '',
};

const uploadSlice = createSlice({
    name: constants.STORE.UPLOAD,
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(summarize.pending, (state) => {
                state.isLoading = true;
                state.summary = '';
                state.error = null;
            })
            .addCase(summarize.fulfilled, (state, action) => {
                state.isLoading = false;
                state.summary = action.payload?.summary || '';
            })
            .addCase(summarize.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload as string;
            });
    },
});

// export const {} = uploadSlice.actions;

export const uploadSelector = (state: RootState) => state.upload;

export default uploadSlice.reducer;
