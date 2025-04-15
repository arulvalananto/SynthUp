import { ToastContainer } from 'react-toastify';

import './App.css';
import 'react-toastify/dist/ReactToastify.css';
import Home from './pages/Home';

function App() {
    return (
        <main>
            <Home />
            <ToastContainer
                autoClose={3000}
                className="custom-toast-container"
            />
        </main>
    );
}

export default App;
