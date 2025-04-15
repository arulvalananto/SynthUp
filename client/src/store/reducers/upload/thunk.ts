import { createAsyncThunk } from '@reduxjs/toolkit';
import { UploadService } from '@/api/services/upload';
import { handleThunkRejection } from '@/common/utils';
import constants from '@/common/constants';

export const summarize = createAsyncThunk(
    'upload/summarize',
    async (videoUrl: string, thunkAPI) => {
        try {
            const response = await UploadService.summarize(videoUrl);
            return response.data;
        } catch (error) {
            return handleThunkRejection(
                error,
                thunkAPI,
                constants.ERROR_MESSAGE.UNABLE_TO_FETCH_SUMMARY
            );
        }
    }
);
