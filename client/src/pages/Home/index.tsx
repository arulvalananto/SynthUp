import { useDispatch, useSelector } from 'react-redux';
import { useEffect, useMemo, useState } from 'react';

import logo from '@assets/logo.svg';
import { AppDispatch } from '@store/types';
import UploadForm from '@components/RequestForm';
import { summarize } from '@store/reducers/upload/thunk';
import { uploadSelector } from '@/store/reducers/upload';

export default function Home() {
    const dispatch = useDispatch<AppDispatch>();
    const { isLoading, summary } = useSelector(uploadSelector);
    const [isSpeaking, setIsSpeaking] = useState(false);
    const estimatedMinutes = useMemo(() => summary ? Math.max(1, Math.ceil(summary.summary.split(/\s+/).length / 150)) : 0, [summary]);

    useEffect(() => () => window.speechSynthesis?.cancel(), []);

    const handleSubmit = async (videoUrl: string) => {
        window.speechSynthesis?.cancel();
        setIsSpeaking(false);
        dispatch(summarize(videoUrl));
    };

    const toggleSpeech = () => {
        if (!summary || !('speechSynthesis' in window)) return;
        if (isSpeaking) { window.speechSynthesis.cancel(); setIsSpeaking(false); return; }
        const utterance = new SpeechSynthesisUtterance(summary.summary);
        utterance.rate = 0.95;
        utterance.onend = () => setIsSpeaking(false);
        utterance.onerror = () => setIsSpeaking(false);
        window.speechSynthesis.speak(utterance);
        setIsSpeaking(true);
    };

    return (
        <div className="app-shell">
            <section className="hero">
                <div>
                    <img src={logo} alt="SynthUp Logo" />
                </div>
                <h1>Long videos, distilled into your next good listen.</h1>
                <p className="lede">Drop in a public YouTube link. We turn its available transcript into a short, focused recap you can read or play aloud.</p>
                <UploadForm onSubmit={handleSubmit} />
                <p className="helper">Currently supports public YouTube videos with available captions.</p>
            </section>
            {isLoading && <section className="status-card" aria-live="polite"><span className="pulse" /><div><strong>Building your recap</strong><p>Fetching captions and finding the important bits.</p></div></section>}
            {summary && (
                <section className="result-card">
                    <div className="result-meta"><span>YOUR SYNTH</span><span>~{estimatedMinutes} MIN LISTEN</span></div>
                    <h2>Your quick take</h2><p className="summary-copy">{summary.summary}</p>
                    <div className="player-row"><button className="listen-button" onClick={toggleSpeech} type="button"><span aria-hidden="true">{isSpeaking ? '■' : '▶'}</span> {isSpeaking ? 'Stop listening' : 'Listen to summary'}</button><span className="caption-note">Browser voice preview</span></div>
                    <details><summary>View source transcript</summary><p className="transcript">{summary.transcript}</p></details>
                </section>
            )}
        </div>
    );
}
