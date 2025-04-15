import { Provider } from 'react-redux';

import App from './App';
import store from './store';

const AppWrapper: React.FC = () => {
    return (
        <Provider store={store}>
            <App />
        </Provider>
    );
};

export default AppWrapper;
