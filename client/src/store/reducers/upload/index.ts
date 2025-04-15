import { createSlice, PayloadAction } from '@reduxjs/toolkit';

import { summarize } from './thunk';
import { RootState } from '@store/types';
import constants from '@common/constants';
import { SummaryResponse, uploadInitialState } from './types';

const initialState: uploadInitialState = {
    isLoading: false,
    summary: null,
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
                state.summary = null;
                state.error = null;
            })
            .addCase(summarize.fulfilled, (state, action: PayloadAction<SummaryResponse>) => {
                state.isLoading = false;
                state.summary = action.payload || null;
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
