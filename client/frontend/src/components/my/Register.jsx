import React from "react";
import { useParams } from "react-router-dom";

function Register() {
    const { userUUID } = useParams();
    return <h1>UUID from URL: {userUUID}</h1>;
}

export default Register;
