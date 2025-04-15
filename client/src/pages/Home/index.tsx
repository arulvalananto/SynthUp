import { useDispatch, useSelector } from 'react-redux';

import UploadForm from '@components/RequestForm';
import { AppDispatch, RootState } from '@store/types';
import { summarize } from '@store/reducers/upload/thunk';

export default function Home() {
    const dispatch = useDispatch<AppDispatch>();
    const { isLoading, error, summary } = useSelector(
        (state: RootState) => state.upload
    );

    const handleSubmit = async (videoUrl: string) => {
        dispatch(summarize(videoUrl));
    };

    return (
        <div className="max-w-xl mx-auto mt-10 p-6 shadow rounded bg-white">
            <h1 className="text-2xl font-bold mb-4">
                SynthUp: Video Summarizer
            </h1>
            <UploadForm onSubmit={handleSubmit} />
            {isLoading && <p className="mt-4 text-blue-600">Summarizing...</p>}
            {error && <p className="mt-4 text-red-600">{error}</p>}
            {summary && (
                <div className="mt-6 p-4 bg-gray-100 rounded">
                    <h2 className="font-semibold">Summary:</h2>
                    <p className="mt-2">{summary}</p>
                </div>
            )}
        </div>
    );
}
