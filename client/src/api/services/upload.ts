import axios from 'axios';
import constants from '@/common/constants';

class UploadService {
    /**
     * Send video URL to backend and get summary
     * @param videoUrl
     * @returns
     */
    async summarize(videoUrl: string) {
        const baseURL =
            import.meta.env.VITE_APP_AI_API_URL + constants.ENDPOINTS.PREFIX;
        const endpoint = `${baseURL}${constants.ENDPOINTS.UPLOAD.SUMMARIZE}`;

        return await axios.post(endpoint, {
            url: videoUrl,
        });
    }
}

const uploadInstance = Object.freeze(new UploadService());
export { uploadInstance as UploadService };
