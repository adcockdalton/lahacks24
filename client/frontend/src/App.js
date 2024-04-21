import "./App.css";

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Navigate,
} from "react-router-dom";

import Login from "./components/my/Login";
import Register from "./components/my/Register";
import Home from "./components/my/Home";

function App() {
    return (
        <>
            <Router>
                <Routes>
                    <Route exact path="/" element={<Login />} />
                    <Route path="/register/:userUUID" element={<Register />} />
                    <Route path="/home/:userUUID" element={<Home />} />
                    <Route path="*" element={<Navigate to="/" />} />
                </Routes>
            </Router>
        </>
    );
}

export default App;
