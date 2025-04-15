import API from '@api/helpers';
import constants from '@/common/constants';

class UploadService {
    /**
     * Send video URL to backend and get summary
     * @param videoUrl
     * @returns
     */
    async summarize(videoUrl: string) {
        const endpoint = constants.ENDPOINTS.UPLOAD.SUMMARIZE;

        return await API.postRequest(endpoint, {
            url: videoUrl,
        });
    }
}

const uploadInstance = Object.freeze(new UploadService());
export { uploadInstance as UploadService };
