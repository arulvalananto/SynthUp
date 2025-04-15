import API from '@api/helpers';
import constants from '@/common/constants';
import { SummaryRequest, SummaryResponse } from '@/store/reducers/upload/types';

class UploadService {
    /**
     * Send video URL to backend and get summary
     * @param videoUrl
     * @returns
     */
    async summarize(videoUrl: string) {
        const endpoint = constants.ENDPOINTS.UPLOAD.SUMMARIZE;

        return await API.postRequest<SummaryResponse, SummaryRequest>(
            endpoint,
            {
                url: videoUrl,
            }
        );
    }
}

const uploadInstance = Object.freeze(new UploadService());
export { uploadInstance as UploadService };
