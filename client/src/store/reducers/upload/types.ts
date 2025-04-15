export type uploadInitialState = {
    isLoading: boolean;
    summary: SummaryResponse | null;
    error: string | null;
};

export type SummaryRequest = {
    url: string;
};

export type SummaryResponse = {
    summary: string;
    transcript: string;
};
