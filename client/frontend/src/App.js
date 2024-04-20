import "./App.css";

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Navigate,
} from "react-router-dom";

import Login from "./components/Login";
import Register from "./components/Register";
import Home from "./components/Home";

function App() {
    return (
        <>
            <Router>
                <Routes>
                    <Route exact path="/" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/home" element={<Home />} />
                    <Route path="*" element={<Navigate to="/" />} />
                </Routes>
            </Router>
        </>
    );
}

export default App;
